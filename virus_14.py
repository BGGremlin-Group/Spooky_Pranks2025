#!/usr/bin/env python3
"""
# Virus_14 Phantom File Names
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
import os
import winsound
from PIL import Image, ImageDraw, ImageTk
import tkinter as tk
import ctypes

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
original_names = []

# Store original file names
for i in range(item_count):
    pidl = folder_view.Item(i)
    pidls.append(pidl)
    name = folder_view.GetItemName(pidl)
    original_names.append(name)

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
    image.save("skull_file.ico")
    return os.path.abspath("skull_file.ico")

skull_icon_path = create_skull_icon()

# Overlay for skull icons
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

# Rename files and show skull icons
def rename_files():
    creepy_names = ["DontOpenMe.txt", "SkullWarning.doc", "HauntedFile.exe", "Cursed.txt"]
    tk_img = ImageTk.PhotoImage(Image.open(skull_icon_path))
    while running:
        for i in range(item_count):
            new_name = random.choice(creepy_names)
            folder_view.SetItemName(pidls[i], new_name)
            pos = folder_view.GetItemPosition(pidls[i])
            canvas.create_image(pos.x, pos.y, image=tk_img)
            canvas.image = tk_img
            root.update()
            time.sleep(0.5)
            canvas.delete('all')
            folder_view.SetItemName(pidls[i], original_names[i])
        time.sleep(random.uniform(10, 30))
        winsound.Beep(600, 200)  # Cackle

# Custom right-click menu for removal
class CustomMenu:
    def __init__(self):
        self.hmenu = win32gui.CreatePopupMenu()
        win32gui.AppendMenu(self.hmenu, win32con.MF_STRING, 1001, "Rename Normal")

    def show(self, hwnd, x, y):
        win32gui.TrackPopupMenu(self.hmenu, win32con.TPM_LEFTALIGN, x, y, 0, hwnd, None)

menu = CustomMenu()

# Monitor right-click
def monitor_right_click():
    def low_level_mouse_proc(nCode, wParam, lParam):
        if wParam == win32con.WM_RBUTTONDOWN and running:
            point = win32gui.GetCursorPos()
            hwnd = win32gui.WindowFromPoint(point)
            desktop_hwnd = win32gui.GetDesktopWindow()
            if hwnd == desktop_hwnd:
                menu.show(desktop_hwnd, point[0], point[1])
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

t1 = threading.Thread(target=rename_files)
t2 = threading.Thread(target=monitor_right_click)
t1.start()
t2.start()
t1.join()
t2.join()
