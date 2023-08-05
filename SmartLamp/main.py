import speech_recognition
from gpiozero import PWMLED
led26 = PWMLED(26)
led16 = PWMLED(16)
led6 = PWMLED(6)
led5 = PWMLED(5)
WordToPercent = {
    "thirty": 30,
    "fifty": 50,
    "seventy": 70,
}

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
                for ele in WordToPercent:
                    if f"lamp {ele} percent" in message:
                        led26.value = WordToPercent[ele]
                        led16.value = WordToPercent[ele]
                        led6.value = WordToPercent[ele]
                        led5.value = WordToPercent[ele]
        except speech_recognition.exceptions.UnknownValueError:
            recogniser = speech_recognition.Recognizer()
            continue
    except KeyboardInterrupt:
        print(f"Terminated")