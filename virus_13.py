#!/usr/bin/env python3
"""
# Virus_13 Eerie Error Messages
# Part of A Collection of 20 Halloween Inspired Pranks
"""
import tkinter as tk
import random
import time
import threading
import sys
import winsound
import ctypes
import os
from PIL import Image, ImageDraw, ImageTk

running = True

# Error message texts
error_messages = ["System Haunted", "Skull Overload", "Ghost in the Shell", "Error: Boo!"]

# Create skull image
def create_skull_image():
    size = (50, 50)
    image = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.ellipse((10, 5, 40, 35), fill=(255, 255, 255, 128))
    draw.ellipse((15, 12, 20, 17), fill=(0, 0, 0, 255))
    draw.ellipse((30, 12, 35, 17), fill=(0, 0, 0, 255))
    draw.polygon((25, 20, 22, 25, 28, 25), fill=(0, 0, 0, 255))
    image.save("skull_error.png")
    return Image.open("skull_error.png")

skull_image = create_skull_image()

# Create error pop-ups
def show_error_popups():
    tk_img = ImageTk.PhotoImage(skull_image)
    while running:
        time.sleep(random.uniform(5, 20))
        popup = tk.Toplevel()
        popup.attributes('-topmost', True)
        popup.overrideredirect(True)
        screen_width = tk.Tk().winfo_screenwidth()
        screen_height = tk.Tk().winfo_screenheight()
        x = random.randint(0, screen_width - 300)
        y = random.randint(0, screen_height - 150)
        popup.geometry(f"300x150+{x}+{y}")
        # Glitchy text and border
        canvas = tk.Canvas(popup, bg='black', highlightthickness=2, highlightbackground='white')
        canvas.pack(fill='both', expand=True)
        canvas.create_text(150, 50, text=random.choice(error_messages), fill='red', font=('Arial', 14))
        # Add skull
        if random.random() < 0.5:
            canvas.create_image(150, 100, image=tk_img)
            canvas.image = tk_img
        # Glitch effect: random lines
        for _ in range(20):
            x1 = random.randint(0, 300)
            y1 = random.randint(0, 150)
            x2 = x1 + random.randint(-20, 20)
            y2 = y1 + random.randint(-20, 20)
            canvas.create_line(x1, y1, x2, y2, fill='white')
        # Melting border effect
        for i in range(10):
            popup.geometry(f"300x{150 - i*5}+{x}+{y + i*5}")
            popup.update()
            time.sleep(0.05)
        # Add dismissal button
        btn = tk.Button(popup, text="Dismiss Spirit", command=lambda: [setattr(sys, 'running', False), popup.destroy(), sys.exit(0)])
        btn.place(x=100, y=120)
        popup.update()
        time.sleep(3)
        if running:
            popup.destroy()

# Play distant scream
def play_scream():
    while running:
        time.sleep(random.uniform(10, 30))
        winsound.Beep(1000 + random.randint(-200, 200), 300)

# Create hidden ErrorGhoul.exe
shell = win32com.client.Dispatch("WScript.Shell")
desktop = shell.SpecialFolders("Desktop")
shortcut_path = os.path.join(desktop, "ErrorGhoul.lnk")
shortcut = shell.CreateShortCut(shortcut_path)
shortcut.Targetpath = sys.executable
shortcut.Arguments = '-c "import os; os._exit(0)"'
shortcut.save()

t1 = threading.Thread(target=show_error_popups)
t2 = threading.Thread(target=play_scream)
t1.start()
t2.start()
t1.join()
t2.join()
