# Voice assistant Made for Code In Place 2024 that can play music on Youtube, tell time, write text, and search for something on Google. I named it Mehris. 
# inspired by the name of Chris and Mehran (ris+Meh= Mehris) 
# Special thanks to the Code In Place 2024 team for the inspiration and guidance and Jhankar Mahbub for the idea of the project.
# Md. Shakhawat Hossain | Computer Science and Engineering major @ North South University, Dhaka, Bangladesh

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import webbrowser
import tkinter as tk
from tkinter import messagebox

# Initialize recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Set the voice properties
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Function to take voice command
def take_command():
    try:
        with sr.Microphone() as source:
            talk("Hi, Mehris here. How can I help you?")
            print('Listening... :D')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            return command
    except sr.RequestError:
        talk("Sorry, I am having trouble connecting to the service.")
    except sr.UnknownValueError:
        talk("Sorry, I didn't catch that. Could you please repeat?")
    return ""

def run_mehris():
    """Execute commands based on voice input."""
    command = take_command()
    if command:
        print(f"Command: {command}")

        if 'play' in command:
            song = command.replace('play', '').strip()
            talk(f'Playing {song}')
            pywhatkit.playonyt(song)

        elif 'time' in command:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f'Current time is {current_time}')

        elif 'write' in command:
            text_to_write = command.replace('write', '').strip()
            print(f"Writing: {text_to_write}")
            talk(f'Writing {text_to_write}')

        elif 'search' in command:
            query = command.replace('search', '').strip()
            talk(f'Searching for {query} on Google')
            webbrowser.open(f"https://www.google.com/search?q={query}")

        else:
            talk('Please say the command again.')
    else:
        talk('I did not receive any command.')

def on_button_click():
    run_mehris()

# Creating the GUI
root = tk.Tk()
root.title("Mehris Voice Assistant")
root.geometry("600x400")

# Create a label
label = tk.Label(root, text="Please click on speak to activate Mehris", font=("Helvetica", 14))
label.pack(pady=20)

# Create a button
button = tk.Button(root, text="Speak Mehris :)", font=("Helvetica", 14), command=on_button_click)
button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
