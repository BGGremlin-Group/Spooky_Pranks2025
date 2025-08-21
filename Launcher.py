#!/usr/bin/env python3

import subprocess
import os
import sys
import tkinter as tk
from tkinter import scrolledtext, simpledialog
import threading
import win32com.client

# Full documentation (unchanged from previous response)
DOCUMENTATION = """
# Documentation: 20 Harmless and Creepy Windows Viruses

## Overview
This document describes 20 harmless Halloween prank programs designed to simulate creepy and humorous "virus" effects on Windows systems. These programs are purely for entertainment, causing no permanent damage or data loss. Some include visual distortions like screen glitches, melting effects, or skull imagery for a spooky yet playful vibe. Each entry includes a description, behavior, visual effects (if applicable), and a "removal" method to ensure reversibility.


---

## Virus 1: Creepy Cursor Crawler
- **Description**: A prank that makes the mouse cursor appear to be "possessed," moving erratically as if controlled by a ghostly entity.
- **Behavior**: The cursor twitches randomly, occasionally darting to the screen's edges or spelling out "HELP" in slow movements. A faint, eerie giggle sound plays intermittently.
- **Visual Effects**: The cursor briefly transforms into a tiny, flickering skull icon every few seconds, with a subtle glitch effect (pixelated distortion) around it.
- **Removal**: Press `Ctrl + Alt + B` or run "Exorcism.exe" from the desktop.

## Virus 2: Melting Desktop Dread
- **Description**: Simulates a screen "melting" effect, making icons and windows appear to drip downward.
- **Behavior**: Desktop icons and open windows slowly slide down the screen, leaving a trail of distorted pixels. A low, ominous hum plays in the background.
- **Visual Effects**: Icons and windows warp with a liquid-like, melting animation, accompanied by occasional skull-shaped distortions in the background.
- **Removal**: Type "SOLIDIFY" in a randomly appearing text box or reboot.

## Virus 3: Phantom Typist
- **Description**: A ghostly "typist" adds creepy messages to text fields.
- **Behavior**: Randomly inserts phrases like "I'm watching you" or "Get out" into text editors, browsers, or chat windows. A faint typing sound plays.
- **Visual Effects**: Text briefly glitches with static-like distortion before appearing, and a translucent skull flashes in the corner of the screen.
- **Removal**: Press `Ctrl + Alt + B` or run the "Begone!" shortcut.

## Virus 4: Haunted Wallpaper
- **Description**: The desktop wallpaper changes to creepy, animated scenes.
- **Behavior**: The wallpaper cycles through eerie images (e.g., foggy graveyards, glowing eyes) with subtle animations. Random whispers play softly.
- **Visual Effects**: Images occasionally glitch with static or flicker to reveal a skull. The screen edges pulse faintly.
- **Removal**: Right-click the desktop and select "Restore Original Wallpaper" or reboot.

## Virus 5: Glitchy Ghost
- **Description**: Causes random screen glitches that form creepy patterns.
- **Behavior**: The screen flickers with static, occasionally forming skull shapes or cryptic symbols. A low, distorted moan plays randomly.
- **Visual Effects**: Glitch effects (pixelated lines, color shifts) dominate, with skulls briefly appearing in distorted areas.
- **Removal**: Press `Ctrl + Shift + G` or run "CleanseGlitch.bat".

## Virus 6: Creepy File Shuffler
- **Description**: Desktop files appear to rearrange themselves into spooky shapes.
- **Behavior**: Files move to form a skull or pentagram on the desktop. A faint cackle plays when the shape completes.
- **Visual Effects**: Files leave a glitchy trail as they move, with a melting effect on their icons.
- **Removal**: Double-click a hidden "OrderRestored.exe" file or reboot.

## Virus 7: Spooky Pop-Up Phantom
- **Description**: Random, creepy pop-ups appear with eerie messages.
- **Behavior**: Small windows pop up with messages like "You're not alone" or skull images, vanishing quickly. A ghostly wail plays.
- **Visual Effects**: Pop-ups have a glitchy, flickering border and sometimes melt before disappearing.
- **Removal**: Press `Alt + F4` three times or run "BanishPopups.exe".

## Virus 8: Screaming Shortcuts
- **Description**: Desktop shortcuts scream when clicked.
- **Behavior**: Clicking any shortcut triggers a brief, eerie scream or moan. The shortcut briefly renames itself to "DOOMED."
- **Visual Effects**: The clicked icon glitches into a skull before reverting.
- **Removal**: Right-click a shortcut and select "Silence," or end "ScreamLink.exe" in Task Manager.

## Virus 9: Flickering Fear
- **Description**: The screen flickers as if possessed, with creepy visuals.
- **Behavior**: The display flashes intermittently, showing faint skulls or shadowy figures. A low, pulsing sound plays.
- **Visual Effects**: Flickers include glitch effects and melting distortions around skull imagery.
- **Removal**: Press `Ctrl + Alt + L` or run "StabilizeScreen.bat".

## Virus 10: Cursed Clock
- **Description**: The system clock displays creepy messages or countdowns.
- **Behavior**: The clock alternates between normal time and phrases like "Time's up" or a countdown to midnight. A ticking sound plays.
- **Visual Effects**: The clock text glitches and occasionally forms a skull shape.
- **Removal**: Double-click the clock and select "Reset Time," or reboot.

## Virus 11: Ghostly Taskbar
- **Description**: The taskbar becomes "haunted," moving and changing.
- **Behavior**: The taskbar shifts positions randomly and displays eerie icons (e.g., skulls). A faint whisper plays.
- **Visual Effects**: Taskbar icons melt or glitch briefly into creepy shapes.
- **Removal**: Right-click the taskbar and select "Exorcise," or end "GhostBar.exe".

## Virus 12: Melting Menu Madness
- **Description**: Start menu items distort and rearrange creepily.
- **Behavior**: Menu items slide into a skull pattern, with some renamed to "Fear" or "Doom." A low growl plays.
- **Visual Effects**: Items melt and glitch as they move, with skull icons appearing briefly.
- **Removal**: Open the Start menu and type "RESTORE" to reset, or run "MenuFix.bat".

## Virus 13: Eerie Error Messages
- **Description**: Fake error messages with creepy themes appear.
- **Behavior**: Pop-ups show errors like "System Haunted" or "Skull Overload." A distant scream plays.
- **Visual Effects**: Messages have glitchy text and melting borders, with skull imagery flashing.
- **Removal**: Click "Dismiss Spirit" on any error pop-up, or end "ErrorGhoul.exe".

## Virus 14: Phantom File Names
- **Description**: File names change to creepy phrases.
- **Behavior**: Files rename to things like "DontOpenMe.txt" or "SkullWarning.doc." A faint cackle plays.
- **Visual Effects**: File icons glitch into skulls before reverting.
- **Removal**: Right-click a file and select "Rename Normal," or reboot.

## Virus 15: Haunted Browser
- **Description**: Web browsers display creepy, fake pages.
- **Behavior**: Random tabs open to pages with skull imagery or messages like "You're being watched." A low hum plays.
- **Visual Effects**: Pages glitch and melt, with skulls fading in and out.
- **Removal**: Close the browser and run "BrowserCleanse.exe," or clear cache.

## Virus 16: Skull Screensaver
- **Description**: A spooky screensaver takes over unexpectedly.
- **Behavior**: A screensaver with floating skulls and eerie fog activates randomly. Ghostly whispers play.
- **Visual Effects**: Skulls glitch and melt across the screen with static bursts.
- **Removal**: Press `Esc` twice or run "BanishScreensaver.exe".

## Virus 17: Creepy Context Menu
- **Description**: Right-click menus show creepy options.
- **Behavior**: Menu options change to "Summon Skull" or "Curse File." A faint moan plays on right-click.
- **Visual Effects**: Menu text glitches and briefly forms skull shapes.
- **Removal**: Select "Restore Menu" from the altered context menu, or end "CreepyMenu.exe".

## Virus 18: Ghostly Glitch Folders
- **Description**: Folders appear to "haunt" themselves, moving and renaming.
- **Behavior**: Folders shift slightly and rename to "Grave" or "Tomb." A low wail plays.
- **Visual Effects**: Folders glitch and melt, with skull icons appearing briefly.
- **Removal**: Open a folder and select "Cleanse" from a custom menu, or reboot.

## Virus 19: Spooky Sound Saboteur
- **Description**: Random creepy sounds interrupt normal audio.
- **Behavior**: Whispers, screams, or cackles play over music or videos. Volume fluctuates slightly.
- **Visual Effects**: A glitchy skull flashes on-screen when sounds trigger.
- **Removal**: Mute and unmute the system, or run "SilenceGhost.bat".

## Virus 20: Phantom Window Wobble
- **Description**: Open windows wobble and distort creepily.
- **Behavior**: Windows shake slightly, with edges warping as if melting. A faint, eerie chant plays.
- **Visual Effects**: Windows glitch and melt, with skulls appearing in distorted areas.
- **Removal**: Press `Ctrl + Alt + S` or run "WindowFix.exe".

---

## Technical Notes
- **Implementation**: These pranks are coded as lightweight Python scripts, using Windows APIs for UI manipulation, sound playback, and visual effects (e.g., PIL for glitch/melt animations). All effects are temporary, stored in memory, and do not modify system files.
- **Safety**: No data is altered or deleted. All changes are cosmetic and reversible via key combos, hidden files, or rebooting.
- **Visual Effects**: Glitch effects use pixelation techniques; melting effects use warping animations; skull imagery is rendered as semi-transparent overlays.

## Disclaimer
These are Halloween inspired pranks, for entertainment.

---

## README: Usage and Instructions

### Usage Instructions
1. **Running the Launcher**: Execute this script (`launcher.py`) to access the interactive menu.
2. **Selecting a Virus**: Enter a number from 1 to 20 to run the corresponding prank virus, 7 for help (displays this documentation), 99 to launch all viruses simultaneously, 100 to launch all viruses sequentially at a user-defined interval, or 0 to exit. Multiple viruses can run concurrently.
3. **Virus Execution**: Each virus runs as a separate process. Use the removal instructions below to stop individual viruses.
4. **Safety**: All viruses are harmless, with no data loss or permanent changes. Effects are reversible via key combos, desktop shortcuts, or rebooting.

### Ethical Guidelines
- **We're not your nanny**: Use at your own discretion.
- **Exit Instructions**: Each virus has a specific removal method (listed below). Ensure you know how to stop each prank.

### Removal Instructions
- **Virus 1**: Press `Ctrl + Alt + B` or run "Exorcism.exe" from the desktop.
- **Virus 2**: Type "SOLIDIFY" in the appearing text box or reboot.
- **Virus 3**: Press `Ctrl + Alt + B` or run the "Begone!" shortcut.
- **Virus 4**: Right-click desktop, select "Restore Original Wallpaper," or reboot.
- **Virus 5**: Press `Ctrl + Shift + G` or run "CleanseGlitch.bat".
- **Virus 6**: Double-click "OrderRestored.exe" or reboot.
- **Virus 7**: Press `Alt + F4` three times or run "BanishPopups.exe".
- **Virus 8**: Right-click shortcut, select "Silence," or end "ScreamLink.exe" in Task Manager.
- **Virus 9**: Press `Ctrl + Alt + L` or run "StabilizeScreen.bat".
- **Virus 10**: Double-click clock, select "Reset Time," or reboot.
- **Virus 11**: Right-click taskbar, select "Exorcise," or end "GhostBar.exe".
- **Virus 12**: Type "RESTORE" in Start menu or run "MenuFix.bat".
- **Virus 13**: Click "Dismiss Spirit" on pop-up or end "ErrorGhoul.exe".
- **Virus 14**: Right-click file, select "Rename Normal," or reboot.
- **Virus 15**: Close browser and run "BrowserCleanse.exe" or clear cache.
- **Virus 16**: Press `Esc` twice or run "BanishScreensaver.exe".
- **Virus 17**: Select "Restore Menu" from context menu or end "CreepyMenu.exe".
- **Virus 18**: Select "Cleanse" from folder context menu or reboot.
- **Virus 19**: Mute and unmute system or run "SilenceGhost.bat".
- **Virus 20**: Press `Ctrl + Alt + S` or run "WindowFix.exe".

### Notes
- Ensure all virus scripts (`virus_1.py` to `virus_20.py`) are in the same directory as this launcher.
- If a virus does not stop as expected, rebooting the system will terminate all effects.
- Running all 20 viruses simultaneously may strain an older PC. Monitor system performance and stop processes if needed.
- For support, refer to the documentation above or experiment safely on your test system.

**Disclaimer**: Use at your own discretion we're not your nanny. These pranks are for fun.
"""

# Interactive Launcher with Concurrent and Sequential Execution
class LauncherApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Prank Virus Launcher")
        self.root.geometry("600x400")
        self.root.configure(bg='black')

        # Instructions label
        tk.Label(self.root, text="Select: 1-20 (virus), 7 (help), 99 (launch all), 100 (sequential), 0 (exit):", 
                 fg='red', bg='black', font=('Arial', 14)).pack(pady=10)

        # Entry for user input
        self.entry = tk.Entry(self.root, font=('Arial', 12))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.process_input)

        # Output area
        self.output = scrolledtext.ScrolledText(self.root, height=15, width=70, fg='white', bg='black', font=('Arial', 10))
        self.output.pack(pady=10)
        self.output.insert(tk.END, "Enter a number (1-20, 7 for help, 99 to launch all, 100 for sequential, 0 to exit).\nMultiple viruses can run at once.\n")
        self.output.config(state='disabled')

        # List to track running processes
        self.processes = []

    def log_message(self, message):
        self.output.config(state='normal')
        self.output.insert(tk.END, message + "\n")
        self.output.see(tk.END)
        self.output.config(state='disabled')

    def process_input(self, event):
        choice = self.entry.get().strip()
        self.entry.delete(0, tk.END)

        try:
            choice = int(choice)
            if choice == 0:
                self.terminate_all()
                self.root.destroy()
                sys.exit(0)
            elif choice == 7:
                self.show_help()
            elif choice == 99:
                self.launch_all()
            elif choice == 100:
                self.launch_sequential()
            elif 1 <= choice <= 20:
                self.run_virus(choice)
            else:
                self.log_message("Invalid choice. Enter 1-20, 7 for help, 99 for all, 100 for sequential, or 0 to exit.")
        except ValueError:
            self.log_message("Please enter a valid number.")

    def run_virus(self, number):
        script_name = f"virus_{number}.py"
        if not os.path.exists(script_name):
            self.log_message(f"Error: {script_name} not found in the current directory.")
            return
        try:
            process = subprocess.Popen([sys.executable, script_name])
            self.processes.append(process)
            self.log_message(f"Started Virus {number}: {self.get_virus_name(number)} (PID: {process.pid})")
        except Exception as e:
            self.log_message(f"Error running {script_name}: {str(e)}")

    def launch_all(self):
        self.log_message("Launching all 20 viruses simultaneously...")
        for i in range(1, 21):
            self.run_virus(i)

    def launch_sequential(self):
        interval = simpledialog.askfloat("Sequential Launch", "Enter interval between launches (seconds, e.g., 2.0):", 
                                        parent=self.root, minvalue=0.1, maxvalue=60.0)
        if interval is None:
            self.log_message("Sequential launch cancelled.")
            return
        self.log_message(f"Launching all 20 viruses sequentially with {interval}-second intervals...")
        def sequential_task():
            for i in range(1, 21):
                self.run_virus(i)
                self.root.update()
                time.sleep(interval)
        threading.Thread(target=sequential_task, daemon=True).start()

    def terminate_all(self):
        self.log_message("Terminating all running virus processes...")
        for process in self.processes:
            try:
                process.terminate()
                process.wait(timeout=3)  # Wait up to 3 seconds for termination
                self.log_message(f"Terminated process PID: {process.pid}")
            except subprocess.TimeoutExpired:
                self.log_message(f"Process PID: {process.pid} did not terminate gracefully.")
            except Exception as e:
                self.log_message(f"Error terminating process PID: {process.pid}: {str(e)}")
        self.processes.clear()

    def show_help(self):
        help_window = tk.Toplevel(self.root)
        help_window.title("Help - Prank Virus Documentation")
        help_window.geometry("800x600")
        help_window.configure(bg='black')

        text_area = scrolledtext.ScrolledText(help_window, height=30, width=90, fg='white', bg='black', font=('Arial', 10))
        text_area.pack(pady=10)
        text_area.insert(tk.END, DOCUMENTATION)
        text_area.config(state='disabled')

    def get_virus_name(self, number):
        names = {
            1: "Creepy Cursor Crawler",
            2: "Melting Desktop Dread",
            3: "Phantom Typist",
            4: "Haunted Wallpaper",
            5: "Glitchy Ghost",
            6: "Creepy File Shuffler",
            7: "Spooky Pop-Up Phantom",
            8: "Screaming Shortcuts",
            9: "Flickering Fear",
            10: "Cursed Clock",
            11: "Ghostly Taskbar",
            12: "Melting Menu Madness",
            13: "Eerie Error Messages",
            14: "Phantom File Names",
            15: "Haunted Browser",
            16: "Skull Screensaver",
            17: "Creepy Context Menu",
            18: "Ghostly Glitch Folders",
            19: "Spooky Sound Saboteur",
            20: "Phantom Window Wobble"
        }
        return names.get(number, "Unknown")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = LauncherApp()
    app.run()
