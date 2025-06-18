import requests
import json
import pyttsx3
import speech_recognition as sr
import sounddevice as sd

# Your API key here
API_KEY = "YOUR_API_KEY"  # <-- Replace with your NewsAPI key

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Sounddevice based recording
def record_audio(duration=5, fs=44100):
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
        print(f"You said: {query}\n")
    except Exception:
        print("Say that again")
        return "None"
    return query.lower()

def latestnews():
    API_KEY = "b21ab09c2d6f35dd2ff63d4cc9b0b569"

    api_dict = {
        "business": f"https://gnews.io/api/v4/top-headlines?topic=business&lang=en&country=in&token={API_KEY}",
        "entertainment": f"https://gnews.io/api/v4/top-headlines?topic=entertainment&lang=en&country=in&token={API_KEY}",
        "health": f"https://gnews.io/api/v4/top-headlines?topic=health&lang=en&country=in&token={API_KEY}",
        "science": f"https://gnews.io/api/v4/top-headlines?topic=science&lang=en&country=in&token={API_KEY}",
        "sports": f"https://gnews.io/api/v4/top-headlines?topic=sports&lang=en&country=in&token={API_KEY}",
        "technology": f"https://gnews.io/api/v4/top-headlines?topic=technology&lang=en&country=in&token={API_KEY}",
        "gaming": f"https://gnews.io/api/v4/search?q=gaming&lang=en&country=in&token={API_KEY}"
    }


    speak("Which field news do you want? business, entertainment, health, science, sports or technology?")
    field = takeCommand()

    url = api_dict.get(field)
    if not url:
        speak("Sorry, I did not find that category.")
        return

    news = requests.get(url).json()

    if news.get("status") != "ok":
        speak("Sorry, couldn't fetch news.")
        return

    speak("Here are the top headlines.")
    articles = news.get("articles", [])

    for article in articles:
        title = article.get("title", "")
        link = article.get("url", "")
        print(title)
        speak(title)
        print(f"More info: {link}")

        speak("Do you want to hear next news?")
        response = takeCommand()
        if "no" in response or "stop" in response:
            break

    speak("That's all for now.")

