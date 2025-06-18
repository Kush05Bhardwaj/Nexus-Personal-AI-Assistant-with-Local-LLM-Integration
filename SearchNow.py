import pyttsx3
import speech_recognition as sr
import pywhatkit
import wikipedia
import webbrowser
import sounddevice as sd
import numpy as np

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def record_audio(duration=4, fs=44100):
    print("Listening...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    return sr.AudioData(recording.tobytes(), fs, 2)

def takeCommand():
    recognizer = sr.Recognizer()
    audio = record_audio()

    try:
        print("Understanding..")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception:
        print("Say that again")
        return "None"
    return query.lower()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("google search","").replace("google","")
        speak("This is what I found on Google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 1)
            speak(result)
        except:
            speak("No speakable output available")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found for your search!")
        query = query.replace("youtube search","").replace("youtube","")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from Wikipedia...")
        query = query.replace("wikipedia","").replace("search wikipedia","")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia..")
        print(results)
        speak(results)