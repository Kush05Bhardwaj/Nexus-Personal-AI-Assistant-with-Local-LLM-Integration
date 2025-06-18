import customtkinter as ctk
import threading
import time
from Nexus_main import takeCommand, handle_query

def continuous_listen():
    while True:
        query = takeCommand()
        if query != "None" and query.strip() != "":
            handle_query(query)
        time.sleep(0.5)

def start_jarvis():
    threading.Thread(target=continuous_listen, daemon=True).start()

app = ctk.CTk()
app.geometry("400x300")
app.title("Nexus AI Assistant")

label = ctk.CTkLabel(app, text="Nexus Listening...", font=("Arial", 20))
label.pack(pady=100)

start_jarvis()

app.mainloop()
