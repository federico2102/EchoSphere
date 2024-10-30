import os
import io
from dotenv import load_dotenv
from google.cloud import texttospeech, speech
from transformers import pipeline

# Load environment variables from .env file
load_dotenv()

# Set the path to the Google Cloud credentials JSON file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "gcs_key.json")

# Initialize Google TTS and STT clients
tts_client = texttospeech.TextToSpeechClient()
stt_client = speech.SpeechClient()

# Use a larger model if available (e.g., GPT-J-6B)
generator = pipeline("text-generation", model="EleutherAI/gpt-j-6b")


def generate_response(last_message, max_retries=3):
    """
    Generates a conversational response based on the last message only.
    Avoids repetition and labels like 'Person A' or 'Person B'.
    """
    base_prompt = f"Respond naturally to the following message:\n\nMessage: {last_message}\nResponse:"

    for _ in range(max_retries):
        response = generator(base_prompt, max_new_tokens=50, num_return_sequences=1, truncation=True)
        generated_text = response[0]["generated_text"].split("Response:")[-1].strip()

        # Ensure the response is meaningful and not too repetitive
        if len(set(generated_text.split())) > 5 and generated_text != last_message:
            return generated_text

    # Fallback response if retries fail
    return "Could you tell me more about that?"

def text_to_speech(text, filename="output.mp3", voice_name="en-US-Wavenet-D"):
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name=voice_name,
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = tts_client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )
    with open(filename, "wb") as out:
        out.write(response.audio_content)
    return filename

def speech_to_text(filename):
    with io.open(filename, "rb") as audio_file:
        content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US"
    )
    response = stt_client.recognize(config=config, audio=audio)
    return response.results[0].alternatives[0].transcript if response.results else ""
