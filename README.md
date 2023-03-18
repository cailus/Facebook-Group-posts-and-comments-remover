# Facebook Group Post Remover

This Python script is designed to help you remove comments and posts from groups in your Facebook activity log in an automated fashion.

## Prerequisites

- Python 3.x installed
- Install `pyautogui` library by running the following command:
    ```
    pip install pyautogui
    ```

## Files

1. `main.py`: The main script that performs the mouse movements and clicks.
2. `checkCoordinate.py`: A script to help you find the coordinates of the two buttons you need to click.

## How to use

1. Go to Facebook and navigate to **Settings & Privacy**.
2. Click on **Activity Log**.
3. Select the **Group posts and comments** filter from the left sidebar.
4. Locate the following buttons on the page: the "Action options" button (3-dot button) and the "Delete" menu item.
5. Run the `checkCoordinate.py` script to see the mouse coordinates in real-time:
    ```
    python checkCoordinate.py
    ```
6. Move your mouse over the "Action options" button and note down the coordinates (x and y).
7. Move your mouse over the "Delete" menu item and note down the coordinates (x and y).
8. Run the `main.py` script:
    ```
    python main.py
    ```
9. When prompted, enter the coordinates for both buttons and the number of iterations (number of times you want the script to perform the clicks).
10. The script will automatically move the mouse and click on the necessary buttons to remove comments and posts from groups in your activity log, based on the number of iterations you provided.

## Troubleshooting

If the script doesn't work as expected, make sure you have the correct coordinates for the two buttons. You can use the `checkCoordinate.py` script to double-check the coordinates.

## Notes

This script is not affiliated with or endorsed by Facebook. Use it at your own risk. The code is provided "as is" with no guarantees or warranties. Always double-check the button coordinates before running the script, as changes to Facebook's layout or code may affect its functionality.
