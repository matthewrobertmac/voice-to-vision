import openai
import os

openai.api_key = "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" 

audio_file = open("/Users/mattmacfarlane/Development/code/phase-4b/voice-to-vision/server/test_audio/oklahoma.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
transcript_text = transcript['text']
total_length = len(transcript_text)
third_length = total_length // 3

transcript_first_third = transcript_text[:third_length]
transcript_second_third = transcript_text[third_length:2*third_length]
transcript_third_third = transcript_text[2*third_length:]

#print("Transcript First Third:")
#print(transcript_first_third)

#print("Transcript Second Third:")
#print(transcript_second_third)

#print("Transcript Third Third:")
#print(transcript_third_third)

#print(transcript)

response = openai.Completion.create(
    model="text-davinci-003",
#   prompt=f"Create an ideal OpenAI DALLE-2 prompt based on themes and imagery pulled from the full text of: {transcript}, and not simply the beginning. The prompt should be concise, evocative, and encourage creative and imaginative visual interpretations. Consider using vivid language, sensory details, and emotional cues to inspire the Whisper model.",
#    prompt=f"Create an ideal OpenAI DALLE-2 prompt to generate album art for the lyrics and themes and imagery in the full {transcript}",
#    prompt=f"Transform lyrics into an ideal DALLE-2 or Stable Diffusion v2 prompt, for the purpose of generating images evokative of the lyrics. Use the full transcript, not just the beginning, in: {transcript}",
    prompt=f"Generate a visual prompt for OpenAI DALL-E 2 using the lyrics from: {transcript} and excluding repetition in the transcript. Use the full transcript, not just the beginning. Use artistic styling and photographic / artistic styling and terms",
    max_tokens=200,
    temperature=0
)

first_third_response = openai.Completion.create(
    model='text-davinci-003',
    prompt = f'Generate a visual prompt for OpenAI DALL-E 2 using the transcript available here: {transcript_first_third}',
    max_tokens=200,
    temperature=0

)

second_third_response = openai.Completion.create(
    model='text-davinci-003',
    prompt = f'Generate a visual prompt for OpenAI DALL-E 2 using the second third of the transcript available here: {transcript_second_third}',
    max_tokens=200,
    temperature=0

)

third_third_response = openai.Completion.create(
    model='text-davinci-003',
    prompt = f'Generate a visual prompt for OpenAI DALL-E 2 using the last third of the transcript available here: {transcript_third_third}',
    max_tokens=200,
    temperature=0
    )

# print(response)
# print(first_third_response)
# print(second_third_response)
# print(third_third_response)

choices = response['choices']
if len(choices) > 0:
    dalle2prompt = choices[0]['text'].strip()
else:
    dalle2prompt = ""

# Remove special characters
dalle2prompt = ''.join(e for e in dalle2prompt if e.isalnum() or e.isspace())

# print(dalle2prompt)

choices_first_third = first_third_response['choices']
if len(choices_first_third) > 0:
    dalle2prompt_first_third = choices_first_third[0]['text'].strip()
else:
    dalle2prompt_first_third = ""

# Remove special characters
dalle2prompt_first_third = ''.join(e for e in dalle2prompt_first_third if e.isalnum() or e.isspace())

# print(dalle2prompt_first_third)

choices_second_third = second_third_response['choices']
if len(choices_second_third) > 0:
    dalle2prompt_second_third = choices_second_third[0]['text'].strip()
else:
    dalle2prompt_second_third = ""

# Remove special characters
dalle2prompt_second_third = ''.join(e for e in dalle2prompt_second_third if e.isalnum() or e.isspace())

# print(dalle2prompt_second_third)

choices_third_third = third_third_response['choices']
if len(choices_third_third) > 0:
    dalle2prompt_third_third = choices_third_third[0]['text'].strip()
else:
    dalle2prompt_third_third = ""

# Remove special characters
dalle2prompt_second_third = ''.join(e for e in dalle2prompt_third_third if e.isalnum() or e.isspace())

# print(dalle2prompt_third_third)

# Text-to-Image

response = openai.Image.create(
    prompt=dalle2prompt,
    n=1,
    size="1024x1024"
)

response_first_third = openai.Image.create(
    prompt=dalle2prompt_first_third,
    n=1,
    size="1024x1024"
)

response_second_third = openai.Image.create(
    prompt=dalle2prompt_second_third,
    n=1,
    size="1024x1024"
)

response_third_third = openai.Image.create(
    prompt=dalle2prompt_third_third,
    n=1,
    size="1024x1024"
)

print(response)
print(response_first_third)
print(response_second_third)
print(response_third_third)

