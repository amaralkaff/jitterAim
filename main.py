import time
import win32api
import keyboard
import tkinter as tk
from tkinter import font as tkFont

# Global variables
state_left = win32api.GetKeyState(0x01)
state_right = win32api.GetKeyState(0x02)
flat_toggle = '6'
last_state_flat = False
enabled_flat = False
alternate = True

def flat_line(s_left, s_right, x):
    global alternate
    if x != s_right:
        while x < 0:
            a = win32api.GetKeyState(0x01)
            if a != s_left:
                if a < 0:
                    win32api.mouse_event(0x01, 3, 0)
                    time.sleep(0.0001)
                    move_up = -5 if alternate else -4
                    win32api.mouse_event(0x01, 0, move_up)
                    time.sleep(0.0001)
                    win32api.mouse_event(0x01, 0, 3)
                    time.sleep(0.0001)
                    win32api.mouse_event(0x01, -3, 0)
                    time.sleep(0.0001)

                    win32api.mouse_event(0x01, 0, 3)
                    time.sleep(0.0001)

                    win32api.mouse_event(0x01, -3, 0)
                    time.sleep(0.0001)
                    win32api.mouse_event(0x01, 0, 3)
                    time.sleep(0.0001)
                    win32api.mouse_event(0x01, 0, move_up)
                    time.sleep(0.0001)
                    win32api.mouse_event(0x01, 3, 0)
                    time.sleep(0.0001)

                    alternate = not alternate

            x = win32api.GetKeyState(0x02)

def check_flat_line():
    global last_state_flat
    b = win32api.GetKeyState(0x02)
    key_down_flat = keyboard.is_pressed(flat_toggle)

    if key_down_flat != last_state_flat:
        last_state_flat = key_down_flat
        if last_state_flat:
            global enabled_flat
            enabled_flat = not enabled_flat
            if enabled_flat:
                status_label.config(text="Anti-recoil flat line ON", fg="#00FF00")
            else:
                status_label.config(text="Anti-recoil flat line OFF", fg="#FF0000")

    if enabled_flat:
        flat_line(state_left, state_right, b)
    root.after(1, check_flat_line)

# Setup the GUI
root = tk.Tk()
root.title("Anti-Recoil Script Control")

# Set window position to top-left
root.geometry("+0+0")
root.overrideredirect(True)
root.attributes('-topmost', True)
root.attributes('-alpha', 0.5)  # Set the transparency of the window

# Enhance visual appearance with neon glow
customFont = tkFont.Font(family="Helvetica", size=12, weight="bold")
root.configure(bg='black')

# Neon effect on text
status_label = tk.Label(root, text="Anti-recoil flat line OFF", font=customFont, bg="black", fg="#00FF00")
status_label.pack(pady=10, fill=tk.X)

# Start the periodic check
root.after(1, check_flat_line)

# Start the GUI
root.mainloop()
