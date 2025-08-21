#!/usr/bin/env python3
"""
# Virus_10 Cursed Clock
# Part of A Collection of 20 Halloween Inspired Pranks
"""
import tkinter as tk
import ctypes
import random
import time
import threading
import sys
import winsound
from datetime import datetime
import win32gui
import win32con
from pynput import keyboard
import os
from PIL import Image, ImageDraw, ImageTk

running = True

# Messages for clock
messages = ["Time's up", "You're late", "Eternal night", "Skull time"]

# Create skull image for clock
def create_skull_image():
    size = (50, 50)
    image = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.ellipse((10, 5, 40, 35), fill=(255, 255, 255, 128))
    draw.ellipse((15, 12, 20, 17), fill=(0, 0, 0, 255))
    draw.ellipse((30, 12, 35, 17), fill=(0, 0, 0, 255))
    draw.polygon((25, 20, 22, 25, 28, 25), fill=(0, 0, 0, 255))
    image.save("skull_clock.png")
    return Image.open("skull_clock.png")

skull_image = create_skull_image()

# Create overlay window at clock position
def get_clock_position():
    hwnd = win32gui.FindWindow("Shell_TrayWnd", None)
    tray_rect = win32gui.GetWindowRect(hwnd)
    clock_hwnd = win32gui.FindWindowEx(hwnd, None, "TrayClockWClass", None)
    if clock_hwnd:
        rect = win32gui.GetWindowRect(clock_hwnd)
        return rect[0], rect[1], rect[2] - rect[0], rect[3] - rect[1]
    return tray_rect[2] - 100, tray_rect[3] - 50, 100, 50  # Fallback

clock_x, clock_y, clock_w, clock_h = get_clock_position()

root = tk.Tk()
root.attributes('-alpha', 0.8)
root.attributes('-topmost', True)
root.overrideredirect(True)
root.geometry(f"{clock_w}x{clock_h}+{clock_x}+{clock_y}")
canvas = tk.Canvas(root, bg='black', highlightthickness=0)
canvas.pack(fill='both', expand=True)
root.attributes('-transparentcolor', 'black')
hwnd = root.winfo_id()
styles = ctypes.windll.user32.GetWindowLongW(hwnd, -20)
ctypes.windll.user32.SetWindowLongW(hwnd, -20, styles | 0x00080000 | 0x00000020)

# Display creepy messages or countdown
def update_clock():
    tk_img = ImageTk.PhotoImage(skull_image)
    while running:
        canvas.delete('all')
        if random.random() < 0.3:
            # Show skull
            canvas.create_image(clock_w // 2, clock_h // 2, image=tk_img)
            canvas.image = tk_img
        elif random.random() < 0.5:
            # Show message
            message = random.choice(messages)
            canvas.create_text(clock_w // 2, clock_h // 2, text=message, fill='red', font=('Arial', 12))
            # Glitch effect
            for _ in range(10):
                x = random.randint(0, clock_w)
                y = random.randint(0, clock_h)
                canvas.create_line(x, y, x + random.randint(-10, 10), y + random.randint(-10, 10), fill='white')
        else:
            # Countdown to midnight
            now = datetime.now()
            midnight = datetime(now.year, now.month, now.day, 23, 59, 59)
            delta = midnight - now
            countdown = f"{delta.seconds // 3600}:{(delta.seconds % 3600) // 60:02d}:{delta.seconds % 60:02d}"
            canvas.create_text(clock_w // 2, clock_h // 2, text=countdown, fill='red', font=('Arial', 12))
        root.update()
        time.sleep(2)
        canvas.delete('all')
        root.update()
        time.sleep(random.uniform(5, 15))

# Play ticking sound
def play_ticking():
    while running:
        time.sleep(random.uniform(10, 30))
        for _ in range(5):
            winsound.Beep(600, 100)
            time.sleep(0.2)

# Double-click clock for removal
def monitor_double_click():
    def low_level_mouse_proc(nCode, wParam, lParam):
        if wParam == win32con.WM_LBUTTONDBLCLK and running:
            point = win32gui.GetCursorPos()
            if clock_x <= point[0] <= clock_x + clock_w and clock_y <= point[1] <= clock_y + clock_h:
                # Show removal prompt
                prompt = tk.Toplevel()
                prompt.attributes('-topmost', True)
                prompt.geometry(f"200x100+{clock_x}+{clock_y}")
                tk.Label(prompt, text="Select to reset clock").pack()
                tk.Button(prompt, text="Reset Time", command=lambda: [setattr(sys, 'running', False), root.destroy(), prompt.destroy(), sys.exit(0)]).pack()
        return win32gui.CallNextHookEx(None, nCode, wParam, lParam)

    mouse_hook = win32api.SetWindowsHookEx(win32con.WH_MOUSE_LL, low_level_mouse_proc, None, 0)
    win32gui.PumpMessages()
    win32api.UnhookWindowsHookEx(mouse_hook)

t1 = threading.Thread(target=update_clock)
t2 = threading.Thread(target=play_ticking)
t3 = threading.Thread(target=monitor_double_click)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
