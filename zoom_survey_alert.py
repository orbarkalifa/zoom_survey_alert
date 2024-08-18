import cv2
import numpy as np
import pyautogui
import pygame
import time

# Path to the image template and alert sound file
TEMPLATE_PATH = r'C:\Users\orbar\Desktop\zoom_survey_alert\poll_template.png'
ALERT_SOUND_PATH = r'C:\Users\orbar\Desktop\zoom_survey_alert\alert_sound.mp3'

# Initialize pygame mixer for sound playback
pygame.mixer.init()

def detect_poll():
    # Load the template image
    template = cv2.imread(TEMPLATE_PATH, cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]

    # Capture a screenshot and convert to grayscale
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)

    # Perform template matching
    res = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # Debugging: Print confidence value
    print(f"Template matching confidence: {max_val}")

    # Set a threshold for detection
    threshold = 0.8
    if max_val >= threshold:
        print("Poll/quiz detected!")
        return True
    else:
        print("Poll/quiz not detected.")
        return False

def play_sound_repeatedly_for_20_seconds():
    start_time = time.time()
    while time.time() - start_time < 20:  # Play for 20 seconds
        pygame.mixer.music.load(ALERT_SOUND_PATH)
        pygame.mixer.music.play()
        time.sleep(1.5)  # Adjust this based on sound length if needed

def main():
    while True:
        if detect_poll():
            play_sound_repeatedly_for_20_seconds()
        
        # Wait for a while before checking again
        time.sleep(10)

if __name__ == '__main__':
    main()
