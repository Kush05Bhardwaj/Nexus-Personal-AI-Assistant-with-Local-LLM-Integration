import pywhatkit
import pyttsx3
import sounddevice as sd
import speech_recognition as sr
from datetime import datetime, timedelta
from Contacts import get_contact, add_contact

# Initialize TTS Engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

# Text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Record voice using sounddevice
def record_audio(duration=5, fs=44100):
    print("Listening...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    return sr.AudioData(recording.tobytes(), fs, 2)

# Recognize voice to text
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

# Send WhatsApp message
def sendMessage():
    speak("Who do you want to message?")
    name = takeCommand()
    
    phone_number = get_contact(name)
    if not phone_number:
        speak("Sorry, I don't have this contact. Please add it first.")
        return

    speak("What should I say?")
    message = takeCommand()

    now = datetime.now()
    time_hour = now.hour
    time_minute = (now + timedelta(minutes=2)).minute

    speak(f"Sending message to {name}")
    pywhatkit.sendwhatmsg(phone_number, message, time_hour, time_minute)
    speak("Message scheduled successfully.")

# Add new contact
def add_new_contact():
    speak("Please say the contact name:")
    name = takeCommand()
    speak("Please say the phone number with country code, digit by digit.")
    number = input("Number (type manually for now): ")  # For safer input, can later convert speech digits
    add_contact(name, number)
    speak("Contact added successfully.")
