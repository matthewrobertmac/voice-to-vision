import openai
import os
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from models import db, Audio2Text, Text2Text, Text2Image

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models defined above...

db.create_all()  # Ensure all the tables exist

# Your existing code...

audio_file_path = "/Users/mattmacfarlane/Development/code/phase-4b/voice-to-vision/server/test_audio/oklahoma.mp3"

# Transcribe audio
audio_file = open(audio_file_path, "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

# Save audio to text
audio2text = Audio2Text(audio_file_path=audio_file_path, transcript_text=transcript['text'])
db.session.add(audio2text)
db.session.commit()

print("Saved transcript to database.")


# Create text prompt
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Generate a visual prompt for OpenAI DALL-E 2 using the lyrics from: {transcript} and excluding repetition in the transcript. Use the full transcript, not just the beginning. Use artistic styling and photographic / artistic styling and terms",
    max_tokens=200,
    temperature=0
)

choices = response['choices']
if len(choices) > 0:
    dalle2prompt = choices[0]['text'].strip()
else:
    dalle2prompt = ""

# Remove special characters
dalle2prompt = ''.join(e for e in dalle2prompt if e.isalnum() or e.isspace())

# Save text to text
text2text = Text2Text(transcript_text=transcript['text'], prompt=dalle2prompt, response=dalle2prompt)
db.session.add(text2text)
db.session.commit()

# Generate image
response = openai.Image.create(
    prompt=dalle2prompt,
    n=1,
    size="1024x1024"
)

image_url = response["data"][0]["url"]

# Save text to image

text2image = Text2Image(prompt=dalle2prompt, image_path=image_url)
db.session.add(text2image)
db.session.commit()

print(image_url)
