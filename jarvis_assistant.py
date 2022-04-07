import pyttsx3  # For speech delivery
import datetime  # For date and time
import speech_recognition as sr  # For speech recognition
import webbrowser  # For opening in webbrowser
import wikipedia  # For searching through wikipedia
import os  # For using os functionality
import random  # For generating random integer

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # getting details of current voice
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    # Without this command, speech will not be audible to us.
    engine.runAndWait()


def welcome():
    hour = (datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir, Welcome back, how may I help you?")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir, Welcome back, how may I help you?")

    else:
        speak("Good Evening sir, Welcome back, how may I help you?")


def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source)
    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User query will be printed.
    except Exception as e:
        # It will be printed in case of improper voice
        print("Say that again please...")
        return "None"  # None string will be returned
    return query


if __name__ == "__main__":
    welcome()
    while True:
        # For opening files in google chrome
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
            "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
        query = takeCommand().lower()
        if 'play music' in query:
            musicdir = "D:\\Songs"
            songs = os.listdir(musicdir)
            rand = random.randint(0, (len(songs)-1))
            os.startfile(os.path.join(musicdir, songs[rand]))
        elif 'the time' in query:
            timepr = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {timepr}")
        elif 'open spotify' in query:
            os.startfile("spotify.exe")
        elif 'open google' in query:
            webbrowser.get('chrome').open("google.com")
        elif 'open youtube' in query:
            webbrowser.get('chrome').open("youtube.com")
        elif 'open quora' in query:
            webbrowser.get('chrome').open("quora.com")
        elif 'open twitter' in query:
            webbrowser.get('chrome').open("twitter.com")
        elif 'open gmail' in query:
            webbrowser.get('chrome').open("gmail.com")
        elif 'open code' in query:
            loc = "C:\\Users\\WELCOME\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(loc)
        elif 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia...")
                speak(result)
            except Exception as e:
                print("No matches found...")
                speak("No matches found...")
        elif 'exit' in query:
            exit()
