
import pyttsx3
import datetime
import webbrowser
import wikipedia
import os
import speech_recognition as sr

# Create recognizer instance
recognizer = sr.Recognizer()

# Set the microphone
mic = sr.Microphone(device_index=1)  # Replace 1 with the correct device index if needed

with mic as source:
    recognizer.adjust_for_ambient_noise(source)
    print("Say something...")
    audio = recognizer.listen(source)

# Initialize the engine
engine = pyttsx3.init()

def speak(text):
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am JARVIS. How can I help you?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception:
        speak("Sorry, I didn't catch that. Please say that again.")
        return "None"
    return query.lower()

def main():
    wish_me()
    while True:
        query = take_command()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia:")
                speak(results)
            except:
                speak("Sorry, no results found.")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open notepad' in query:
            os.system("notepad.exe")

        elif 'the time' in query:
            time_str = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time_str}")

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
