import cv2
import numpy as np
import pyautogui
import pygame
import time

# Constants for file paths and settings
TEMPLATE_PATH = r'C:\Users\orbar\Desktop\zoom_survey_alert\poll_template.png'
ALERT_SOUND_PATH = r'C:\Users\orbar\Desktop\zoom_survey_alert\alert_sound.mp3'
DETECTION_THRESHOLD = 0.8
CHECK_INTERVAL = 5  # seconds
ALERT_DURATION = 20  # seconds
ALERT_REPEAT_INTERVAL = 1.5  # seconds

# Initialize pygame mixer for sound playback
pygame.mixer.init()

def load_template(template_path):
    """Load and return the template image in grayscale."""
    return cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)

def capture_screenshot():
    """Capture a screenshot and return it as a grayscale image."""
    screenshot = pyautogui.screenshot()
    screenshot_array = np.array(screenshot)
    return cv2.cvtColor(screenshot_array, cv2.COLOR_RGB2GRAY)

def is_poll_detected(template, screenshot_gray, threshold=DETECTION_THRESHOLD):
    """Perform template matching and return True if a match is found."""
    res = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(res)
    print(f"Template matching confidence: {max_val}")  # Debugging output
    return max_val >= threshold

def play_sound_for_duration(sound_path, duration=ALERT_DURATION, interval=ALERT_REPEAT_INTERVAL):
    """Play the alert sound repeatedly for the specified duration."""
    pygame.mixer.music.load(sound_path)
    end_time = time.time() + duration
    while time.time() < end_time:
        pygame.mixer.music.play()
        time.sleep(interval)

def main():
    template = load_template(TEMPLATE_PATH)
    
    while True:
        screenshot_gray = capture_screenshot()
        if is_poll_detected(template, screenshot_gray):
            play_sound_for_duration(ALERT_SOUND_PATH)
        
        time.sleep(CHECK_INTERVAL)

if __name__ == '__main__':
    main()
