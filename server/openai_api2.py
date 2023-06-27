import openai
import os
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from models import db, Audio2Text, Text2Text, Text2Image

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # change this to your db URI
db = SQLAlchemy(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

audio_file = open("/Users/mattmacfarlane/Development/code/phase-4b/voice-to-vision/server/test_audio/oklahoma.mp3", "rb")

# I assume openai.Audio.transcribe is a fictional method. To the best of my knowledge, OpenAI doesn't provide such service. 
# So, you should replace it with the correct service/method.
transcript = openai.Audio.transcribe("whisper-1", audio_file)
transcript_text = transcript['text']

# insert into Audio2Text
audio2text = Audio2Text(audio_file_path=audio_file.name, transcript_text=transcript_text)
db.session.add(audio2text)
db.session.commit()

audio_file.close()

# Generate a response for Text2Text. You should replace it with the correct service/method.
response = openai.Completion.create(engine="text-davinci-002", prompt=transcript_text, max_tokens=60)

text2text = Text2Text(transcript_text=transcript_text, response=response['choices'][0]['text'].strip() if response['choices'] else "")
db.session.add(text2text)
db.session.commit()


# Insert into Text2Image
generated_text = response['choices'][0]['text'].strip() if response['choices'] else ""
text2image = Text2Image(prompt=generated_text)
db.session.add(text2image)
db.session.commit()

