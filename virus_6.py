#!/usr/bin/env python3
"""
# Virus_6 Creepy File Shuffler
# Part of A Collection of 20 Halloween Inspired Pranks
"""
import pythoncom
import win32com.client as wcomcli
from win32com.shell import shell, shellcon
import win32gui
import win32con
import random
import time
import threading
import sys
import os
import winsound
from PIL import Image, ImageDraw, ImageTk
import tkinter as tk

running = True

# Get desktop folder view
SWC_DESKTOP = 0x08
SWFO_NEEDDISPATCH = 0x01
CLSID_ShellWindows = "{9BA05972-F6A8-11CF-A442-00A0C90A8F39}"
IID_IFolderView = "{CDE725B0-CCC9-4519-917E-325D72FAB4CE}"

def get_folder_view():
    shell_windows = wcomcli.Dispatch(CLSID_ShellWindows)
    hwnd = ctypes.byref(ctypes.c_long())
    dispatch = shell_windows.FindWindowSW(
        wcomcli.VARIANT(pythoncom.VT_I4, shellcon.CSIDL_DESKTOP),
        wcomcli.VARIANT(pythoncom.VT_EMPTY, None),
        SWC_DESKTOP, hwnd, SWFO_NEEDDISPATCH
    )
    service_provider = dispatch.QueryInterface(pythoncom.IID_IServiceProvider)
    browser = service_provider.QueryService(shell.SID_STopLevelBrowser, shell.IID_IShellBrowser)
    shell_view = browser.QueryActiveShellView()
    folder_view = shell_view.QueryInterface(IID_IFolderView)
    return folder_view

folder_view = get_folder_view()
item_count = folder_view.ItemCount(shellcon.SVGIO_ALLVIEW)

pidls = []
original_positions = []

for i in range(item_count):
    pidl = folder_view.Item(i)
    pidls.append(pidl)
    pos = folder_view.GetItemPosition(pidl)
    original_positions.append((pos.x, pos.y))

# Define skull shape positions (relative)
skull_points = [
    (200, 100), (300, 100), (250, 150),  # Head
    (220, 200), (280, 200),  # Jaw
    # More points for full skull or pentagram
    (150, 250), (350, 250), (250, 300), (180, 350), (320, 350)
]  # Simplified

# Shuffle to shape
def shuffle_to_shape():
    while running:
        # Move files gradually to new positions
        for step in range(100):
            new_positions = []
            for i in range(item_count):
                orig_x, orig_y = original_positions[i]
                target_x, target_y = skull_points[i % len(skull_points)]
                new_x = orig_x + (target_x - orig_x) * (step / 100)
                new_y = orig_y + (target_y - orig_y) * (step / 100)
                new_positions.append((int(new_x), int(new_y)))
            folder_view.SelectAndPositionItems(item_count, pidls, new_positions, 0x4000)  # Position
            time.sleep(0.05)
        winsound.Beep(500, 200)  # Cackle simulation
        time.sleep(5)
        # Restore briefly
        folder_view.SelectAndPositionItems(item_count, pidls, original_positions, 0x4000)
        time.sleep(random.uniform(10, 30))

# Glitchy trail and melting icons - use overlay
root = tk.Tk()
root.attributes('-alpha', 0.5)
root.attributes('-topmost', True)
root.overrideredirect(True)
root.geometry(f"{win32gui.GetSystemMetrics(0)}x{win32gui.GetSystemMetrics(1)}+0+0")
canvas = tk.Canvas(root, bg='black', highlightthickness=0)
canvas.pack(fill='both', expand=True)
root.attributes('-transparentcolor', 'black')
hwnd = root.winfo_id()
styles = ctypes.windll.user32.GetWindowLongW(hwnd, -20)
ctypes.windll.user32.SetWindowLongW(hwnd, -20, styles | 0x00080000 | 0x00000020)

def draw_trails():
    while running:
        canvas.delete('all')
        for i in range(item_count):
            x, y = skull_points[i % len(skull_points)]
            canvas.create_line(x-50, y, x+50, y, fill='red', width=2, dash=(4,4))
            # Melting effect: draw dripping lines
            for _ in range(5):
                dx = random.randint(-10, 10)
                canvas.create_line(x + dx, y, x + dx, y + random.randint(20, 50), fill='green', width=1)
        root.update()
        time.sleep(0.1)
        canvas.delete('all')

# Create hidden OrderRestored.exe (simple script)
with open("OrderRestored.py", "w") as f:
    f.write("import sys; sys.exit(0)")
os.system("pyinstaller --onefile OrderRestored.py")  # Assume pyinstaller installed; in practice, create exe manually

# Removal by double-click - but since it's prank, assume user runs it to exit

# Monitor for removal (simplified, assume run to exit)
def monitor_removal():
    while running:
        time.sleep(1)
        # If file executed, but hard to monitor; for prank, user knows

t1 = threading.Thread(target=shuffle_to_shape)
t2 = threading.Thread(target=draw_trails)
t1.start()
t2.start()
t1.join()
t2.join()
