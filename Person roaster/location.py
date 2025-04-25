import pyautogui
import keyboard
import time

is_paused = False  # Flag to control pausing
try:
    while True:
        # Check for pause key (Alt+P)
        if keyboard.is_pressed('alt+p'):  # Pause the script
            is_paused = True
            print("\nPaused. Press Alt+O to resume.", end="\r")
            time.sleep(1)  # Prevent rapid toggling

        # Check for resume key (Alt+O)
        if keyboard.is_pressed('alt+o'):  # Resume the script
            is_paused = False
            print("\nResumed. Press Alt+P to pause.", end="\r")
            time.sleep(1)  # Prevent rapid toggling

        if not is_paused:
            x, y = pyautogui.position()  # Get current mouse position
            rgb = pyautogui.pixel(x, y)  # Get RGB color at the current mouse position
            print(f"Mouse Position: (x={x}, y={y}) RGB: {rgb}", end="\r")  # Print position and RGB
            time.sleep(0.1)  # Reduce output frequency
except KeyboardInterrupt:
    print("\nStopped tracking.")
