import os 
import pyautogui
import webbrowser
import pyttsx3
import sounddevice as sd
import numpy as np
import speech_recognition as sr
from time import sleep

# Text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Recording audio using sounddevice
def record_audio(duration=4, fs=44100):
    print("Listening...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    return sr.AudioData(recording.tobytes(), fs, 2)

# Speech recognition
def takeCommand():
    recognizer = sr.Recognizer()
    audio = record_audio()

    try:
        print("Understanding...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception:
        print("Say that again")
        return "None"
    return query.lower()

# Dictionary of apps with correct executable names
dictapp = {
    "command prompt": "cmd",
    "paint": "mspaint",
    "word": "winword",
    "excel": "excel",
    "chrome": "chrome",
    "vscode": "code",
    "powerpoint": "powerpnt",
    "notepad": "notepad",
    "spotify": "spotify",
    "telegram": "telegram",
    "discord": "discord",
    "calculator": "calc",
    "task manager": "taskmgr",
    "control panel": "control"
}

def openappweb(query):
    speak("Launching sir...")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","").replace("jarvis","").replace("launch","").replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        for app in dictapp:
            if app in query:
                os.system(f"start {dictapp[app]}")
                return
        speak("Application not found")

def closeappweb(query):
    speak("Closing sir...")
    # Closing browser tabs using pyautogui
    if "tab" in query:
        words = query.split()
        try:
            number = next(int(word) for word in words if word.isdigit())
            for _ in range(number):
                pyautogui.hotkey("ctrl", "w")
                sleep(0.3)
            speak(f"{number} tabs closed")
        except:
            pyautogui.hotkey("ctrl", "w")
            speak("One tab closed")
    else:
        for app in dictapp:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
                return
        speak("Application not found")