# 📜 Spooky Prank Viruses Project README

**Version 1.0** | **Last Updated: August 21, 2025** | **BGGG**

---

## 🚀 Project Overview

Welcome to the **Spooky Prank Viruses Project**! 🎃 This is a collection of **20 harmless, humorous, and spooky prank programs** designed for Windows systems, created for fun. Each "virus" simulates creepy effects like glitching screens, melting icons, and eerie sounds, all while ensuring **no data loss or permanent system changes**. The project includes an **interactive launcher** (`launcher.py`) that allows you to run any or all of the 20 viruses concurrently, with a help system that provides full documentation and usage instructions. 

The launcher supports simultaneous execution of multiple viruses, and each virus includes clear removal methods to ensure ease of use.

**Key Features**:
- 🖥️ **Interactive GUI Launcher**: Select and run viruses (1–20), view help, or exit cleanly via a `tkinter` interface.
- 👻 **20 Unique Pranks**: Each virus has distinct behaviors, visual effects (e.g., glitches, melting, skulls), and sounds (e.g., whispers, screams).
- 📚 **Integrated Documentation**: Access full details and removal instructions via the help option (7).
- 🔄 **Concurrent Execution**: Run all 20 viruses at once on your experimental PC, with process management for clean termination.
- 🛡️ **Safe and Ethical**: No system harm.
- 🛠️ **Verbose Instructions**: Detailed setup, usage, and troubleshooting for all skill levels.

**Disclaimer**: This project is for **entertainment and educational purposes only** 🎃 

---

## 📋 Table of Contents

- [🎯 Project Goals](#-project-goals)
- [📦 Project Structure](#-project-structure)
- [🛠️ Setup Instructions](#-setup-instructions)
- [🚀 Usage Instructions](#-usage-instructions)
- [🧙‍♂️ Virus Descriptions](#-virus-descriptions)
- [🛑 Removal Instructions](#-removal-instructions)
- [⚙️ Technical Details](#-technical-details)
- [🔍 Troubleshooting](#-troubleshooting)
- [📝 License and Disclaimer](#-license-and-disclaimer)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 🎯 Project Goals

The **Spooky Prank Viruses Project** aims to:
- Provide a **fun and educational** way to explore Windows system manipulation using Python, with a focus on visual and audio effects. 🎨🔊
- Create **20 distinct prank programs** that simulate spooky, virus-like behaviors without causing harm. 👻
- Offer an **interactive launcher** to manage and run pranks concurrently, with a user-friendly GUI and detailed documentation. 🖥️
- Ensure **safety and reversibility**, making all effects temporary and easily removable via key combos, shortcuts, or rebooting. 🔄
- Support experimentation, with considerations for resource constraints and robust error handling. 💾


---

## 📦 Project Structure

The project consists of **21 Python scripts** in a single directory:

- **`launcher.py`**: The main interactive launcher script with a GUI for selecting and running viruses, viewing help, or exiting.
- **`virus_1.py` to `virus_20.py`**: Individual scripts for each prank virus, implementing the behaviors and effects described in the documentation.

**Directory Example**:
```
C:\Experiments\Pranks\
├── launcher.py
├── virus_1.py
├── virus_2.py
├── ...
├── virus_20.py
```

**Generated Files**:
- Each virus creates temporary files (e.g., `skull.png`, `Exorcism.exe`) during execution, which are automatically removed when the virus stops or the system reboots.
- Desktop shortcuts (e.g., `BanishPopups.exe`, `SilenceGhost.bat`) are created as removal methods, pointing to a simple exit script.

**Dependencies**:
- **Python 3.x** (tested with Python 3.8+)
- **Libraries**:
  - `tkinter` (included with Python for GUI)
  - `pynput` (for keyboard/mouse input)
  - `pywin32` (for Windows API interactions)
  - `Pillow` (for image manipulation, e.g., skull icons)
- Install dependencies: `pip install pynput pywin32 Pillow`

---

## 🛠️ Setup Instructions

Follow these steps to set up the project on your experimental Windows PC:

1. **Install Python** 🐍:
   - Download and install **Python 3.8 or later** from [python.org](https://www.python.org/downloads/).
   - Ensure Python is added to your system PATH during installation.

2. **Install Dependencies** 📦:
   - Open a command prompt and run:
     ```bash
     pip install pynput pywin32 Pillow
     ```
   - Verify installation: `pip list` should show `pynput`, `pywin32`, and `Pillow`.

3. **Create Project Directory** 📂:
   - Create a directory for the project, e.g., `C:\Experiments\Pranks`.
   - Save the launcher script (`launcher.py`) and all virus scripts (`virus_1.py` to `virus_20.py`) in this directory.
   - Ensure each virus script matches the code provided earlier for Viruses 1–20.

4. **Verify Scripts** ✅:
   - Confirm all 21 scripts (`launcher.py`, `virus_1.py` to `virus_20.py`) are in the same directory.
   - Check that each script is named correctly (e.g., `virus_7.py` for Spooky Pop-Up Phantom).

5. **Test Environment** 🧪:
   -  PC, ensure it has sufficient resources (at least 2 GB RAM, Windows 7 or later).
   - Monitor CPU and memory usage via Task Manager during testing to avoid overloading the system.

6. **Optional: Create Executables** ⚙️:
   - To run viruses as standalone executables, use `pyinstaller`:
     ```bash
     pip install pyinstaller
     pyinstaller --onefile virus_1.py
     ```
   - This creates `virus_1.exe` in the `dist` folder. Repeat for each virus if desired. Update `launcher.py` to reference `.exe` files instead of `.py` if used.

---

## 🚀 Usage Instructions

The launcher provides an interactive GUI to run the prank viruses, view help, or exit. Here’s how to use it:

1. **Launch the Program** 🎬:
   - Navigate to the project directory in a command prompt:
     ```bash
     cd C:\Experiments\Pranks
     ```
   - Run the launcher:
     ```bash
     python launcher.py
     ```
   - A `tkinter` GUI window will appear with an input field and a log area.

2. **Interact with the GUI** 🖱️:
   - **Input Field**: Enter a number (1–20, 7, or 0) and press Enter.
   - **Options**:
     - **1–20**: Start the corresponding virus (e.g., 1 for Creepy Cursor Crawler). Each virus runs as a separate process, allowing concurrent execution.
     - **7**: Open a help window with full documentation and this README.
     - **0**: Terminate all running virus processes and exit the launcher.
   - **Log Area**: Displays feedback, such as which viruses are running (with PIDs), errors (e.g., missing scripts), or termination confirmations.

3. **Running Viruses** 🦠:
   - Enter a number (e.g., 1) to start `virus_1.py`. The virus runs immediately, and the log shows “Started Virus 1: Creepy Cursor Crawler (PID: 1234)”.
   - Repeat for other viruses (e.g., 2, 3, etc.) to run multiple viruses simultaneously. All 20 can run at once on your experimental PC.
   - Each virus performs its prank (e.g., cursor twitching, screen flickering, eerie sounds) as described below.

4. **Viewing Help** 📖:
   - Enter 7 to open a scrollable window with the full documentation and README, detailing each virus’s behavior, effects, and removal methods.

5. **Exiting** 🛑:
   - Enter 0 to terminate all running virus processes and close the launcher. The log confirms each process’s termination (e.g., “Terminated process PID: 1234”).
   - If a process doesn’t stop, reboot the PC to clear all effects (all changes are temporary).

6. **Monitoring Performance** 📈:
   - On your older PC, monitor system performance in Task Manager (Ctrl+Shift+Esc) while running multiple viruses.
   - If the system slows down, stop some viruses using their removal methods (see below) or reboot.

---

## 🧙‍♂️ Virus Descriptions

Below is the detailed description of each prank virus, including its behavior, visual effects, and purpose, as provided in the original documentation.

### 🦠 Virus 1: Creepy Cursor Crawler
- **Description**: Makes the mouse cursor appear "possessed," moving erratically as if controlled by a ghost. 👻
- **Behavior**: The cursor twitches randomly, occasionally darts to screen edges, or spells “HELP” slowly. A faint giggle sound plays intermittently.
- **Visual Effects**: The cursor briefly becomes a flickering skull icon with pixelated distortion around it.
- **Purpose**: Creates a spooky, playful effect to surprise the user.

### 🦠 Virus 2: Melting Desktop Dread
- **Description**: Simulates a "melting" desktop, with icons and windows dripping downward. 💧
- **Behavior**: Desktop icons and windows slide down, leaving distorted pixel trails. A low, ominous hum plays.
- **Visual Effects**: Icons and windows warp with a liquid-like melting animation; skull-shaped distortions appear in the background.
- **Purpose**: Mimics a surreal, horror-themed desktop malfunction.

### 🦠 Virus 3: Phantom Typist
- **Description**: A ghostly typist inserts creepy messages into text fields. ⌨️
- **Behavior**: Phrases like “I’m watching you” or “Get out” appear in text editors, browsers, or chat windows. A faint typing sound plays.
- **Visual Effects**: Text glitches with static distortion; a translucent skull flashes in the screen corner.
- **Purpose**: Simulates a haunted typing experience.

### 🦠 Virus 4: Haunted Wallpaper
- **Description**: Changes the desktop wallpaper to creepy, animated scenes. 🖼️
- **Behavior**: Cycles through eerie images (e.g., foggy graveyards, glowing eyes) with subtle animations. Random whispers play.
- **Visual Effects**: Images glitch with static or flicker to reveal skulls; screen edges pulse faintly.
- **Purpose**: Creates an unsettling desktop atmosphere.

### 🦠 Virus 5: Glitchy Ghost
- **Description**: Causes random screen glitches forming creepy patterns. 📺
- **Behavior**: The screen flickers with static, forming skull shapes or cryptic symbols. A distorted moan plays.
- **Visual Effects**: Pixelated lines and color shifts dominate, with skulls appearing in distorted areas.
- **Purpose**: Mimics a haunted, malfunctioning display.

### 🦠 Virus 6: Creepy File Shuffler
- **Description**: Desktop files rearrange into spooky shapes. 📁
- **Behavior**: Files move to form a skull or pentagram. A cackle plays when the shape completes.
- **Visual Effects**: Files leave glitchy trails with melting icon effects.
- **Purpose**: Creates a playful, organized chaos effect.

### 🦠 Virus 7: Spooky Pop-Up Phantom
- **Description**: Displays random, creepy pop-up windows. 🪟
- **Behavior**: Small windows show messages like “You’re not alone” or skull images, vanishing quickly. A ghostly wail plays.
- **Visual Effects**: Pop-ups have glitchy, flickering borders and may melt before disappearing.
- **Purpose**: Surprises users with fleeting, eerie messages.

### 🦠 Virus 8: Screaming Shortcuts
- **Description**: Desktop shortcuts scream when clicked. 🔊
- **Behavior**: Clicking a shortcut triggers an eerie scream or moan; the shortcut briefly renames to “DOOMED.”
- **Visual Effects**: The icon glitches into a skull before reverting.
- **Purpose**: Adds a startling audio-visual prank to shortcut interactions.

### 🦠 Virus 9: Flickering Fear
- **Description**: The screen flickers as if possessed, with creepy visuals. 🌫️
- **Behavior**: The display flashes, showing faint skulls or shadowy figures. A pulsing sound plays.
- **Visual Effects**: Flickers include glitch effects and melting distortions around skull imagery.
- **Purpose**: Creates a spooky, unstable screen effect.

### 🦠 Virus 10: Cursed Clock
- **Description**: The system clock displays creepy messages or countdowns. ⏰
- **Behavior**: Alternates between normal time and phrases like “Time’s up” or a midnight countdown. A ticking sound plays.
- **Visual Effects**: Clock text glitches and forms skull shapes.
- **Purpose**: Transforms the clock into a creepy timekeeper.

### 🦠 Virus 11: Ghostly Taskbar
- **Description**: The taskbar becomes “haunted,” moving and changing. 📊
- **Behavior**: The taskbar shifts positions and displays eerie icons (e.g., skulls). A faint whisper plays.
- **Visual Effects**: Taskbar icons melt or glitch into creepy shapes.
- **Purpose**: Disrupts the taskbar with spooky animations.

### 🦠 Virus 12: Melting Menu Madness
- **Description**: Start menu items distort and rearrange creepily. 🍽️
- **Behavior**: Menu items slide into a skull pattern, renamed to “Fear” or “Doom.” A low growl plays.
- **Visual Effects**: Items melt and glitch, with skull icons appearing briefly.
- **Purpose**: Turns the Start menu into a chaotic, spooky interface.

### 🦠 Virus 13: Eerie Error Messages
- **Description**: Fake error messages with creepy themes appear. ⚠️
- **Behavior**: Pop-ups show errors like “System Haunted” or “Skull Overload.” A distant scream plays.
- **Visual Effects**: Messages have glitchy text and melting borders, with skull imagery.
- **Purpose**: Mimics unsettling system errors.

### 🦠 Virus 14: Phantom File Names
- **Description**: File names change to creepy phrases. 📜
- **Behavior**: Files rename to “DontOpenMe.txt” or “SkullWarning.doc.” A faint cackle plays.
- **Visual Effects**: File icons glitch into skulls before reverting.
- **Purpose**: Creates a spooky file-naming prank.

### 🦠 Virus 15: Haunted Browser
- **Description**: Web browsers display creepy, fake pages. 🌐
- **Behavior**: Random tabs open to pages with skull imagery or messages like “You’re being watched.” A low hum plays.
- **Visual Effects**: Pages glitch and melt, with skulls fading in and out.
- **Purpose**: Simulates a haunted browsing experience.

### 🦠 Virus 16: Skull Screensaver
- **Description**: A spooky screensaver takes over unexpectedly. 🖥️
- **Behavior**: Floating skulls and eerie fog activate randomly. Ghostly whispers play.
- **Visual Effects**: Skulls glitch and melt across the screen with static bursts.
- **Purpose**: Creates an intrusive, spooky screensaver.

### 🦠 Virus 17: Creepy Context Menu
- **Description**: Right-click menus show creepy options. 🖱️
- **Behavior**: Menu options change to “Summon Skull” or “Curse File.” A faint moan plays on right-click.
- **Visual Effects**: Menu text glitches and forms skull shapes.
- **Purpose**: Adds a spooky twist to context menus.

### 🦠 Virus 18: Ghostly Glitch Folders
- **Description**: Folders move and rename themselves creepily. 📂
- **Behavior**: Folders shift slightly and rename to “Grave” or “Tomb.” A low wail plays.
- **Visual Effects**: Folders glitch and melt, with skull icons appearing briefly.
- **Purpose**: Simulates haunted folder behavior.

### 🦠 Virus 19: Spooky Sound Saboteur
- **Description**: Random creepy sounds interrupt normal audio. 🔊
- **Behavior**: Whispers, screams, or cackles play over music or videos. Volume fluctuates slightly.
- **Visual Effects**: A glitchy skull flashes when sounds trigger.
- **Purpose**: Disrupts audio with eerie effects.

### 🦠 Virus 20: Phantom Window Wobble
- **Description**: Open windows wobble and distort creepily. 🪟
- **Behavior**: Windows shake, with edges warping as if melting. A faint chant plays.
- **Visual Effects**: Windows glitch and melt, with skulls in distorted areas.
- **Purpose**: Creates a surreal, wobbling window effect.

---

## 🛑 Removal Instructions

Each virus is designed to be **easily reversible** with specific removal methods. Below are the instructions for stopping each virus, plus a universal fallback (rebooting). Use these to stop individual viruses, or enter 0 in the launcher to terminate all running processes.

- **Virus 1**: Press `Ctrl + Alt + B` or run “Exorcism.exe” from the desktop.
- **Virus 2**: Type “SOLIDIFY” in the appearing text box or reboot.
- **Virus 3**: Press `Ctrl + Alt + B` or run the “Begone!” shortcut.
- **Virus 4**: Right-click desktop, select “Restore Original Wallpaper,” or reboot.
- **Virus 5**: Press `Ctrl + Shift + G` or run “CleanseGlitch.bat”.
- **Virus 6**: Double-click “OrderRestored.exe” or reboot.
- **Virus 7**: Press `Alt + F4` three times or run “BanishPopups.exe”.
- **Virus 8**: Right-click shortcut, select “Silence,” or end “ScreamLink.exe” in Task Manager.
- **Virus 9**: Press `Ctrl + Alt + L` or run “StabilizeScreen.bat”.
- **Virus 10**: Double-click clock, select “Reset Time,” or reboot.
- **Virus 11**: Right-click taskbar, select “Exorcise,” or end “GhostBar.exe”.
- **Virus 12**: Type “RESTORE” in Start menu or run “MenuFix.bat”.
- **Virus 13**: Click “Dismiss Spirit” on pop-up or end “ErrorGhoul.exe”.
- **Virus 14**: Right-click file, select “Rename Normal,” or reboot.
- **Virus 15**: Close browser and run “BrowserCleanse.exe” or clear cache.
- **Virus 16**: Press `Esc` twice or run “BanishScreensaver.exe”.
- **Virus 17**: Select “Restore Menu” from context menu or end “CreepyMenu.exe”.
- **Virus 18**: Select “Cleanse” from folder context menu or reboot.
- **Virus 19**: Mute and unmute system or run “SilenceGhost.bat”.
- **Virus 20**: Press `Ctrl + Alt + S` or run “WindowFix.exe”.

**Universal Fallback**:
- **Reboot**: Restarting the PC terminates all virus effects, as they are memory-based and do not modify system files. 🔄
- **Launcher Exit**: Enter 0 in the launcher to stop all running virus processes.

**Note**: If a virus doesn’t stop as expected, check Task Manager for processes like `python.exe` or `virus_<number>.exe` and end them manually. Rebooting is always a safe option.

---

## ⚙️ Technical Details

### 🖥️ System Requirements
- **OS**: Windows 7 or later (tested on Windows 10/11).
- **Python**: 3.8 or later.
- **Hardware**: Minimum 2 GB RAM, 1 GHz CPU. Older PCs may experience slowdowns when running all 20 viruses simultaneously.
- **Dependencies**:
  - `tkinter`: For GUI (included with Python).
  - `pynput`: For keyboard/mouse input (`pip install pynput`).
  - `pywin32`: For Windows API interactions (`pip install pywin32`).
  - `Pillow`: For image manipulation (`pip install Pillow`).

### 🛠️ Implementation
- **Launcher (`launcher.py`)**:
  - Uses `tkinter` for a GUI with an input field and log area.
  - Launches viruses via `subprocess.Popen`, allowing concurrent execution.
  - Tracks processes in a list for termination on exit (option 0).
  - Displays help with full documentation via a scrollable `tkinter` window.
- **Virus Scripts**:
  - Written in Python, using:
    - `tkinter` for overlays (e.g., pop-ups, screensavers).
    - `pynput` for key/mouse events (e.g., cursor control, key combos).
    - `winsound` for eerie sounds (e.g., whispers, screams).
    - `pywin32` for Windows API calls (e.g., taskbar, desktop manipulation).
    - `Pillow` for visual effects (e.g., skull icons, glitches, melting).
  - Effects are temporary, stored in memory, and do not modify system files.
- **Visual Effects**:
  - **Glitches**: Pixelated lines, static, and color shifts using `tkinter` canvases or `Pillow`.
  - **Melting**: Warping animations via `tkinter` geometry changes or `Pillow` image distortions.
  - **Skulls**: Semi-transparent PNGs rendered as overlays.
- **Concurrency**: Each virus runs in a separate process, allowing simultaneous execution. The launcher manages process IDs for clean termination.

### 🧪 Performance on Older PCs
- Running all 20 viruses may strain your knock-around PC due to:
  - Multiple `tkinter` windows (e.g., pop-ups, overlays).
  - Frequent API calls (`pywin32` for desktop/taskbar manipulation).
  - Sound playback (`winsound`) and image rendering (`Pillow`).
- **Mitigation**:
  - Start with 1–5 viruses and monitor performance in Task Manager.
  - Use removal methods or reboot if the system slows down.
  - The launcher logs process IDs for manual termination if needed.


---

## 🔍 Troubleshooting

Here are common issues and solutions for running the project on your PC:

- **Problem**: Launcher fails to start with “No module named <library>”.
  - **Solution**: Install missing dependencies:
    ```bash
    pip install pynput pywin32 Pillow
    ```

- **Problem**: “Error: virus_<number>.py not found” in the log.
  - **Solution**: Ensure all scripts (`virus_1.py` to `virus_20.py`) are in the same directory as `launcher.py`. Verify file names match exactly.

- **Problem**: System slows down or freezes when running multiple viruses.
  - **Solution**:
    - Stop viruses using their removal methods (e.g., key combos, shortcuts).
    - Enter 0 in the launcher to terminate all processes.
    - Reboot the PC to clear all effects.
    - Run fewer viruses (e.g., 1–5) to reduce resource usage.

- **Problem**: A virus doesn’t stop with its key combo or shortcut.
  - **Solution**:
    - Open Task Manager (Ctrl+Shift+Esc), find `python.exe` or `virus_<number>.exe`, and end the process.
    - Reboot the PC to terminate all effects.
    - Check the log for the process ID (PID) and end it manually.

- **Problem**: Visual effects (e.g., skulls, glitches) don’t display correctly.
  - **Solution**:
    - Ensure `Pillow` is installed (`pip install Pillow`).
    - Verify your PC’s graphics driver supports `tkinter` rendering.
    - Reduce the number of running viruses to lower GPU load.

- **Problem**: Sounds (e.g., whispers, screams) don’t play.
  - **Solution**:
    - Check that your PC’s audio is enabled and not muted.
    - Test `winsound` with a simple script:
      ```python
      import winsound
      winsound.Beep(1000, 500)
      ```
    - Ensure no other applications are blocking audio output.

- **Problem**: Launcher GUI is unresponsive.
  - **Solution**:
    - Close the launcher via Task Manager (`python.exe`).
    - Restart the launcher and run fewer viruses.
    - Reboot the PC if needed.

For additional help, refer to the help window (option 7) or contact the script creator (not applicable for this fictional setup).

---

## 📝 License and Disclaimer

**License**: This project is provided under the **MIT License** for educational and experimental use:
```
MIT License

Copyright (c) 2025 BG Gremlin Group 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

**Disclaimer**:
- This project is for **entertainment and educational purposes**.
- **No warranty**: The software is provided as-is, with no guarantee of performance or suitability.
- **Safety**: All effects are temporary and reversible. No data loss or system damage will occur if used as intended.

---

## 🙌 Acknowledgments

- **Python Community**: For providing libraries like `tkinter`, `pynput`, `pywin32`, and `Pillow`. 🐍
- **Ai Community**: `xAi` assisted DevOps
- **Windows APIs**: For enabling creative system manipulations in a safe manner. 🖥️
- **You**: For experimenting with this fun project on `your PC`! 🎉

---

## 🌟 Final Notes

The **Spooky Prank Viruses Project** is a playfulcollection, with **20 unique pranks**, a **user-friendly launcher**, and **comprehensive documentation**, it’s perfect for anyone looking for an interesting experience. Have fun testing the spooky effects, but keep an eye on performance and use the removal methods to keep things under control.

**Happy Haunting!** 👻

### Background Gremlin Group 
***Creating Unique Tools for Unique Individuals***
