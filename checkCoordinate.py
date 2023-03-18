import pyautogui
import time

def get_mouse_coordinates():
    """Returns the current mouse coordinates (x, y)."""
    x, y = pyautogui.position()
    return x, y

def main():
    while True:
        x, y = get_mouse_coordinates()
        print(f"Mouse coordinates: x={x}, y={y}")
        time.sleep(2)

if __name__ == '__main__':
    main()
    