import pygame
import time
from gtts import gTTS
import speech_recognition as sr
from typing import Optional


async def play_audio(filename: str, text: str):
    tts = gTTS(text=text, lang="en")
    tts.save(f"{filename}.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load(f"{filename}.mp3")
    pygame.mixer.music.play()

    # Wait until playback is finished
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.quit()


async def listen() -> Optional[str]:
    """
    Listen for speech using speech_recognition with silence detection.
    Returns transcribed text or None if no speech detected.
    """
    recognizer = sr.Recognizer()

    # Adjust for ambient noise and set dynamic energy threshold
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        # Configure silence detection
        recognizer.dynamic_energy_threshold = True
        recognizer.energy_threshold = (
            300  # Minimum audio energy to consider for recording
        )
        recognizer.pause_threshold = (
            2.0  # Seconds of silence before considering the phrase complete
        )
        recognizer.phrase_threshold = 0.3  # Minimum seconds of speaking audio before we consider the speech a phrase

        print("Listening... (Will stop after 2 seconds of silence)")
        try:
            # Listen for speech with timeout
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

            try:
                text = recognizer.recognize_google(audio)
                print("You said:", text)
                return text
            except sr.UnknownValueError:
                print("Sorry, could not understand what you said.")
                return None
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                return None

        except sr.WaitTimeoutError:
            print("No speech detected within timeout period.")
            return None


# if __name__ == "__main__":
#     while True:
#         result = listen()
#         if result:
#             print("Transcribed:", result)
#         else:
#             print("No valid transcription")

#         response = input("\nContinue? (y/n): ")
#         if response.lower() != "y":
#             break
