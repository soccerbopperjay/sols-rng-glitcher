from pynput.mouse import Listener
import pyautogui

# Function to capture the mouse position when clicked
def on_click(x, y, button, pressed):
    if pressed:  # Check if the mouse button was pressed
        print(f"Clicked at: ({x}, {y})")

# Setting up the listener for mouse events
with Listener(on_click=on_click) as listener:
    listener.join()
