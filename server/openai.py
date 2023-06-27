import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

mp3_file = "/Users/mattmacfarlane/Development/code/phase-4b/voice-to-vision/server/test_audio/oklahoma.mp3"
audio_file = open(f"{mp3_file}", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file) 


# print(transcript) 

# Text-to-Text

response = openai.Completion.create(
    model="text-davinci-003",
#   prompt=f"Create an ideal OpenAI DALLE-2 prompt based on themes and imagery pulled from the full text of: {transcript}, and not simply the beginning. The prompt should be concise, evocative, and encourage creative and imaginative visual interpretations. Consider using vivid language, sensory details, and emotional cues to inspire the Whisper model.",
#    prompt=f"Create an ideal OpenAI DALLE-2 prompt to generate album art for the lyrics and themes and imagery in the full {transcript}",
#    prompt=f"Transform lyrics into an ideal DALLE-2 or Stable Diffusion v2 prompt, for the purpose of generating images evokative of the lyrics. Use the full transcript, not just the beginning, in: {transcript}",
    prompt=f"Generate a visual prompt for OpenAI DALL-E 2 using the lyrics from: {transcript}",
    max_tokens=75,
    temperature=0
)

# to print JSON response: 
# print(response) 

choices = response['choices']
if len(choices) > 0:
    dalle2prompt = choices[0]['text'].strip()
else:
    dalle2prompt = ""

# Remove special characters
dalle2prompt = ''.join(e for e in dalle2prompt if e.isalnum() or e.isspace())

# prints only the dalle2prompt
print(dalle2prompt)

# Text-to-Image

response = openai.Image.create(
    prompt=dalle2prompt,
    n=1,
    size="1024x1024"
)

print(response)
