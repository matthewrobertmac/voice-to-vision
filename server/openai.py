import os
from dotenv import load_dotenv
import openai
import sounddevice as sd
import soundfile as sf

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the function for recording audio
def record_audio(duration=5, sample_rate=44100):
    print("Recording audio...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()
    print("Audio recorded.")
    return audio, sample_rate

# Define the function for saving the recorded audio to a file
def save_audio(audio, sample_rate, file_path):
    sf.write(file_path, audio, sample_rate)

# Set the file path for the MP3 file
mp3_file = "/Users/mattmacfarlane/Development/code/phase-4b/voice-to-vision/server/test_audio/oklahoma.mp3"

# Define the file path for the recorded audio
recorded_audio_file = "/Users/mattmacfarlane/Development/code/phase-4b/voice-to-vision/server/test_audio/recorded_audio.wav"

# Check if the MP3 file exists
if os.path.exists(mp3_file):
    audio_file = open(mp3_file, "rb")
else:
    # Record audio if the MP3 file doesn't exist
    audio, sample_rate = record_audio()
    save_audio(audio, sample_rate, recorded_audio_file)
    audio_file = open(recorded_audio_file, "rb")

# Transcribe the audio to text using Whisper model
transcript = openai.Audio.transcribe("whisper-1", audio_file)

# Print the transcript
print("Transcript:", transcript)

# Text-to-Text

response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Generate a visual prompt for OpenAI DALL-E 2 using the lyrics from: {transcript}",
    max_tokens=75,
    temperature=0
)

choices = response['choices']
if len(choices) > 0:
    dalle2prompt = choices[0]['text'].strip()
else:
    dalle2prompt = ""

# Remove special characters
dalle2prompt = ''.join(e for e in dalle2prompt if e.isalnum() or e.isspace())

# Print only the dalle2prompt
print("DALLE-2 Prompt:", dalle2prompt)

# Text-to-Image

response = openai.Image.create(
    prompt=dalle2prompt,
    n=1,
    size="1024x1024"
)

# Print the response
print("Image Response:", response)
