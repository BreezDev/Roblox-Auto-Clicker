from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Listener
import time

mouse = MouseController()
running = True

def on_press(key):
    global running
    if hasattr(key, 'char') and key.char == 'x':
        running = False
        return False  # Stop the listener


def click_mouse():
    try:
        while running:
            mouse.click(Button.left)
            time.sleep(0.05)  # Adjust this value to change click speed
    except KeyboardInterrupt:
        pass


listener = Listener(on_press=on_press)
listener.start()

click_mouse()

listener.join()
