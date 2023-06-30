import openai
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Assuming these models are defined in a separate 'models.py' file
from models import Audio2Text, Text2Text, Text2Image

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
with app.app_context():
    db.create_all()  # Ensure all the tables exist

audio_file_path = "/Users/mattmacfarlane/Development/code/phase-4b/voice-to-vision/server/test_audio/In the Bible, Drake.m4a"

try:
    # Transcribe audio
    with open(audio_file_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        transcript_text = transcript.get('text')
except Exception as e:
    print(f"Error during transcription: {e}")
    transcript_text = None

if transcript_text:
    # Save audio to text
    audio2text = Audio2Text(audio_file_path=audio_file_path, transcript_text=transcript_text)
    with app.app_context():
        db.session.add(audio2text)
        db.session.commit()
    print("Saved transcript to database.")
else:
    print("Transcription returned no text.")

try:
    # Create text prompt
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Generate a visual prompt for OpenAI DALL-E 2 using the lyrics from: {transcript_text} and excluding repetition in the transcript. Use the full transcript, not just the beginning. Use artistic styling and photographic / artistic styling and terms",
        max_tokens=200,
        temperature=0
    )

    choices = response.get('choices', [])
    dalle2prompt = choices[0]['text'].strip() if choices else ""
    # Remove special characters
    dalle2prompt = ''.join(e for e in dalle2prompt if e.isalnum() or e.isspace())
except Exception as e:
    print(f"Error during DALL-E 2 prompt generation: {e}")
    dalle2prompt = None

if dalle2prompt:
    # Save text to text
    text2text = Text2Text(transcript_text=transcript_text, prompt=dalle2prompt, response=dalle2prompt)
    with app.app_context():
        db.session.add(text2text)
        db.session.commit()
else:
    print("No prompt generated.")

try:
    # Generate image
    response = openai.Image.create(
        prompt=dalle2prompt,
        n=1,
        size="1024x1024"
    )

    image_url = response["data"][0]["url"] if response.get("data") else None
except Exception as e:
    print(f"Error during image generation: {e}")
    image_url = None

if image_url:
    # Save text to image
    text2image = Text2Image(prompt=dalle2prompt, image_path=image_url)
    with app.app_context():
        db.session.add(text2image)
        db.session.commit()
    print(image_url)
else:
    print("No image generated.")
