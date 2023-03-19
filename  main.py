import pyautogui
import random
import time
from PIL import ImageGrab

TARGET_COLOR_1 = (56, 56, 57, 255)
TARGET_COLOR_3 = (55, 120, 224, 255)
TOLERANCE = 5
MAX_ITERATIONS = 20


def move_mouse(x, y, delay=1):
    pyautogui.moveTo(x, y)


def left_click(delay=40):
    pyautogui.click()
    time.sleep(delay / 1000 * random_multiplier())


def move_mouse_up(pixels):
    pyautogui.move(0, -pixels)


def scroll_mouse(amount):
    pyautogui.scroll(amount)


def random_multiplier():
    return random.uniform(1, 1.33)


def get_user_input():
    coords = []
    for i in range(2):
        x = int(input(f"Enter x-coordinate of button {i + 1}: "))
        y = int(input(f"Enter y-coordinate of button {i + 1}: "))
        coords.append((x, y))

    # Calculate the second coordinate based on the first
    coords.insert(1, (coords[0][0] - 100, coords[0][1]))

    # Get user input for the third and fourth coordinates
    input_third_coord = input("Would you like to input the third coordinate? (y/n): ")
    if input_third_coord.lower() == "y":
        x = int(input("Enter x-coordinate of button 3: "))
        y = int(input("Enter y-coordinate of button 3: "))
        coords.append((x, y))
    else:
        coords.append(None)

    input_fourth_coord = input("Would you like to input the fourth coordinate? (y/n): ")
    if input_fourth_coord.lower() == "y":
        x = int(input("Enter x-coordinate of button 4: "))
        y = int(input("Enter y-coordinate of button 4: "))
        coords.append((x, y))
    else:
        coords.append(None)

    iterations = int(input("Enter the number of iterations: "))

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
            while not is_color_close(current_color_1, TARGET_COLOR_1, 0):
                if counter >= MAX_ITERATIONS:
                    print("Reached maximum scroll iterations, exiting.")
                    exit()
                scroll_mouse(-1)
                time.sleep(0.17)
                current_color_1 = get_mouse_color()
                if is_color_close(current_color_1, (104, 104, 106, 255), TOLERANCE) or is_color_close(current_color_1, (
                227, 228, 232, 255), 50):
                    break
                print(current_color_1)
                counter += 1
            left_click()

            # Second button
            move_mouse(*click_coords[1])
            left_click()

            # Third button
            if click_coords[2] is not None:
                move_mouse(*click_coords[2])
                current_color_3 = get_mouse_color()
                if is_color_close(current_color_3, TARGET_COLOR_3, TOLERANCE) or is_color_close(current_color_3, (163, 193, 241, 255), 10):
                    left_click()

            # Fourth button
            if click_coords[3] is not None:
                move_mouse(click_coords[3][0], click_coords[3][1])
                current_color_4 = get_mouse_color()
                if is_color_close(current_color_4, TARGET_COLOR_3, TOLERANCE) or is_color_close(current_color_4,
                                                                                                (163, 193, 241, 255), 10):
                    left_click()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()