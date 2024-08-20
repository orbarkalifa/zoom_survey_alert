import pyautogui
import time

def move_and_click(image, confidence=0.8):
    x, y = pyautogui.locateCenterOnScreen(image, confidence=confidence)
    if x is not None and y is not None:
        print(f"Moving to {image} at x: {x}, y: {y}")
        pyautogui.moveTo(x, y, duration=0.5)  # Move slowly to the target
        time.sleep(1)  # Pause to see the cursor position
        pyautogui.click(x, y)
    else:
        print(f"{image} not found on the screen")

move_and_click('yes_button.png')
move_and_click('submit_button.png')
