import speech_recognition
import requests
from gpiozero import PWMLED
from time import sleep
led26 = PWMLED(26)
led16 = PWMLED(16)
led6 = PWMLED(6)
led5 = PWMLED(5)

def on(percentage):
    led26.value = percentage / 100
    led16.value = percentage / 100
    led6.value = percentage / 100
    led5.value = percentage / 100

def off():
    led26.value = 0
    led16.value = 0
    led6.value = 0
    led5.value = 0

recogniser = speech_recognition.Recognizer()

try:
    requests.get("https://www.google.com", timeout=5)

    on()
    sleep(1)
    off()

    while True:
        try:
            try:
                with speech_recognition.Microphone() as mic:
                    print(f"Listening...")
                    recogniser.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = recogniser.listen(mic)
                    message = recogniser.recognize_google(audio)
                    message = message.lower()
                print(f"You said: {message}\n")
                if "lamp on" in message:
                    on(100)
                elif "lamp off" in message:
                    off()
                else:
                    for i in range(100):
                        if f"lamp {i}%" in message:
                            on(i)
            except speech_recognition.exceptions.UnknownValueError:
                recogniser = speech_recognition.Recognizer()
                continue
        except KeyboardInterrupt:
            print(f"Terminated")
except requests.ConnectionError:
    print("Connection Failed")
