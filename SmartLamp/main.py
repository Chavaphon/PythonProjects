import speech_recognition
from gpiozero import PWMLED
led26 = PWMLED(26)
led16 = PWMLED(16)
led6 = PWMLED(6)
led5 = PWMLED(5)

recogniser = speech_recognition.Recognizer()

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
                led26.value = 1
                led16.value = 1
                led6.value = 1
                led5.value = 1
            elif "lamp off" in message:
                led26.value = 0
                led16.value = 0
                led6.value = 0
                led5.value = 0
            else:
                for i in range(100):
                    if f"lamp {i}%" in message:
                        led26.value = i / 100
                        led16.value = i / 100
                        led6.value = i / 100
                        led5.value = i / 100
        except speech_recognition.exceptions.UnknownValueError:
            recogniser = speech_recognition.Recognizer()
            continue
    except KeyboardInterrupt:
        print(f"Terminated")
