#!/usr/bin/env python3
"""
# Virus_19 Spooky Sound Saboteur
# Part of A Collection of 20 Halloween Inspired Pranks
"""
import winsound
import random
import time
import threading
import sys
import os
import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
import ctypes
import win32gui
import win32con
import win32api
from pynput import keyboard

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
    image.save("skull_sound.png")
    return Image.open("skull_sound.png")

skull_image = create_skull_image()

# Overlay for skull flash
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

# Play creepy sounds
def play_creepy_sounds():
    sounds = [
        (300, 400, "whisper"),  # Whisper
        (1000, 300, "scream"),  # Scream
        (600, 200, "cackle")    # Cackle
    ]
    tk_img = ImageTk.PhotoImage(skull_image)
    while running:
        time.sleep(random.uniform(10, 30))
        freq, duration, _ = random.choice(sounds)
        winsound.Beep(freq + random.randint(-100, 100), duration)
        # Flash skull
        canvas.create_image(random.randint(100, screen_width-100), random.randint(100, screen_height-100), image=tk_img)
        canvas.image = tk_img
        root.update()
        time.sleep(0.2)
        canvas.delete('all')
        # Fluctuate volume
        current_volume = ctypes.windll.winmm.waveOutGetVolume(0, None) & 0xFFFF
        new_volume = current_volume + random.randint(-1000, 1000)
        new_volume = max(0, min(0xFFFF, new_volume))
        ctypes.windll.winmm.waveOutSetVolume(0, new_volume)
        time.sleep(1)
        ctypes.windll.winmm.waveOutSetVolume(0, current_volume)  # Restore volume

# Monitor mute/unmute for removal
def monitor_volume():
    def low_level_keyboard_proc(nCode, wParam, lParam):
        if wParam == win32con.WM_KEYDOWN and running:
            vk_code = lParam >> 16 & 0xFFFF
            if vk_code == win32con.VK_VOLUME_MUTE:
                global running
                running = False
                root.destroy()
                sys.exit(0)
        return win32gui.CallNextHookEx(None, nCode, wParam, lParam)

    keyboard_hook = win32api.SetWindowsHookEx(win32con.WH_KEYBOARD_LL, low_level_keyboard_proc, None, 0)
    win32gui.PumpMessages()
    win32api.UnhookWindowsHookEx(keyboard_hook)

# Create SilenceGhost.bat
shell = win32com.client.Dispatch("WScript.Shell")
desktop = shell.SpecialFolders("Desktop")
shortcut_path = os.path.join(desktop, "SilenceGhost.lnk")
shortcut = shell.CreateShortCut(shortcut_path)
shortcut.Targetpath = sys.executable
shortcut.Arguments = '-c "import os; os._exit(0)"'
shortcut.save()

t1 = threading.Thread(target=play_creepy_sounds)
t2 = threading.Thread(target=monitor_volume)
t1.start()
t2.start()
t1.join()
t2.join()
