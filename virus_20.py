#!/usr/bin/env python3
"""
# Virus_20 Phantom Window Wobble
# Part of A Collection of 20 Halloween Inspired Pranks
"""
import win32gui
import win32con
import win32api
import random
import time
import threading
import sys
import winsound
import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
import ctypes
import os

running = True

# Create skull image
def create_skull_image():
    size = (50, 50)
    image = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.ellipse((10, 5, 40, 35), fill=(255, 255, 255, 128))
    draw.ellipse((15, 12, 20, 17), fill=(0, 0, 0, 255))
    draw.ellipse((30, 12, 35, 17), fill=(0, 0, 0, 255))
    draw.polygon((25, 20, 22, 25, 28, 25), fill=(0, 0, 0, 255))
    image.save("skull_window.png")
    return Image.open("skull_window.png")

skull_image = create_skull_image()

# Overlay for skulls
root = tk.Tk()
root.attributes('-alpha', 0.5)
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
ctypes.windll.user32.SetWindowLongW(hwnd, -20, styles | 0x00080000 | 0x00000020)

# Wobble windows and add effects
def wobble_windows():
    tk_img = ImageTk.PhotoImage(skull_image)
    while running:
        def callback(hwnd, _):
            if win32gui.IsWindowVisible(hwnd) and hwnd != root.winfo_id():
                l, t, r, b = win32gui.GetWindowRect(hwnd)
                # Wobble
                for i in range(5):
                    offset = random.randint(-5, 5)
                    win32gui.SetWindowPos(hwnd, 0, l + offset, t + offset, r - l, b - t, win32con.SWP_NOZORDER)
                    # Show skull in distorted areas
                    canvas.create_image(l + (r - l) // 2, t + (b - t) // 2, image=tk_img)
                    canvas.image = tk_img
                    # Melting effect
                    canvas.create_line(l + (r - l) // 2, b, l + (r - l) // 2, b + random.randint(20, 50), fill='green', width=2)
                    root.update()
                    time.sleep(0.05)
                win32gui.SetWindowPos(hwnd, 0, l, t, r - l, b - t, win32con.SWP_NOZORDER)
                canvas.delete('all')
        win32gui.EnumWindows(callback, None)
        time.sleep(random.uniform(5, 15))

# Play eerie chant
def play_chant():
    while running:
        time.sleep(random.uniform(10, 30))
        for freq in range(200, 400, 20):
            winsound.Beep(freq, 100)
            time.sleep(0.05)

# Key combo for removal (Ctrl + Alt + Steady)
def on_press(key):
    try:
        if keyboard.Key.ctrl in listener.pressed_keys and keyboard.Key.alt in listener.pressed_keys and key.char.lower() == 's':
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

# Create WindowFix.exe
shell = win32com.client.Dispatch("WScript.Shell")
desktop = shell.SpecialFolders("Desktop")
shortcut_path = os.path.join(desktop, "WindowFix.lnk")
shortcut = shell.CreateShortCut(shortcut_path)
shortcut.Targetpath = sys.executable
shortcut.Arguments = '-c "import os; os._exit(0)"'
shortcut.save()

listener.start()
t1 = threading.Thread(target=wobble_windows)
t2 = threading.Thread(target=play_chant)
t1.start()
t2.start()
listener.join()
t1.join()
t2.join()
