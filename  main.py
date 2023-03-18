import pyautogui
import random
import time
import tkinter as tk
from tkinter import simpledialog

def move_mouse(x, y, delay=100):
    """Moves the mouse to the specified coordinates with a delay."""
    pyautogui.moveTo(x, y)
    time.sleep(delay / 1000 * random_multiplier())

def left_click(delay=200):
    """Performs a left click with a delay."""
    pyautogui.click()
    time.sleep(delay / 1000 * random_multiplier())

def random_multiplier():
    """Generates a random multiplier between 1 and 1.33."""
    return random.uniform(1, 1.33)

def get_user_input():
    """Prompts the user for the coordinates of the two clicks and the number of iterations."""
    root = tk.Tk()
    root.withdraw()

    message = "Run the checkCoordinate.py to see coordinates."

    x1 = simpledialog.askinteger("Input", f"Enter x-coordinate of the first button:\n{message}")
    y1 = simpledialog.askinteger("Input", f"Enter y-coordinate of the first button:\n{message}")
    x2 = simpledialog.askinteger("Input", f"Enter x-coordinate of the second button:\n{message}")
    y2 = simpledialog.askinteger("Input", f"Enter y-coordinate of the second button:\n{message}")
    iterations = simpledialog.askinteger("Input", "Enter the number of iterations:")

    return (x1, y1), (x2, y2), iterations

def main():
    first_click_coords, second_click_coords, iterations = get_user_input()

    # Perform the loop n times, where n is the number of iterations provided by the user
    for _ in range(iterations):
        move_mouse(*first_click_coords)
        left_click()
        move_mouse(*second_click_coords)
        left_click()

if __name__ == '__main__':
    main()
    