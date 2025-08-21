#!/usr/bin/env python3
"""
# Virus_15 Haunted Browser
# Part of A Collection of 20 Halloween Inspired Pranks
"""
import webbrowser
import random
import time
import threading
import sys
import winsound
import os
import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
import ctypes

running = True

# Create creepy HTML page
def create_creepy_page():
    html_content = """
    <html>
    <head><title>Haunted Browser</title></head>
    <body style="background: black; color: red; text-align: center; font-family: Arial;">
        <h1>You're being watched</h1>
        <img src="skull.png" style="opacity: 0.5;" id="skull">
        <script>
            var img = document.getElementById('skull');
            function glitch() {
                img.style.marginLeft = (Math.random() * 50 - 25) + 'px';
                img.style.marginTop = (Math.random() * 50 - 25) + 'px';
                img.style.opacity = Math.random();
            }
            setInterval(glitch, 200);
        </script>
    </body>
    </html>
    """
    with open("haunted.html", "w") as f:
        f.write(html_content)
    # Create skull image
    size = (100, 100)
    image = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.ellipse((20, 10, 80, 70), fill=(255, 255, 255, 128))
    draw.ellipse((30, 25, 40, 35), fill=(0, 0, 0, 255))
    draw.ellipse((60, 25, 70, 35), fill=(0, 0, 0, 255))
    draw.polygon((50, 40, 45, 50, 55, 50), fill=(0, 0, 0, 255))
    image.save("skull.png")
    return os.path.abspath("haunted.html")

page_path = create_creepy_page()

# Open random tabs
def open_haunted_tabs():
    browsers = ["chrome", "firefox", "edge"]
    while running:
        time.sleep(random.uniform(10, 30))
        browser = random.choice(browsers)
        try:
            webbrowser.get(browser).open("file://" + page_path)
        except:
            webbrowser.open("file://" + page_path)  # Fallback
        winsound.Beep(200 + random.randint(-50, 50), 500)  # Low hum

# Create BrowserCleanse.exe
shell = win32com.client.Dispatch("WScript.Shell")
desktop = shell.SpecialFolders("Desktop")
shortcut_path = os.path.join(desktop, "BrowserCleanse.lnk")
shortcut = shell.CreateShortCut(shortcut_path)
shortcut.Targetpath = sys.executable
shortcut.Arguments = '-c "import os; os._exit(0)"'
shortcut.save()

t1 = threading.Thread(target=open_haunted_tabs)
t1.start()
t1.join()
