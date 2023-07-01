import openai
import gradio as gr
from werkzeug.utils import secure_filename

# Assuming these models are defined in a separate 'models.py' file
from models import db, Audio2Text, Text2Text, Text2Image, Audio

def process_audio(audio):
    # Save the uploaded audio file
    filename = secure_filename(audio.name)
    audio_path = f"./upload_folder/{filename}"
    audio.save(audio_path)

    # Transcribe audio
    audio_file = open(audio_path, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    # Save audio to text
    audio2text = Audio2Text(audio_file_path=audio_path, transcript_text=transcript['text'])
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

    return image_url

inputs = gr.inputs.File(label="Upload Audio")
outputs = gr.outputs.Image(type="pil")

gr.Interface(fn=process_audio, inputs=inputs, outputs=outputs).launch()