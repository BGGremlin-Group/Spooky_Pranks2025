#!/usr/bin/env python3
"""
# Virus_17 Creepy Context Menu
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
import ctypes
from PIL import Image, ImageDraw, ImageTk
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
    image.save("skull_context.png")
    return Image.open("skull_context.png")

skull_image = create_skull_image()

# Custom context menu
class CustomMenu:
    def __init__(self):
        self.hmenu = win32gui.CreatePopupMenu()
        creepy_options = ["Summon Skull", "Curse File", "Haunt This", "Doom"]
        for i, option in enumerate(creepy_options, 1001):
            win32gui.AppendMenu(self.hmenu, win32con.MF_STRING, i, option)
        win32gui.AppendMenu(self.hmenu, win32con.MF_STRING, 1005, "Restore Menu")

    def show(self, hwnd, x, y):
        win32gui.TrackPopupMenu(self.hmenu, win32con.TPM_LEFTALIGN, x, y, 0, hwnd, None)

menu = CustomMenu()

# Monitor right-click
def monitor_right_click():
    root = tk.Tk()
    root.attributes('-alpha', 0.3)
    root.attributes('-topmost', True)
    root.overrideredirect(True)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")
    canvas = tk.Canvas(root, bg='black', highlightthickness=0)
    canvas.pack(fill='both', expand=True)
    root.attributes('-transparentcolor', 'black')
    hwnd_canvas = root.winfo_id()
    styles = ctypes.windll.user32.GetWindowLongW(hwnd_canvas, -20)
    ctypes.windll.user32.SetWindowLongW(hwnd_canvas, -20, styles | 0x00080000 | 0x00000020)
    tk_img = ImageTk.PhotoImage(skull_image)

    def low_level_mouse_proc(nCode, wParam, lParam):
        if wParam == win32con.WM_RBUTTONDOWN and running:
            point = win32gui.GetCursorPos()
            hwnd = win32gui.WindowFromPoint(point)
            menu.show(hwnd, point[0], point[1])
            # Show skull on click
            canvas.delete('all')
            canvas.create_image(point[0], point[1], image=tk_img)
            canvas.image = tk_img
            root.update()
            time.sleep(0.5)
            canvas.delete('all')
            winsound.Beep(400 + random.randint(-100, 100), 300)  # Moan
            # Check menu selection
            msg = win32gui.PeekMessage(None, 0, 0, win32con.PM_REMOVE)
            if msg and msg[1] == win32con.WM_COMMAND and msg[2] == 1005:
                global running
                running = False
                root.destroy()
                sys.exit(0)
        return win32gui.CallNextHookEx(None, nCode, wParam, lParam)

    mouse_hook = win32api.SetWindowsHookEx(win32con.WH_MOUSE_LL, low_level_mouse_proc, None, 0)
    win32gui.PumpMessages()
    win32api.UnhookWindowsHookEx(mouse_hook)

# Create CreepyMenu.exe
shell = win32com.client.Dispatch("WScript.Shell")
desktop = shell.SpecialFolders("Desktop")
shortcut_path = os.path.join(desktop, "CreepyMenu.lnk")
shortcut = shell.CreateShortCut(shortcut_path)
shortcut.Targetpath = sys.executable
shortcut.Arguments = '-c "import os; os._exit(0)"'
shortcut.save()

t1 = threading.Thread(target=monitor_right_click)
t1.start()
t1.join()
