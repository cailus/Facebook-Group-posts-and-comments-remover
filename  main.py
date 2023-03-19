import pyautogui
import random
import time
import tkinter as tk
from tkinter import simpledialog
from PIL import ImageGrab

TARGET_COLOR_2 = (56, 56, 57, 255)
TARGET_COLOR_3 = (55, 120, 224, 255)
TOLERANCE = 10

def move_mouse(x, y, delay=100):
    pyautogui.moveTo(x, y, duration=delay / 1000 * random_multiplier())

def left_click(delay=200):
    pyautogui.click()
    time.sleep(delay / 1000 * random_multiplier())

def random_multiplier():
    return random.uniform(1, 1.33)

def get_user_input():
    root = tk.Tk()
    root.withdraw()

    message = "Run the checkCoordinate.py to see coordinates."

    coords = []
    for i in range(3):
        x = simpledialog.askinteger("Input", f"Enter x-coordinate of button {i + 1}:\n{message}")
        y = simpledialog.askinteger("Input", f"Enter y-coordinate of button {i + 1}:\n{message}")
        coords.append((x, y))

    iterations = simpledialog.askinteger("Input", "Enter the number of iterations:")

    return coords, iterations

def is_color_close(color1, color2, tolerance):
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(color1, color2))

def get_mouse_color():
    x, y = pyautogui.position()
    screen = ImageGrab.grab()
    return screen.getpixel((x, y))

def main():
    click_coords, iterations = get_user_input()

    for _ in range(iterations):
        # First button
        move_mouse(*click_coords[0])
        left_click()

        # Second button
        move_mouse(*click_coords[1])
        current_color_2 = get_mouse_color()
        if is_color_close(current_color_2, TARGET_COLOR_2, TOLERANCE):
            left_click()

        # Third button
        move_mouse(*click_coords[2])
        current_color_3 = get_mouse_color()
        if is_color_close(current_color_3, TARGET_COLOR_3, TOLERANCE):
            left_click()

if __name__ == '__main__':
    main()
    