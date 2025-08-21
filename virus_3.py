#!/usr/bin/env python3
"""
# Virus_3 Phantom Typist
# Part of A Collection of 20 Halloween Inspired Pranks
"""
import random
import time
import threading
import sys
from pynput import keyboard
import pyautogui
import winsound
import tkinter as tk
import ctypes

running = True

phrases = ["I'm watching you", "Get out", "Help me", "Behind you"]

def insert_phrases():
    while running:
        time.sleep(random.uniform(5, 15))
        phrase = random.choice(phrases)
        pyautogui.typewrite(phrase)
        time.sleep(0.5)

def play_typing_sound():
    while running:
        time.sleep(random.uniform(5, 15))
        for _ in range(10):
            winsound.Beep(600, 50)
            time.sleep(0.1)

def flash_skull():
    root = tk.Tk()
    root.attributes('-alpha', 0.3)
    root.attributes('-topmost', True)
    root.overrideredirect(True)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")
    canvas = tk.Canvas(root, bg='black')
    canvas.pack(fill='both', expand=True)
    root.attributes('-transparentcolor', 'black')
    canvas.config(bg='black')
    hwnd = root.winfo_id()
    styles = ctypes.windll.user32.GetWindowLongW(hwnd, -20)
    ctypes.windll.user32.SetWindowLongW(hwnd, -20, styles | 0x00080000 | 0x00000020)
    root.update()

    while running:
        time.sleep(random.uniform(5, 15))
        # Flash skull
        image = Image.new("RGBA", (100, 100), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        draw.ellipse((20, 10, 80, 70), fill=(255, 255, 255, 100))
        # Eyes, etc.
        tk_image = ImageTk.PhotoImage(image)
        canvas.create_image(screen_width - 150, screen_height - 150, image=tk_image)
        root.update()
        time.sleep(0.2)
        canvas.delete('all')
        root.update()

def on_press(key):
    if running:
        if key == keyboard.Key.ctrl and key == keyboard.Key.alt and hasattr(key, 'char') and key.char == 'b':
            global running
            running = False
            listener.stop()
            sys.exit(0)

listener = keyboard.Listener(on_press=on_press)
listener.start()

t1 = threading.Thread(target=insert_phrases)
t2 = threading.Thread(target=play_typing_sound)
t3 = threading.Thread(target=flash_skull)
t1.start()
t2.start()
t3.start()
listener.join()
