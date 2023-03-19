import pyautogui
import random
import time
from PIL import ImageGrab

TARGET_COLOR_1 = (56, 56, 57, 255)
TARGET_COLOR_3 = (55, 120, 224, 255)
TOLERANCE = 5
MAX_ITERATIONS = 20

def move_mouse(x, y, delay=100):
    pyautogui.moveTo(x, y, duration=delay / 1000 * random_multiplier())

def left_click(delay=140):  # Reduced sleep amount by 30%
    pyautogui.click()
    time.sleep(delay / 1000 * random_multiplier())

def scroll_mouse(amount):
    pyautogui.scroll(amount)

def random_multiplier():
    return random.uniform(1, 1.33)

def get_user_input():

    coords = []
    for i in range(2):
        x = int(input(f"Enter x-coordinate of button {i + 1}:"))
        y = int(input(f"Enter y-coordinate of button {i + 1}:"))
        coords.append((x, y))

    # Calculate the second coordinate based on the first
    coords.insert(1, (coords[0][0] - 100, coords[0][1] + 6))

    iterations = int(input("Enter the number of iterations:\n"))

    return coords, iterations

def is_color_close(color1, color2, tolerance):
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(color1, color2))

def get_mouse_color():
    x, y = pyautogui.position()
    screen = ImageGrab.grab()
    return screen.getpixel((x, y))

def main():
    try:
        click_coords, iterations = get_user_input()

        for _ in range(iterations):
            # First button
            move_mouse(*click_coords[0])
            current_color_1 = get_mouse_color()
            counter = 0
            while not is_color_close(current_color_1, TARGET_COLOR_1, TOLERANCE):
                if counter >= MAX_ITERATIONS:
                    print("Reached maximum scroll iterations, exiting.")
                    exit()
                scroll_mouse(-1)
                time.sleep(0.17)
                current_color_1 = get_mouse_color()
                if is_color_close(current_color_1, (104, 104, 106, 255), TOLERANCE):
                    break
                print(current_color_1)
                counter += 1
            left_click()

            # Second button
            move_mouse(*click_coords[1])
            left_click()

            # Third button
            move_mouse(*click_coords[2])
            current_color_3 = get_mouse_color()
            if is_color_close(current_color_3, TARGET_COLOR_3, TOLERANCE):
                left_click()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
    