#!/usr/bin/env python3
"""
# Virus_4 Haunted Wallpaper
# Part of A Collection of 20 Halloween Inspired Pranks
"""
import ctypes
import os
import random
import time
import threading
import sys
from PIL import Image, ImageDraw
from pynput import keyboard
import winsound
import win32gui
import win32con
import win32api

running = True

# Function to get current wallpaper
def get_current_wallpaper():
    SPI_GETDESKWALLPAPER = 0x0073
    buffer = ctypes.create_unicode_buffer(260)
    ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, 260, buffer, 0)
    return buffer.value

original_wallpaper = get_current_wallpaper()

# Function to set wallpaper
def set_wallpaper(path):
    ctypes.windll.user32.SystemParametersInfoW(win32con.SPI_SETDESKWALLPAPER, 0, path, win32con.SPIF_UPDATEINIFILE | win32con.SPIF_SENDWININICHANGE)

# Generate eerie images
def generate_eerie_image(index):
    size = (1920, 1080)  # Assuming common resolution; in real code, get actual screen size
    image = Image.new("RGB", size, (0, 0, 0))
    draw = ImageDraw.Draw(image)
    if index == 0:
        # Foggy graveyard
        draw.rectangle((0, size[1]//2, size[0], size[1]), fill=(50, 50, 50))
        draw.rectangle((400, 700, 500, 900), fill=(100, 100, 100))  # Tombstone
        draw.text((410, 750), "R.I.P.", fill=(0, 0, 0))
    elif index == 1:
        # Glowing eyes
        draw.ellipse((800, 400, 820, 420), fill=(255, 255, 0))
        draw.ellipse((900, 400, 920, 420), fill=(255, 255, 0))
    # Add skull overlay with transparency
    skull_image = Image.new("RGBA", (100, 100), (255, 255, 255, 128))
    skull_draw = ImageDraw.Draw(skull_image)
    skull_draw.ellipse((20, 10, 80, 70), fill=(255, 255, 255, 128))
    skull_draw.ellipse((30, 25, 40, 35), fill=(0, 0, 0, 255))
    skull_draw.ellipse((60, 25, 70, 35), fill=(0, 0, 0, 255))
    image.paste(skull_image, (random.randint(0, size[0]-100), random.randint(0, size[1]-100)), skull_image)
    # Add glitch effect: random lines
    for _ in range(50):
        x1, y1 = random.randint(0, size[0]), random.randint(0, size[1])
        x2, y2 = x1 + random.randint(-50, 50), y1 + random.randint(-50, 50)
        draw.line((x1, y1, x2, y2), fill=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    path = f"eerie_{index}.jpg"
    image.save(path)
    return path

# Cycle through wallpapers
def cycle_wallpapers():
    index = 0
    while running:
        path = generate_eerie_image(index)
        set_wallpaper(os.path.abspath(path))
        index = (index + 1) % 5  # Cycle through 5 variations
        time.sleep(10)  # Change every 10 seconds

# Play random whispers
def play_whispers():
    while running:
        time.sleep(random.uniform(15, 45))
        winsound.Beep(300 + random.randint(-100, 100), 500)

# Pulse screen edges (simple flash)
def pulse_edges():
    while running:
        time.sleep(random.uniform(5, 15))
        hwnd = win32gui.GetDesktopWindow()
        hdc = win32gui.GetWindowDC(hwnd)
        width = win32api.GetSystemMetrics(0)
        height = win32api.GetSystemMetrics(1)
        for i in range(5):
            win32gui.DrawEdge(hdc, (0, 0, width, height), win32con.EDGE_RAISED, win32con.BF_RECT)
            time.sleep(0.1)
            win32gui.DrawEdge(hdc, (0, 0, width, height), win32con.EDGE_SUNKEN, win32con.BF_RECT)
            time.sleep(0.1)
        win32gui.ReleaseDC(hwnd, hdc)

# Custom right-click menu for removal
class CustomMenu:
    def __init__(self):
        self.hmenu = win32gui.CreatePopupMenu()
        win32gui.AppendMenu(self.hmenu, win32con.MF_STRING, 1001, "Restore Original Wallpaper")

    def show(self, hwnd, x, y):
        win32gui.TrackPopupMenu(self.hmenu, win32con.TPM_LEFTALIGN, x, y, 0, hwnd, None)

menu = CustomMenu()

# Hook for desktop right-click
def monitor_right_click():
    def low_level_mouse_proc(nCode, wParam, lParam):
        if wParam == win32con.WM_RBUTTONDOWN:
            # Get position
            point = win32gui.GetCursorPos()
            # Show custom menu
            desktop_hwnd = win32gui.GetDesktopWindow()
            menu.show(desktop_hwnd, point[0], point[1])
            # Check if selected
            msg = win32gui.PeekMessage(None, 0, 0, win32con.PM_REMOVE)
            if msg and msg[1] == win32con.WM_COMMAND and msg[2] == 1001:
                global running
                running = False
                set_wallpaper(original_wallpaper)
                sys.exit(0)
        return win32gui.CallNextHookEx(None, nCode, wParam, lParam)

    mouse_hook = win32api.SetWindowsHookEx(win32con.WH_MOUSE_LL, low_level_mouse_proc, None, 0)
    win32gui.PumpMessages()
    win32api.UnhookWindowsHookEx(mouse_hook)

# Key listener for reboot not needed, as reboot is system

t1 = threading.Thread(target=cycle_wallpapers)
t2 = threading.Thread(target=play_whispers)
t3 = threading.Thread(target=pulse_edges)
t4 = threading.Thread(target=monitor_right_click)
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
