#!/usr/bin/env python3
"""
# Virus_16 Skull Screensaver
# Part of A Collection of 20 Halloween Inspired Pranks
"""
import tkinter as tk
import ctypes
import random
import time
import threading
import sys
import winsound
import os
from PIL import Image, ImageDraw, ImageTk
import win32gui
import win32con
import win32api

running = True

# Create skull image
def create_skull_image():
    size = (100, 100)
    image = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.ellipse((20, 10, 80, 70), fill=(255, 255, 255, 128))
    draw.ellipse((30, 25, 40, 35), fill=(0, 0, 0, 255))
    draw.ellipse((60, 25, 70, 35), fill=(0, 0, 0, 255))
    draw.polygon((50, 40, 45, 50, 55, 50), fill=(0, 0, 0, 255))
    image.save("skull_screensaver.png")
    return Image.open("skull_screensaver.png")

skull_image = create_skull_image()

# Create screensaver window
root = tk.Tk()
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
root.overrideredirect(True)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")
canvas = tk.Canvas(root, bg='black', highlightthickness=0)
canvas.pack(fill='both', expand=True)
hwnd = root.winfo_id()
styles = ctypes.windll.user32.GetWindowLongW(hwnd, -20)
ctypes.windll.user32.SetWindowLongW(hwnd, -20, styles | 0x00080000 | 0x00000020)

# Screensaver effect with floating skulls and fog
def screensaver_effect():
    tk_img = ImageTk.PhotoImage(skull_image)
    skulls = []
    for _ in range(10):
        skulls.append({
            'x': random.randint(0, screen_width),
            'y': random.randint(0, screen_height),
            'dx': random.uniform(-2, 2),
            'dy': random.uniform(-2, 2)
        })
    while running:
        canvas.delete('all')
        # Fog effect (semi-transparent rectangles)
        for _ in range(5):
            canvas.create_rectangle(
                random.randint(0, screen_width), random.randint(0, screen_height),
                random.randint(0, screen_width), random.randint(0, screen_height),
                fill='gray', stipple='gray50', outline=''
            )
        # Floating skulls
        for skull in skulls:
            canvas.create_image(skull['x'], skull['y'], image=tk_img)
            skull['x'] += skull['dx']
            skull['y'] += skull['dy']
            if skull['x'] < 0 or skull['x'] > screen_width:
                skull['dx'] = -skull['dx']
            if skull['y'] < 0 or skull['y'] > screen_height:
                skull['dy'] = -skull['dy']
            # Glitch effect
            if random.random() < 0.2:
                canvas.create_line(
                    skull['x'], skull['y'],
                    skull['x'] + random.randint(-50, 50), skull['y'] + random.randint(-50, 50),
                    fill='white'
                )
            # Melting effect
            if random.random() < 0.1:
                canvas.create_line(
                    skull['x'], skull['y'],
                    skull['x'], skull['y'] + random.randint(20, 50),
                    fill='green', width=2
                )
        canvas.image = tk_img
        root.update()
        time.sleep(0.1)
        time.sleep(random.uniform(5, 15))  # Activate randomly

# Play ghostly whispers
def play_whispers():
    while running:
        time.sleep(random.uniform(10, 30))
        winsound.Beep(300 + random.randint(-100, 100), 400)

# Esc key press detection (twice)
press_count = 0
last_press_time = 0
def on_press(key):
    global press_count, last_press_time
    try:
        if key == keyboard.Key.esc:
            current_time = time.time()
            if current_time - last_press_time < 1:
                press_count += 1
            else:
                press_count = 1
            last_press_time = current_time
            if press_count >= 2:
                global running
                running = False
                root.destroy()
                sys.exit(0)
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

# Create BanishScreensaver.exe
shell = win32com.client.Dispatch("WScript.Shell")
desktop = shell.SpecialFolders("Desktop")
shortcut_path = os.path.join(desktop, "BanishScreensaver.lnk")
shortcut = shell.CreateShortCut(shortcut_path)
shortcut.Targetpath = sys.executable
shortcut.Arguments = '-c "import os; os._exit(0)"'
shortcut.save()

t1 = threading.Thread(target=screensaver_effect)
t2 = threading.Thread(target=play_whispers)
t1.start()
t2.start()
listener.join()
t1.join()
t2.join()
