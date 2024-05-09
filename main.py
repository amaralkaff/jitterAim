import time
import win32api
import keyboard

# only jitter while ads
state_left = win32api.GetKeyState(0x01)  # leftButton Up = 0 or 1; Down = -127 or -128
state_right = win32api.GetKeyState(0x02)  # rightButton Up = 0 or 1; Down = -127 or -128
flat_toggle = '6'

last_state_flat = False
enabled_flat = False
alternate = True  # Initialize the 'alternate' variable globally

def flat_line(s_left, s_right, x):
    global alternate  # Declare 'alternate' as a global variable
    if x != s_right:  # jitter aim while ads
        while x < 0:
            a = win32api.GetKeyState(0x01)  # always check the state of left click
            if a != s_left:
                if a < 0:
                    win32api.mouse_event(0x01, 3, 0)  # move right (+ve)
                    time.sleep(0.0001)
                    move_up = -5 if alternate else -4
                    win32api.mouse_event(0x01, 0, move_up)  # alternate move up (-ve)
                    time.sleep(0.0001)
                    win32api.mouse_event(0x01, 0, 3)  # move down (+ve)
                    time.sleep(0.0001)
                    win32api.mouse_event(0x01, -3, 0)  # move left (-ve)
                    time.sleep(0.0001)

                    win32api.mouse_event(0x01, 0, 3)  # move down (+ve)
                    time.sleep(0.0001)

                    win32api.mouse_event(0x01, -3, 0)  # move left (-ve)
                    time.sleep(0.0001)
                    win32api.mouse_event(0x01, 0, 3)  # move down (+ve)
                    time.sleep(0.0001)
                    win32api.mouse_event(0x01, 0, move_up)  # alternate move up (-ve)
                    time.sleep(0.0001)
                    win32api.mouse_event(0x01, 3, 0)  # move right (+ve)
                    time.sleep(0.0001)

                    alternate = not alternate  # Toggle alternate

            x = win32api.GetKeyState(0x02)  # check right button state

# main part
# print for startup
print("Anti-recoil script started!")

while True:
    b = win32api.GetKeyState(0x02)

    # check state changed for toggle button
    key_down_flat = keyboard.is_pressed(flat_toggle)

    if key_down_flat != last_state_flat:
        last_state_flat = key_down_flat
        if last_state_flat:
            enabled_flat = not enabled_flat
            if enabled_flat:
                print("Anti-recoil flat line ON")
            else:
                print("Anti-recoil flat line OFF")

    if enabled_flat:
        flat_line(state_left, state_right, b)

    time.sleep(0.001)
