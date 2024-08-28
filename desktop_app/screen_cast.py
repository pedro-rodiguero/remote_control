import pyautogui
from PIL import Image

def start_physical_cast(output_screen):
    # Implement the logic to cast to the selected physical screen
    while True:
        screen = pyautogui.screenshot()
        screen.show()

def stop_physical_cast():
    # Implement the logic to stop casting to a physical screen
    pass