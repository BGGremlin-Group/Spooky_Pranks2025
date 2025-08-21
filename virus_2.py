#!/usr/bin/env python3
"""
# Virus_2 Melting Desktop Dread
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
from pynput import keyboard
import tk inter as tk
import winsound

running = True

SWC_DESKTOP = 0x08
SWFO_NEEDDISPATCH = 0x01

CLSID_ShellWindows = "{9BA05972-F6A8-11CF-A442-00A0C90A8F39}"
IID_IFolderView = "{CDE725B0-CCC9-4519-917E-325D72FAB4CE}"

def get_folder_view():
    shell_windows = wcomcli.Dispatch(CLSID_ShellWindows)
    hwnd = 0
    dispatch = shell_windows.FindWindowSW(
        wcomcli.VARIANT(pythoncom.VT_I4, shellcon.CSIDL_DESKTOP),
        wcomcli.VARIANT(pythoncom.VT_EMPTY, None),
        SWC_DESKTOP, hwnd, SWFO_NEEDDISPATCH,
    )
    service_provider = dispatch._oleobj_.QueryInterface(pythoncom.IID_IServiceProvider)
    browser = service_provider.QueryService(shell.SID_STopLevelBrowser, shell.IID_IShellBrowser)
    shell_view = browser.QueryActiveShellView()
    folder_view = shell_view.QueryInterface(IID_IFolderView)
    return folder_view

folder_view = get_folder_view()
items_len = folder_view.ItemCount(shellcon.SVGIO_ALLVIEW)

pidls = []
original_positions = []

for i in range(items_len):
    item = folder_view.Item(i)
    pidls.append(item)
    pos = folder_view.GetItemPosition(item)
    original_positions.append(pos)

def restore_icons():
    folder_view.SelectAndPositionItems(items_len, pidls, original_positions, 0x4000)  # SVSI_POSITIONITEM = 0x4000

def slide_icons():
    step = 1
    steps = 500  # slide down by 500 pixels
    for t in range(steps):
        if not running:
            break
        new_positions = [(x, y + t * step) for (x, y) in original_positions]
        folder_view.SelectAndPositionItems(items_len, pidls, new_positions, 0x4000)
        time.sleep(0.05)

def slide_windows():
    step = 1
    steps = 500
    for t in range(steps):
        if not running:
            break
        def callback(hwnd, extra):
            if win32gui.IsWindowVisible(hwnd):
                l, t, r, b = win32gui.GetWindowRect(hwnd)
                win32gui.SetWindowPos(hwnd, 0, l, t + step, 0, 0, win32con.SWP_NOSIZE | win32con.SWP_NOZORDER | win32con.SWP_NOACTIVATE)
        win32gui.EnumWindows(callback, None)
        time.sleep(0.05)

def play_hum():
    while running:
        winsound.Beep(200, 1000)
        time.sleep(1)

def text_box_removal():
    while running:
        time.sleep(random.uniform(10, 30))
        root = tk.Tk()
        root.attributes('-topmost', True)
        entry = tk.Entry(root)
        entry.pack()
        def check(event):
            if entry.get().upper() == "SOLIDIFY":
                global running
                running = False
                restore_icons()
                root.destroy()
                sys.exit(0)
        entry.bind("<Return>", check)
        root.mainloop()

def on_press(key):
    pass  # Removal is via text box

listener = keyboard.Listener(on_press=on_press)
listener.start()

t1 = threading.Thread(target=slide_icons)
t2 = threading.Thread(target=slide_windows)
t3 = threading.Thread(target=play_hum)
t4 = threading.Thread(target=text_box_removal)
t1.start()
t2.start()
t3.start()
t4.start()
listener.join()
