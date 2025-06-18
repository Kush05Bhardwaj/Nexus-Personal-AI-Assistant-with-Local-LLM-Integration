import pyttsx3
import speech_recognition as sr
import sounddevice as sd
import numpy as np
import requests
from bs4 import BeautifulSoup
import datetime
import pyautogui
import speedtest
from Whatsapp import sendMessage, add_new_contact


# Initialize Text-to-Speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    print(f"Assistant: {audio}")
    engine.say(audio)
    engine.runAndWait()

# Audio recording function
def record_audio(duration=5, fs=44100):
    print("Listening...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    return sr.AudioData(recording.tobytes(), fs, 2)

# Speech recognition function
def takeCommand():
    recognizer = sr.Recognizer()
    audio = record_audio()

    try:
        print("Understanding...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        print("Could not understand audio. Please say that again.")
        return None
    except sr.RequestError:
        print("Could not request results; check your internet connection.")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Core command processing
def process_command(query):
    if query is None:
        return

    if "go to sleep" in query:
        speak("Ok Boss! You can call me anytime")
        return "sleep"
    
    elif "exit" in query or "quit" in query:
        speak("Terminating Nexus")
        exit()

    elif "hello" in query:
        speak("Hello sir, how are you?")
    elif "i am fine" in query:
        speak("That's great, sir")
    elif "how are you" in query:
        speak("Perfect, sir")
    elif "thank you" in query:
        speak("You are welcome, sir")

    elif "google" in query:
        from SearchNow import searchGoogle
        searchGoogle(query)
    elif "youtube" in query:
        from SearchNow import searchYoutube
        searchYoutube(query)
    elif "wikipedia" in query:
        from SearchNow import searchWikipedia
        searchWikipedia(query)

    elif "temperature" in query or "weather" in query:
        search = "temperature in delhi"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        speak(f"Current {search} is {temp}")

    elif "the time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"Sir, the time is {strTime}")

    elif "open" in query:
        from Dictapp import openappweb
        openappweb(query)
    elif "close" in query:
        from Dictapp import closeappweb
        closeappweb(query)

    elif "pause" in query:
        pyautogui.press("k")
        speak("Video paused")
    elif "play" in query:
        pyautogui.press("k")
        speak("Video played")
    elif "mute" in query:
        pyautogui.press("m")
        speak("Video muted")

    elif "volume up" in query:
        from Keyboard import volumeup
        speak("Turning volume up, sir")
        volumeup()
    elif "volume down" in query:
        from Keyboard import volumedown
        speak("Turning volume down, sir")
        volumedown()

    elif "news" in query:
        from NewsRead import latestnews
        latestnews()

    elif "send whatsapp message" in query:
        sendMessage()

    elif "add whatsapp contact" in query:
        add_new_contact()

    elif "internet speed" in query:
        wifi = speedtest.Speedtest()
        upload_net = wifi.upload() / 1048576
        download_net = wifi.download() / 1048576
        speak(f"Download speed: {download_net:.2f} Mbps")
        speak(f"Upload speed: {upload_net:.2f} Mbps")

    elif "screenshot" in query:
        im = pyautogui.screenshot()
        im.save("ss.jpg")
        speak("Screenshot taken")

    

# Main Assistant Loop
if __name__ == "__main__":
    while True:
        query = takeCommand()
        if query is None:
            continue
        if "activate" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand()
                result = process_command(query)
                if result == "sleep":
                    break
