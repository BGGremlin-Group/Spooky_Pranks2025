#!/usr/bin/env python3
"""
# Virus_5 Glitchy Ghost
# Part of A Collection of 20 Halloween Inspired Pranks
"""
import tkinter as tk
import ctypes
import random
import time
import threading
import sys
from pynput import keyboard
import winsound
from PIL import ImageTk

running = True

# Create overlay window for glitches
root = tk.Tk()
root.attributes('-alpha', 0.3)
root.attributes('-topmost', True)
root.overrideredirect(True)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")
canvas = tk.Canvas(root, bg='black', highlightthickness=0)
canvas.pack(fill='both', expand=True)
root.attributes('-transparentcolor', 'black')
hwnd = root.winfo_id()
styles = ctypes.windll.user32.GetWindowLongW(hwnd, -20)
ctypes.windll.user32.SetWindowLongW(hwnd, -20, styles | 0x00080000 | 0x00000020)  # Click-through

# Function to draw glitch effects
def draw_glitch():
    while running:
        canvas.delete('all')
        # Pixelated lines and color shifts
        for _ in range(100):
            x1 = random.randint(0, screen_width)
            y1 = random.randint(0, screen_height)
            x2 = x1 + random.randint(-100, 100)
            y2 = y1 + random.randint(-100, 100)
            color = '#%06x' % random.randint(0, 0xFFFFFF)
            width = random.randint(1, 5)
            canvas.create_line(x1, y1, x2, y2, fill=color, width=width)
        # Form skull shape occasionally
        if random.random() < 0.3:
            cx, cy = random.randint(100, screen_width-100), random.randint(100, screen_height-100)
            canvas.create_oval(cx-50, cy-50, cx+50, cy+50, fill='white', outline='red')
            canvas.create_oval(cx-20, cy-10, cx-10, cy, fill='black')
            canvas.create_oval(cx+10, cy-10, cx+20, cy, fill='black')
            canvas.create_polygon(cx-15, cy+10, cx, cy+30, cx+15, cy+10, fill='black')
        root.update()
        time.sleep(0.2)
        canvas.delete('all')
        time.sleep(random.uniform(3, 10))

# Play distorted moan
def play_moan():
    while running:
        time.sleep(random.uniform(10, 30))
        for freq in range(200, 100, -10):
            winsound.Beep(freq, 100)
            time.sleep(0.05)

# Key combo for removal
def on_press(key):
    try:
        if keyboard.Key.ctrl in listener.pressed_keys and keyboard.Key.shift in listener.pressed_keys and key.char.lower() == 'g':
            global running
            running = False
            root.destroy()
            sys.exit(0)
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.pressed_keys = set()
def on_release(key):
    try:
        listener.pressed_keys.remove(key)
    except KeyError:
        pass
listener.on_release = on_release

# Create hidden CleanseGlitch.bat
with open("CleanseGlitch.bat", "w") as f:
    f.write("@echo off\npython -c \"import sys; sys.exit(0)\"")

listener.start()

t1 = threading.Thread(target=draw_glitch)
t2 = threading.Thread(target=play_moan)
t1.start()
t2.start()
listener.join()
