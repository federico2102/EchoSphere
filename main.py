from helpers import generate_response, text_to_speech, speech_to_text
import pygame
import time

# Initialize pygame mixer
pygame.mixer.init()

def play_audio(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

def main(num_ais=2):
    last_message = "Hi there! How are you feeling today?"  # Starting conversation message
    max_turns = 10  # Limit the conversation to 10 exchanges

    # Define distinct voices for each AI
    voices = ["en-US-Wavenet-D", "en-US-Wavenet-F"]

    for turn in range(max_turns):
        # Determine the current AI based on the turn number
        current_voice = voices[turn % num_ais]

        # Generate response based on the last message, without labels
        response_text = generate_response(last_message)
        print(response_text)  # Print to console for tracking

        # Convert the response to speech and play it
        audio_file = text_to_speech(response_text, f"response_{turn + 1}.mp3", voice_name=current_voice)
        play_audio(audio_file)

        # Update the last message for the next response
        last_message = response_text

        # Optional delay for pacing
        time.sleep(1)

if __name__ == "__main__":
    main(num_ais=2)  # Default is 2 participants, but can increase for more
