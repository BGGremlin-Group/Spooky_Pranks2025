#!/usr/bin/env python3
"""
# Virus_9 Flickering Fear
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
from PIL import Image, ImageDraw, ImageTk
import os

running = True

# Create overlay window for flicker
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

# Create skull image
def create_skull_image():
    size = (100, 100)
    image = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.ellipse((20, 10, 80, 70), fill=(255, 255, 255, 128))
    draw.ellipse((30, 25, 40, 35), fill=(0, 0, 0, 255))
    draw.ellipse((60, 25, 70, 35), fill=(0, 0, 0, 255))
    draw.polygon((50, 40, 45, 50, 55, 50), fill=(0, 0, 0, 255))
    image.save("skull.png")
    return Image.open("skull.png")

skull_image = create_skull_image()

# Flicker effect with skulls and glitches
def flicker_screen():
    while running:
        canvas.delete('all')
        # Static effect
        for _ in range(200):
            x1 = random.randint(0, screen_width)
            y1 = random.randint(0, screen_height)
            x2 = x1 + random.randint(-50, 50)
            y2 = y1 + random.randint(-50, 50)
            color = '#%06x' % random.randint(0, 0xFFFFFF)
            canvas.create_line(x1, y1, x2, y2, fill=color, width=2)
        # Random skull or shadowy figure
        if random.random() < 0.4:
            tk_img = ImageTk.PhotoImage(skull_image)
            canvas.create_image(random.randint(100, screen_width-100), random.randint(100, screen_height-100), image=tk_img)
            canvas.image = tk_img  # Keep reference
        else:
            # Shadowy figure (rectangle)
            canvas.create_rectangle(random.randint(100, screen_width-100), random.randint(100, screen_height-100),
                                   random.randint(100, screen_width-100)+50, random.randint(100, screen_height-100)+100,
                                   fill='black', outline='gray')
        # Melting effect: warp canvas
        for i in range(5):
            canvas.scale('all', screen_width//2, screen_height//2, 1, 1 - i*0.02)
            root.update()
            time.sleep(0.05)
        canvas.scale('all', screen_width//2, screen_height//2, 1, 1.1)  # Reset
        root.update()
        time.sleep(0.2)
        canvas.delete('all')
        time.sleep(random.uniform(5, 15))

# Play pulsing sound
def play_pulse():
    while running:
        time.sleep(random.uniform(10, 30))
        for freq in range(200, 300, 10):
            winsound.Beep(freq, 100)
            time.sleep(0.05)

# Key combo for removal
def on_press(key):
    try:
        if keyboard.Key.ctrl in listener.pressed_keys and keyboard.Key.alt in listener.pressed_keys and key.char.lower() == 'l':
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

# Create hidden StabilizeScreen.bat
with open("StabilizeScreen.bat", "w") as f:
    f.write("@echo off\npython -c \"import sys; sys.exit(0)\"")

listener.start()
t1 = threading.Thread(target=flicker_screen)
t2 = threading.Thread(target=play_pulse)
t1.start()
t2.start()
listener.join()
