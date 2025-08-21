```#!/usr/bin/env python3
"""
# Virus_8 Screaming Shortcuts
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
from PIL import Image, ImageDraw
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

# Store original shortcut names
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
    draw.line((11, 23, 21, 23), fill=(0, 0, 0, 255), width=1)
    image.save("skull.ico")
    return "skull.ico"

skull_icon_path = os.path.abspath(create_skull_icon())

# Monitor mouse clicks
def monitor_clicks():
    def low_level_mouse_proc(nCode, wParam, lParam):
        if wParam == win32con.WM_LBUTTONDOWN and running:
            point = win32gui.GetCursorPos()
            hwnd = win32gui.WindowFromPoint(point)
            # Check if click is on desktop
            desktop_hwnd = win32gui.GetDesktopWindow()
            if hwnd == desktop_hwnd:
                # Find closest icon
                min_dist = float('inf')
                selected_idx = -1
                for i in range(item_count):
                    pos = folder_view.GetItemPosition(pidls[i])
                    dist = ((pos.x - point[0])**2 + (pos.y - point[1])**2)**0.5
                    if dist < min_dist:
                        min_dist = dist
                        selected_idx = i
                if selected_idx >= 0:
                    # Play scream
                    winsound.Beep(1000 + random.randint(-200, 200), 300)
                    # Rename to DOOMED
                    folder_view.SetItemName(pidls[selected_idx], "DOOMED")
                    # Change icon (simplified, requires shell refresh)
                    # In practice, changing icon is complex; simulate with overlay
                    root = tk.Tk()
                    root.attributes('-alpha', 0.8)
                    root.overrideredirect(True)
                    root.geometry(f"32x32+{point[0]}+{point[1]}")
                    img = Image.open(skull_icon_path)
                    tk_img = ImageTk.PhotoImage(img)
                    label = tk.Label(root, image=tk_img)
                    label.pack()
                    root.update()
                    time.sleep(0.5)
                    root.destroy()
                    # Restore name
                    time.sleep(1)
                    folder_view.SetItemName(pidls[selected_idx], original_names[selected_idx])
        return win32gui.CallNextHookEx(None, nCode, wParam, lParam)

    mouse_hook = win32api.SetWindowsHookEx(win32con.WH_MOUSE_LL, low_level_mouse_proc, None, 0)
    win32gui.PumpMessages()
    win32api.UnhookWindowsHookEx(mouse_hook)

# Custom right-click menu for removal
class CustomMenu:
    def __init__(self):
        self.hmenu = win32gui.CreatePopupMenu()
        win32gui.AppendMenu(self.hmenu, win32con.MF_STRING, 1001, "Silence")

    def show(self, hwnd, x, y):
        win32gui.TrackPopupMenu(self.hmenu, win32con.TPM_LEFTALIGN, x, y, 0, hwnd, None)

menu = CustomMenu()

# Monitor right-click for removal
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
                    sys.exit(0)
        return win32gui.CallNextHookEx(None, nCode, wParam, lParam)

    mouse_hook = win32api.SetWindowsHookEx(win32con.WH_MOUSE_LL, low_level_mouse_proc, None, 0)
    win32gui.PumpMessages()
    win32api.UnhookWindowsHookEx(mouse_hook)

# Create hidden ScreamLink.exe
shell = win32com.client.Dispatch("WScript.Shell")
desktop = shell.SpecialFolders("Desktop")
shortcut_path = os.path.join(desktop, "ScreamLink.lnk")
shortcut = shell.CreateShortCut(shortcut_path)
shortcut.Targetpath = sys.executable
shortcut.Arguments = '-c "import os; os._exit(0)"'
shortcut.save()

t1 = threading.Thread(target=monitor_clicks)
t2 = threading.Thread(target=monitor_right_click)
t1.start()
t2.start()
t1.join()
t2.join()
