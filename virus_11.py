#!/usr/bin/env python3
"""
# Virus_11 Ghostly Taskbar
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
import winsound
from PIL import Image, ImageDraw
import tkinter as tk
import ctypes
import os

running = True

# Get taskbar handle
taskbar_hwnd = win32gui.FindWindow("Shell_TrayWnd", None)

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
    image.save("skull_taskbar.ico")
    return os.path.abspath("skull_taskbar.ico")

skull_icon_path = create_skull_icon()

# Overlay for melting effect
root = tk.Tk()
root.attributes('-alpha', 0.5)
root.attributes('-topmost', True)
root.overrideredirect(True)
taskbar_rect = win32gui.GetWindowRect(taskbar_hwnd)
root.geometry(f"{taskbar_rect[2]-taskbar_rect[0]}x{taskbar_rect[3]-taskbar_rect[1]}+{taskbar_rect[0]}+{taskbar_rect[1]}")
canvas = tk.Canvas(root, bg='black', highlightthickness=0)
canvas.pack(fill='both', expand=True)
root.attributes('-transparentcolor', 'black')
hwnd = root.winfo_id()
styles = ctypes.windll.user32.GetWindowLongW(hwnd, -20)
ctypes.windll.user32.SetWindowLongW(hwnd, -20, styles | 0x00080000 | 0x00000020)

# Shift taskbar position
def shift_taskbar():
    screen_width = win32api.GetSystemMetrics(0)
    screen_height = win32api.GetSystemMetrics(1)
    while running:
        pos = random.choice(['left', 'right', 'top', 'bottom'])
        if pos == 'left':
            win32gui.SetWindowPos(taskbar_hwnd, 0, 0, 0, 0, screen_height, win32con.SWP_NOZORDER)
        elif pos == 'right':
            win32gui.SetWindowPos(taskbar_hwnd, 0, screen_width - 40, 0, 40, screen_height, win32con.SWP_NOZORDER)
        elif pos == 'top':
            win32gui.SetWindowPos(taskbar_hwnd, 0, 0, 0, screen_width, 40, win32con.SWP_NOZORDER)
        elif pos == 'bottom':
            win32gui.SetWindowPos(taskbar_hwnd, 0, 0, screen_height - 40, screen_width, 40, win32con.SWP_NOZORDER)
        # Update overlay position
        new_rect = win32gui.GetWindowRect(taskbar_hwnd)
        root.geometry(f"{new_rect[2]-new_rect[0]}x{new_rect[3]-new_rect[1]}+{new_rect[0]}+{new_rect[1]}")
        time.sleep(random.uniform(10, 30))

# Display eerie icons and melting effect
def display_eerie_icons():
    tk_img = ImageTk.PhotoImage(Image.open(skull_icon_path))
    while running:
        canvas.delete('all')
        # Place skull icons
        for i in range(5):
            canvas.create_image(50 + i*50, 20, image=tk_img)
            canvas.image = tk_img
            # Melting effect
            canvas.create_line(50 + i*50, 20, 50 + i*50, 40 + random.randint(10, 30), fill='green', width=2)
        root.update()
        time.sleep(0.5)
        canvas.delete('all')
        time.sleep(random.uniform(5, 15))

# Play whisper sound
def play_whisper():
    while running:
        time.sleep(random.uniform(10, 30))
        winsound.Beep(300 + random.randint(-100, 100), 400)

# Custom right-click menu for removal
class CustomMenu:
    def __init__(self):
        self.hmenu = win32gui.CreatePopupMenu()
        win32gui.AppendMenu(self.hmenu, win32con.MF_STRING, 1001, "Exorcise")

    def show(self, hwnd, x, y):
        win32gui.TrackPopupMenu(self.hmenu, win32con.TPM_LEFTALIGN, x, y, 0, hwnd, None)

menu = CustomMenu()

# Monitor right-click
def monitor_right_click():
    def low_level_mouse_proc(nCode, wParam, lParam):
        if wParam == win32con.WM_RBUTTONDOWN and running:
            point = win32gui.GetCursorPos()
            hwnd = win32gui.WindowFromPoint(point)
            if hwnd == taskbar_hwnd:
                menu.show(taskbar_hwnd, point[0], point[1])
                msg = win32gui.PeekMessage(None, 0, 0, win32con.PM_REMOVE)
                if msg and msg[1] == win32con.WM_COMMAND and msg[2] == 1001:
                    global running
                    running = False
                    root.destroy()
                    sys.exit(0)
        return win32gui.CallNextHookEx(None, nCode, wParam, lParam)

    mouse_hook = win32api.SetWindowsHookEx(win32con.WH_MOUSE_LL, low_level_mouse_proc, None, 0)
    win32gui.PumpMessages()
    win32api.UnhookWindowsHookEx(mouse_hook)

# Create hidden GhostBar.exe
shell = win32com.client.Dispatch("WScript.Shell")
desktop = shell.SpecialFolders("Desktop")
shortcut_path = os.path.join(desktop, "GhostBar.lnk")
shortcut = shell.CreateShortCut(shortcut_path)
shortcut.Targetpath = sys.executable
shortcut.Arguments = '-c "import os; os._exit(0)"'
shortcut.save()

t1 = threading.Thread(target=shift_taskbar)
t2 = threading.Thread(target=display_eerie_icons)
t3 = threading.Thread(target=play_whisper)
t4 = threading.Thread(target=monitor_right_click)
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
