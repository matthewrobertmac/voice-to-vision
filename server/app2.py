#!/usr/bin/env python3

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Audio2Text, Text2Text, Text2Image

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    newFile = Audio(audio_data=file.read())
    db.session.add(newFile)
    db.session.commit()
    return "File has been uploaded and stored into database."

@app.route('/audio2texts', methods=['GET'])
def get_audio2texts():
    audio2texts = Audio2Text.query.all()
    return jsonify([audio2text.to_dict() for audio2text in audio2texts])

@app.route('/audio2texts', methods=['POST'])
def create_audio2text():
    data = request.get_json()
    audio2text = Audio2Text(**data)
    db.session.add(audio2text)
    db.session.commit()
    return jsonify(audio2text.to_dict()), 201

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

@app.route('/text2texts', methods=['GET'])
def get_text2texts():
    text2texts = Text2Text.query.all()
    return jsonify([text2text.to_dict() for text2text in text2texts])

@app.route('/text2texts', methods=['POST'])
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

@app.route('/text2texts/<int:text2text_id>', methods=['PATCH'])
def update_text2text(text2text_id):
    text2text = Text2Text.query.get(text2text_id)
    if not text2text:
        return jsonify({'message': 'Text2Text not found'}), 404

    data = request.get_json()
    text2text.source_text = data.get('source_text', text2text.source_text)
    text2text.translated_text = data.get('translated_text', text2text.translated_text)
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

@app.route('/text2images', methods=['GET'])
def get_text2images():
    text2images = Text2Image.query.all()
    return jsonify([text2image.to_dict() for text2image in text2images])

@app.route('/text2images', methods=['POST'])
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

@app.route('/text2images/<int:text2image_id>', methods=['PATCH'])
def update_text2image(text2image_id):
    text2image = Text2Image.query.get(text2image_id)
    if not text2image:
        return jsonify({'message': 'Text2Image not found'}), 404

    data = request.get_json()
    text2image.source_text = data.get('source_text', text2image.source_text)
    text2image.image_url = data.get('image_url', text2image.image_url)
    db.session.commit()
    return jsonify(text2image.to_dict())

@app.route('/text2images/<int:text2image_id>', methods=['DELETE'])
def delete_text2image(text2image_id):
    text2image = Text2Image.query.get(text2image_id)
    if text2image:
        db.session.delete(text2image)
        db.session.commit()
        return jsonify({'message': 'Text2Image deleted'})
    return jsonify({'message': 'Text2Image not found'}), 404

if __name__ == '__main__':
    app.run(port=7000, debug=True)
