# Nexus - Personal AI Assistant with Local LLM Integration

## Overview

**Nexus** is a fully offline voice-activated personal assistant built in Python, designed to automate tasks and engage in natural language conversations using a locally hosted Large Language Model (LLM).  
It mimics a simple form of "Jarvis" that understands commands, executes them, and falls back to an LLM when necessary for casual conversation or general queries.

---

## Features

- **Voice Recognition:** Uses `speech_recognition` + `sounddevice` for speech input.
- **Text-To-Speech:** Converts AI responses into speech using `pyttsx3`.
- **Command Execution:** Handles multiple pre-programmed tasks:
  - WhatsApp messaging (sendMessage, add_new_contact)
  - News reading
  - Web search automation
  - Keyboard control
  - Speed tests
  - Dictation
- **Local LLM Integration:** Uses `llama.cpp` to load OpenHermes 2.5 model for general-purpose question answering and casual conversations.
- **Offline Operation:** Fully functional without internet connection (after initial model setup).
- **Privacy Friendly:** No data leaves your machine.
- **Packaged Application:** Distributed as a standalone executable using PyInstaller.

---

## Tech Stack

- Python 3.13
- PyInstaller
- llama.cpp (Local model inference)
- OpenHermes 2.5 model
- pyttsx3 (Text-to-Speech)
- speech_recognition (Speech input)
- sounddevice (Microphone access)
- pyautogui (Keyboard/mouse automation)
- BeautifulSoup (Web scraping)
- requests (API/web access)
- speedtest (Network speed test)

---

## Basic Flow
1. App starts and waits for user speech.
2. Speech is converted to text.
3. If the input matches a hardcoded command:
   - Task is executed (WhatsApp message, web search, news, etc.)
4. If not recognized:
   - Input is passed to LLM via `llama.cpp`.
   - Model generates a natural reply.
   - Reply is spoken out via `pyttsx3`.

---

## Limitations
1. Requires initial model download (~4-5 GB).
2. LLM inference may consume significant RAM (4GB minimum for quantized models).
3. Currently supports English speech only.

## Future Plans
1. Multi-language support
2. GUI improvements
3. More offline tools integration
4. Intent classification improvement

## Credits
1. llama.cpp
2. OpenHermes 2.5 (Mistral-based model)
3. Pyttsx3
4. SpeechRecognition
5. BeautifulSoup
6. Python community!
