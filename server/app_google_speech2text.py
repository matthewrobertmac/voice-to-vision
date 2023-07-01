#!/usr/bin/env python3

import openai
import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.utils import secure_filename
from flask_cors import CORS
import io
from google.cloud import storage 
from datetime import datetime, timedelta 
import tempfile
from pydub import AudioSegment
from google.cloud import speech 
# Assuming these models are defined in a separate 'models.py' file
from models import db, Audio2Text, Text2Text, Text2Image, Audio

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

storage_client = storage.Client() # it will auto-discover the credentials
bucket_name = 'voice2vision' # replace with your bucket name
bucket = storage_client.get_bucket(bucket_name)

UPLOAD_FOLDER = '/Users/mattmacfarlane/Development/code/phase-4b/voice-to-vision/server/upload_folder'  # Change this to your path
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

migrate = Migrate(app, db)

db.init_app(app)
CORS(app)  # Enable CORS for all routes

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part in the request', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    try:
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    except Exception as e:
        print(f"Error creating upload folder: {e}")
        return 'Error creating upload folder', 500

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    try:
        # Convert audio to WAV format
        wav_file_path = os.path.splitext(file_path)[0] + '.mp3'
        audio = AudioSegment.from_file(file_path, format='mp3')
        audio.export(wav_file_path, format='mp3')

        # Transcribe audio using Google Cloud Speech-to-Text
        client = speech.SpeechClient()
        with io.open(wav_file_path, 'rb') as audio_file:
            audio_data = audio_file.read()

        audio = speech.RecognitionAudio(content=audio_data)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="en-US",
        )
        response = client.recognize(config=config, audio=audio)
        transcript_text = response.results[0].alternatives[0].transcript
    except Exception as e:
        print(f"Error during transcription: {e}")
        transcript_text = None

    if transcript_text:
        new_audio = Audio(audio_data=audio_data)  # Pass the audio_data to the Audio model
        db.session.add(new_audio)
        db.session.commit()

        new_audio2text = Audio2Text(audio_file_path=file_path, transcript_text=transcript_text)
        db.session.add(new_audio2text)
        db.session.commit()
        return jsonify({'message': 'File uploaded and transcribed successfully'}), 200

    return 'Error transcribing audio', 400

@app.route('/audio2texts', methods=['GET'])
def get_audio2texts():
    audio2texts = Audio2Text.query.all()
    return jsonify([audio2text.to_dict() for audio2text in audio2texts])


@app.route('/audio2texts', methods=['POST'])
def create_audio2text():
    data = request.get_json()
    audio_id = data.get('audio_id')
    audio = Audio.query.get(audio_id)
    if audio is None:
        return 'Audio not found', 404

    try:
        # Transcribe audio
        transcript = openai.Audio.transcribe("whisper-1", audio.audio_data)
        transcript_text = transcript.get('text')
    except Exception as e:
        print(f"Error during transcription: {e}")
        transcript_text = None

    if transcript_text:
        audio2text = Audio2Text(audio_file_path=audio.audio_data, transcript_text=transcript_text)
        db.session.add(audio2text)
        db.session.commit()
        return jsonify(audio2text.to_dict()), 201

    return 'Error transcribing audio', 400


@app.route('/audio2texts/<int:audio2text_id>', methods=['GET'])
def get_audio2text(audio2text_id):
    audio2text = Audio2Text.query.get(audio2text_id)
    if audio2text:
        return jsonify(audio2text.to_dict())
    return jsonify({'message': 'Audio2Text not found'}), 404


@app.route('/audio2texts/<int:audio2text_id>', methods=['PATCH'])
def update_audio2text(audio2text_id):
    audio2text = Audio2Text.query.get(audio2text_id)
    if not audio2text:
        return jsonify({'message': 'Audio2Text not found'}), 404

    data = request.get_json()
    audio2text.audio_file_path = data.get('audio_file_path', audio2text.audio_file_path)
    audio2text.transcript_text = data.get('transcript_text', audio2text.transcript_text)
    db.session.commit()
    return jsonify(audio2text.to_dict())


@app.route('/audio2texts/<int:audio2text_id>', methods=['DELETE'])
def delete_audio2text(audio2text_id):
    audio2text = Audio2Text.query.get(audio2text_id)
    if audio2text:
        db.session.delete(audio2text)
        db.session.commit()
        return jsonify({'message': 'Audio2Text deleted'})
    return jsonify({'message': 'Audio2Text not found'}), 404


@app.route('/text2texts', methods=['GET', 'POST'])
def get_text2texts():
    text2texts = Text2Text.query.all()
    return jsonify([text2text.to_dict() for text2text in text2texts])


def create_text2text():
    data = request.get_json()
    text2text = Text2Text(**data)
    db.session.add(text2text)
    db.session.commit()
    return jsonify(text2text.to_dict()), 201


@app.route('/text2texts/<int:text2text_id>', methods=['GET'])
def get_text2text(text2text_id):
    text2text = Text2Text.query.get(text2text_id)
    if text2text:
        return jsonify(text2text.to_dict())
    return jsonify({'message': 'Text2Text not found'}), 404

### USE THIS PATCH TO ALLOW A USER TO UPLOAD A REVISED TRANSCRIPT 

@app.route('/text2texts/<int:text2text_id>', methods=['PATCH'])
def update_text2text(text2text_id):
    text2text = Text2Text.query.get(text2text_id)
    if not text2text:
        return jsonify({'message': 'Text2Text not found'}), 404

    data = request.get_json()
    text2text.transcript_text = data.get('transcript_text', text2text.transcript_text)
    text2text.prompt = data.get('prompt', text2text.prompt)
    text2text.response = data.get('response', text2text.response)
    db.session.commit()
    return jsonify(text2text.to_dict())


@app.route('/text2texts/<int:text2text_id>', methods=['DELETE'])
def delete_text2text(text2text_id):
    text2text = Text2Text.query.get(text2text_id)
    if text2text:
        db.session.delete(text2text)
        db.session.commit()
        return jsonify({'message': 'Text2Text deleted'})
    return jsonify({'message': 'Text2Text not found'}), 404


@app.route("/text2images", methods=["GET", "POST"])

def get_text2images():
    text2images = Text2Image.query.all()
    response = [
        {
            "id": text2image.id,
            "prompt": text2image.prompt,
            "image_url": text2image.image_path,  # Use image_path as image_url
        }
        for text2image in text2images
    ]
    return jsonify(response)

def create_text2image():
    data = request.get_json()
    text2image = Text2Image(**data)
    db.session.add(text2image)
    db.session.commit()
    return jsonify(text2image.to_dict()), 201


@app.route('/text2images/<int:text2image_id>', methods=['GET'])
def get_text2image(text2image_id):
    text2image = Text2Image.query.get(text2image_id)
    if text2image:
        return jsonify(text2image.to_dict())
    return jsonify({'message': 'Text2Image not found'}), 404


@app.route('/text2images/<int:text2image_id>', methods=['PATCH', 'DELETE'])
def update_text2image(text2image_id):
    text2image = Text2Image.query.get(text2image_id)
    if not text2image:
        return jsonify({'message': 'Text2Image not found'}), 404

    data = request.get_json()
    text2image.prompt = data.get('prompt', text2image.prompt)
    text2image.image_path = data.get('image_path', text2image.image_path)
    db.session.commit()
    return jsonify(text2image.to_dict())


def delete_text2image(text2image_id):
    text2image = Text2Image.query.get(text2image_id)
    if text2image:
        db.session.delete(text2image)
        db.session.commit()
        return jsonify({'message': 'Text2Image deleted'})
    return jsonify({'message': 'Text2Image not found'}), 404


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure all the tables exist

    app.run(port=7000, debug=True)
