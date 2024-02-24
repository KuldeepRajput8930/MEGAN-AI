import os
import pygame

voice2 = 'en-GB-SoniaNeural'

def speak(data):
    voice = 'en-US-SteffanNeural'
    command = f'edge-tts --voice "{voice2}" --text "{data}" --write-media "data.mp3"'
    os.system(command)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("data.mp3")
    
    try:
        pygame.mixer.music.play()
        # Allow the mixer to initialize
        pygame.time.wait(100)
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(100)  # Adjust tick rate to reduce delay
    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

speak("Welcome back to Detroit, where every choice shapes our destiny. What path shall we tread today?")
    
        