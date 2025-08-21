#!/usr/bin/env python3
"""
# Virus_12 Melting Menu Madness
# Part of A Collection of 20 Halloween Inspired Pranks
"""
import pythoncom
import win32com.client as wcomcli
from win32com.shell import shell, shellcon
import win32gui
import win32con
import win32api
import random
import time
import threading
import sys
import os
import winsound
from PIL import Image, ImageDraw, ImageTk
import tkinter as tk
import ctypes

running = True

# Get Start menu items (simplified, as direct manipulation is complex)
start_menu_path = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs")
original_items = {}
for root, _, files in os.walk(start_menu_path):
    for file in files:
        if file.endswith(".lnk"):
            full_path = os.path.join(root, file)
            original_items[full_path] = file

# Create skull icon
def create_skull_icon():
    size = (32, 32)
    image = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.ellipse((8, 4, 24, 20), fill=(255, 255, 255, 255))
    draw.rectangle((10, 20, 22, 28), fill=(255, 255, 255, 255))
    draw.ellipse((11, 8, 15, 12), fill=(0, 0, 0, 255))
    draw.ellipse((17, 8, 21, 12), fill=(0, 0, 0, 255))
    draw.polygon((16, 14, 14, 18, 18, 18), fill=(0, 0, 0, 255))
    image.save("skull_menu.ico")
    return os.path.abspath("skull_menu.ico")

skull_icon_path = create_skull_icon()

# Overlay for Start menu
root = tk.Tk()
root.attributes('-alpha', 0.5)
root.attributes('-topmost', True)
root.overrideredirect(True)
screen_width = root.winfo_screenwidth()
menu_width, menu_height = 300, 400
root.geometry(f"{menu_width}x{menu_height}+0+{root.winfo_screenheight()-menu_height}")
canvas = tk.Canvas(root, bg='black', highlightthickness=0)
canvas.pack(fill='both', expand=True)
root.attributes('-transparentcolor', 'black')
hwnd = root.winfo_id()
styles = ctypes.windll.user32.GetWindowLongW(hwnd, -20)
ctypes.windll.user32.SetWindowLongW(hwnd, -20, styles | 0x00080000 | 0x00000020)

# Skull pattern positions
skull_points = [
    (100, 50), (200, 50), (150, 100),
    (120, 150), (180, 150),
    (100, 200), (200, 200)
]

# Rearrange and rename menu items
def rearrange_menu():
    creepy_names = ["Fear", "Doom", "Terror", "Skull"]
    while running:
        for path in original_items:
            new_name = f"{random.choice(creepy_names)}.lnk"
            try:
                os.rename(path, os.path.join(os.path.dirname(path), new_name))
            except:
                pass
        time.sleep(5)
        # Restore names
        for path, name in original_items.items():
            try:
                os.rename(os.path.join(os.path.dirname(path), os.path.basename(path)), path)
            except:
                pass
        time.sleep(random.uniform(10, 30))

# Display skull pattern and melting effect
def display_skull_pattern():
    tk_img = ImageTk.PhotoImage(Image.open(skull_icon_path))
    while running:
        canvas.delete('all')
        for x, y in skull_points:
            canvas.create_image(x, y, image=tk_img)
            canvas.image = tk_img
            # Melting effect
            canvas.create_line(x, y, x, y + random.randint(20, 50), fill='green', width=2)
        root.update()
        time.sleep(0.5)
        canvas.delete('all')
        time.sleep(random.uniform(5, 15))
        # Show input box occasionally
        if random.random() < 0.2:
            entry = tk.Entry(root)
            entry.place(x=50, y=menu_height-30, width=200)
            def check(event):
                if entry.get().upper() == "RESTORE":
                    global running
                    running = False
                    root.destroy()
                    sys.exit(0)
            entry.bind("<Return>", check)
            root.update()
            time.sleep(5)
            entry.destroy()

# Play growl sound
def play_growl():
    while running:
        time.sleep(random.uniform(10, 30))
        winsound.Beep(200 + random.randint(-50, 50), 500)

# Create hidden MenuFix.bat
with open("MenuFix.bat", "w") as f:
    f.write("@echo off\npython -c \"import sys; sys.exit(0)\"")

t1 = threading.Thread(target=rearrange_menu)
t2 = threading.Thread(target=display_skull_pattern)
t3 = threading.Thread(target=play_growl)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
