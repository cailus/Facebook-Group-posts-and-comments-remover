import time
import pyautogui
from PIL import ImageGrab

def get_mouse_color():
    x, y = pyautogui.position()
    screen = ImageGrab.grab()
    return screen.getpixel((x, y))

while True:
    rgb = get_mouse_color()
    print(f"RGB: {rgb}")
    time.sleep(2)
    