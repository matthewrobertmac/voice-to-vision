#!/usr/bin/env python3

import openai
import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.utils import secure_filename
from flask_cors import CORS
from google.cloud import storage 
import io
import requests

# Assuming these models are defined in a separate 'models.py' file
from models import db, Audio2Text, Text2Text, Text2Image, Audio

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

UPLOAD_FOLDER = '/Users/mattmacfarlane/Development/code/phase-4b/voice-to-vision/server/upload_folder'  # Change this to your path
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

storage_client = storage.Client() 

def save_to_gcs(image_content, filename, bucket_name, image_number):
    """Save image_content to a file named filename in bucket_name on GCS."""
    bucket = storage_client.get_bucket(bucket_name)

    # Append image number to filename
    base_name, extension = os.path.splitext(filename)
    filename = f"{base_name}_{image_number}{extension}"

    # Check if a file with the same name exists and append a counter if it does
    counter = 1
    while bucket.blob(filename).exists():
        filename = f"{base_name}_{counter}{extension}"
        counter += 1

    blob = bucket.blob(filename)

    blob.upload_from_string(image_content, content_type='image/jpeg')

    # Make the blob publicly accessible
    blob.make_public()

    return blob.public_url



migrate = Migrate(app, db)

db.init_app(app)
CORS(app)  # Enable CORS for all routes

with app.app_context():  # Set up an application context
    db.create_all()  # Ensure all the tables exist
    #audio_file_path = "/Users/mattmacfarlane/Development/code/phase-4b/voice-to-vision/server/upload_folder/y2mate.is - Bee Gees - Night Fever-SkypZuY6ZvA-192k-1688158768.mp3"

    #Your existing code...
    #audio_file_path = "/Users/mattmacfarlane/Development/code/phase-4b/voice-to-vision/server/test_audio/oklahoma.mp3"
    #audio_file_path = "/Users/mattmacfarlane/Development/code/phase-4b/voice-to-vision/server/test_audio/final_countdown.mp3"
    #audio_file_path = "/Users/mattmacfarlane/Development/code/phase-4b/voice-to-vision/server/upload_folder/Opening_Oh_What_A_Beautiful_Mornin_From.mp3"
    audio_file_path = "/Users/mattmacfarlane/Development/code/phase-4b/voice-to-vision/server/upload_folder/y2mate.is_-_CLARA_LUCIANI_-_LA_GRENADE_-_AUDIO_-h59X4qvGFvI-192k-1688076381.mp3"
    

    #Transcribe audio
    audio_file = open(audio_file_path, "rb")
    transcript = openai.Audio.translate("whisper-1", audio_file)
  #  transcript = openai.Audio.transcribe("whisper-1", audio_file)

    #Save audio to text
    audio2text = Audio2Text(audio_file_path=audio_file_path, transcript_text=transcript['text'])
    db.session.add(audio2text)
    db.session.commit()

    print("Saved transcript to database.")

    #Create text prompt
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Generate a visual prompt for OpenAI DALL-E 2 using the lyrics from: {transcript} and excluding repetition in the transcript. Use the full transcript, not just the beginning. Use artistic styling and photographic / artistic styling and terms",
        #prompt=f"Render a composite illustration that visually interprets the entire lyrics from the provided transcript {transcript}. Ensure to avoid any repetitive elements from the transcript in your creation. Embrace a blend of artistic and photographic styles in your execution. Remember to incorporate a rich array of artistic techniques throughout the entirety of the image, and not just focusing on the initial parts. The final output should be a fusion of both creative artistic expression and photographic realism.",
        #prompt=f"Generate a stunning and dramatic watercolor painting from the provided transcript {transcript}, including bright colors to represent areas of positive sentiment and dark colors to represent areas of negative sentiment.",

        max_tokens=200,
        temperature=0
    )

    choices = response['choices']
    if len(choices) > 0:
        dalle2prompt = choices[0]['text'].strip()
    else:
        dalle2prompt = ""

    #Remove special characters
    dalle2prompt = ''.join(e for e in dalle2prompt if e.isalnum() or e.isspace())

    #Save text to text
    text2text = Text2Text(transcript_text=transcript['text'], prompt=dalle2prompt, response=dalle2prompt)
    db.session.add(text2text)
    db.session.commit()

    for i in range(1):
        # Generate image
        response = openai.Image.create(
            prompt=dalle2prompt,
            n=1,
            size="1024x1024"
        )

        image_url = response["data"][0]["url"]

        original_filename = image_url.split('/')[-1] 

        image_content = requests.get(image_url).content

        gcs_bucket_name = 'voice2vision'

        gcs_image_url = save_to_gcs(image_content, original_filename, gcs_bucket_name, i+1) 

        # Save text to image
        text2image = Text2Image(prompt=dalle2prompt, image_path=gcs_image_url)
        db.session.add(text2image)

    db.session.commit()

    print("Images generated and saved.")
