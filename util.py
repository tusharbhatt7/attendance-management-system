import tkinter as tk
from tkinter import messagebox
import face_recognition
import numpy as np
import os
import pickle

def get_button(window, text, color, command, fg='white'):
    return tk.Button(window, text=text, bg=color, fg=fg, command=command, font=('Arial', 16), width=20, height=2)

def get_img_label(window):
    label = tk.Label(window)
    return label

def get_entry_text(window):
    text = tk.Text(window, height=1, width=20, font=('Arial', 16))
    return text

def get_text_label(window, text):
    label = tk.Label(window, text=text, font=('Arial', 16))
    return label

def msg_box(title, message):
    messagebox.showinfo(title, message)

def recognize(image, db_dir):
    encodings = face_recognition.face_encodings(image)
    if not encodings:
        return 'no_persons_found'
    encoding = encodings[0]
    for file in os.listdir(db_dir):
        if file.endswith('.pickle'):
            with open(os.path.join(db_dir, file), 'rb') as f:
                db_encoding = pickle.load(f)
                match = face_recognition.compare_faces([db_encoding], encoding)[0]
                if match:
                    return file.replace('.pickle', '')
    return 'unknown_person'
