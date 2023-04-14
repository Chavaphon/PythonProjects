import speech_recognition
import openai
import pyttsx3
import keyboard

#  READ ME
#  Wake up word: "hey alice"
#  To make the bot output answers without it speaking, use "write me a" phrase

#  Get an account to get new API key
openai.api_key = "###"
recogniser = speech_recognition.Recognizer()
messages = []
GotMessage = False
Name = "alice"  # Artificial Labile Intelligence Cybernated Existence (by Ivan my good friend)
print(f"{Name} is ready to assist you!\n")
while 1:
    try:
        if keyboard.is_pressed("alt"):
            with speech_recognition.Microphone() as mic:
                print(f"Listening...")
                # Adjust noise
                recogniser.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recogniser.listen(mic)
                # listen
                message = recogniser.recognize_google(audio)
                message = message.lower()
                print(f"You said: {message}\n")
            #  wake up word recognition
            if f"hey {Name}" in message:
                messages.append({"role": "user", "content": message})

                print(f"Thinking...")
                messages.append({"role": "user", "content": message})
                response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
                reply = response["choices"][0]["message"]["content"]
                messages.append({"role": "assistant", "content": reply})
                print(f"{reply}\n")
                if f"write me a" not in message:
                    engine = pyttsx3.init()
                    engine.setProperty("rate", 160)
                    engine.say(reply)
                    engine.runAndWait()
                print(f"Anymore question?")
    except speech_recognition.exceptions.UnknownValueError:
        recogniser = speech_recognition.Recognizer()
        continue
    except KeyboardInterrupt:
        print(f"Goodbye!")