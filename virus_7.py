#!/usr/bin/env python3
"""
# Virus_7 Spooky Pop-Up Phantom
# Part of A Collection of 20 Halloween Inspired Pranks
"""
import tkinter as tk
import random
import time
import threading
import sys
from pynput import keyboard
import winsound
import ctypes
import os

running = True

messages = ["You're not alone", "Boo!", "Watch out", "Skull awaits"]

# Create pop-up windows
def create_popup():
    while running:
        time.sleep(random.uniform(5, 20))
        root = tk.Toplevel()
        root.attributes('-topmost', True)
        root.overrideredirect(True)
        screen_width = tk.Tk().winfo_screenwidth()
        screen_height = tk.Tk().winfo_screenheight()
        x = random.randint(0, screen_width - 200)
        y = random.randint(0, screen_height - 100)
        root.geometry(f"200x100+{x}+{y}")
        label = tk.Label(root, text=random.choice(messages), fg='red', bg='black', font=('Arial', 14))
        label.pack(expand=True, fill='both')
        # Glitchy border
        root.config(highlightbackground='white', highlightcolor='white', highlightthickness=2)
        # Flicker effect
        for i in range(5):
            root.attributes('-alpha', 0.5 if i % 2 == 0 else 1.0)
            root.update()
            time.sleep(0.1)
        # Melt effect: warp geometry downward
        for i in range(10):
            root.geometry(f"200x{100 - i*5}+{x}+{y + i*5}")
            root.update()
            time.sleep(0.05)
        root.destroy()
        winsound.Beep(800, 200)  # Ghostly wail

# Play ghostly wail sound
def play_wail():
    while running:
        time.sleep(random.uniform(10, 30))
        winsound.Beep(800 + random.randint(-200, 200), 300)

# Key combo for removal (Alt+F4 three times)
press_count = 0
def on_press(key):
    global press_count
    try:
        if key == keyboard.Key.alt and keyboard.Key.f4 in listener.pressed_keys:
            press_count += 1
            if press_count >= 3:
                global running
                running = False
                listener.stop()
                sys.exit(0)
        else:
            press_count = 0
    except AttributeError:
        press_count = 0

listener = keyboard.Listener(on_press=on_press)
listener.pressed_keys = set()
def on_release(key):
    try:
        listener.pressed_keys.remove(key)
    except KeyError:
        pass
listener.on_release = on_release

# Create desktop shortcut BanishPopups.exe
shell = win32com.client.Dispatch("WScript.Shell")
desktop = shell.SpecialFolders("Desktop")
shortcut_path = os.path.join(desktop, "BanishPopups.lnk")
shortcut = shell.CreateShortCut(shortcut_path)
shortcut.Targetpath = sys.executable
shortcut.Arguments = '-c "import os; os._exit(0)"'
shortcut.save()

listener.start()
t1 = threading.Thread(target=create_popup)
t2 = threading.Thread(target=play_wail)
t1.start()
t2.start()
listener.join()
