#!/usr/bin/env python3
"""
# Virus_1 Creepy Cursor Crawler
# Part of A Collection of 20 Halloween Inspired Pranks
"""
import ctypes
from ctypes import windll, c_int, c_char_p
import win32con
import random
import time
import threading
import sys
import os
import win32com.client
from pynput import keyboard
import pyautogui
import winsound
from PIL import Image, ImageDraw

running = True

def create_skull_cursor_file():
    size = (32, 32)
    image = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    # Head
    draw.ellipse((8, 4, 24, 20), fill=(255, 255, 255, 255))
    # Jaw
    draw.rectangle((10, 20, 22, 28), fill=(255, 255, 255, 255))
    # Eyes
    draw.ellipse((11, 8, 15, 12), fill=(0, 0, 0, 255))
    draw.ellipse((17, 8, 21, 12), fill=(0, 0, 0, 255))
    # Nose
    draw.polygon((16, 14, 14, 18, 18, 18), fill=(0, 0, 0, 255))
    # Mouth
    draw.line((11, 23, 21, 23), fill=(0, 0, 0, 255), width=1)
    draw.line((13, 25, 15, 25), fill=(0, 0, 0, 255), width=1)
    draw.line((17, 25, 19, 25), fill=(0, 0, 0, 255), width=1)
    image.save("skull.ico", format="ICO")
    return "skull.ico"

path = create_skull_cursor_file()

LoadCursorFromFile = windll.user32.LoadCursorFromFileA
LoadCursorFromFile.restype = c_int
LoadCursorFromFile.argtypes = [c_char_p]

SetSystemCursor = windll.user32.SetSystemCursor
SetSystemCursor.restype = c_int
SetSystemCursor.argtypes = [c_int, c_int]

original_cursor = windll.user32.CopyImage(windll.user32.LoadCursorA(0, win32con.IDC_ARROW), win32con.IMAGE_CURSOR, 0, 0, win32con.LR_COPYFROMRESOURCE)

def set_to_skull():
    new_cursor = LoadCursorFromFile(path.encode('ansi'))
    SetSystemCursor(new_cursor, win32con.IDC_ARROW)

def restore_cursor():
    SetSystemCursor(original_cursor, win32con.IDC_ARROW)

def play_giggle():
    for i in range(5):
        winsound.Beep(1000 + random.randint(0, 500), 50)
        time.sleep(0.05)

def twitch_cursor():
    while running:
        pyautogui.moveRel(random.randint(-5, 5), random.randint(-5, 5), duration=0.1)
        time.sleep(random.uniform(0.5, 2))
        if random.random() < 0.1:
            edge = random.choice(['left', 'top', 'right', 'bottom'])
            screen_width, screen_height = pyautogui.size()
            if edge == 'left':
                pyautogui.moveTo(0, random.randint(0, screen_height), duration=0.5)
            elif edge == 'top':
                pyautogui.moveTo(random.randint(0, screen_width), 0, duration=0.5)
            elif edge == 'right':
                pyautogui.moveTo(screen_width - 1, random.randint(0, screen_height), duration=0.5)
            elif edge == 'bottom':
                pyautogui.moveTo(random.randint(0, screen_width), screen_height - 1, duration=0.5)
            time.sleep(1)
        if random.random() < 0.05:
            start_x, start_y = pyautogui.position()
            scale = 50
            # H
            pyautogui.moveTo(start_x, start_y, duration=0.5)
            pyautogui.moveRel(0, scale, duration=0.5)
            pyautogui.moveRel(0, -scale, duration=0.5)
            pyautogui.moveRel(scale, 0, duration=0.5)
            pyautogui.moveRel(0, scale, duration=0.5)
            pyautogui.moveRel(0, -scale / 2, duration=0.5)
            pyautogui.moveRel(-scale, 0, duration=0.5)
            # E
            start_x += scale + 10
            pyautogui.moveTo(start_x, start_y, duration=0.5)
            pyautogui.moveRel(scale, 0, duration=0.5)
            pyautogui.moveRel(0, scale / 2, duration=0.5)
            pyautogui.moveRel(-scale, 0, duration=0.5)
            pyautogui.moveRel(0, scale / 2, duration=0.5)
            pyautogui.moveRel(scale, 0, duration=0.5)
            pyautogui.moveRel(0, -scale, duration=0.5)
            pyautogui.moveRel(-scale, 0, duration=0.5)
            # L
            start_x += scale + 10
            pyautogui.moveTo(start_x, start_y, duration=0.5)
            pyautogui.moveRel(scale, 0, duration=0.5)
            pyautogui.moveRel(0, scale, duration=0.5)
            pyautogui.moveRel(-scale, 0, duration=0.5)
            pyautogui.moveRel(0, -scale, duration=0.5)
            # P
            start_x += scale + 10
            pyautogui.moveTo(start_x, start_y, duration=0.5)
            pyautogui.moveRel(0, scale, duration=0.5)
            pyautogui.moveRel(scale, 0, duration=0.5)
            pyautogui.moveRel(0, -scale / 2, duration=0.5)
            pyautogui.moveRel(-scale, 0, duration=0.5)
            time.sleep(1)

def flicker_skull():
    while running:
        time.sleep(random.uniform(5, 10))
        set_to_skull()
        time.sleep(0.5)
        restore_cursor()
        for i in range(3):
            set_to_skull()
            time.sleep(0.1)
            restore_cursor()
            time.sleep(0.1)

def random_sound():
    while running:
        time.sleep(random.uniform(10, 30))
        play_giggle()

def on_press(key):
    if running:
        if key == keyboard.Key.ctrl and key == keyboard.Key.alt and hasattr(key, 'char') and key.char == 'b':
            global running
            running = False
            restore_cursor()
            listener.stop()
            sys.exit(0)

listener = keyboard.Listener(on_press=on_press)
listener.start()

# Create shortcut
shell = win32com.client.Dispatch("WScript.Shell")
desktop = shell.SpecialFolders("Desktop")
shortcut_path = os.path.join(desktop, "Exorcism.lnk")
shortcut = shell.CreateShortCut(shortcut_path)
shortcut.Targetpath = sys.executable
shortcut.Arguments = '-c "import os; os._exit(0)"'  # Rough way to exit
shortcut.save()

t1 = threading.Thread(target=twitch_cursor)
t2 = threading.Thread(target=flicker_skull)
t3 = threading.Thread(target=random_sound)
t1.start()
t2.start()
t3.start()
listener.join()
