import pyautogui
import pygame
import time
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for image files and settings
TEMPLATE_IMAGE = 'poll_template.png'
YES_BUTTON_IMAGE = 'yes_button.png'
SUBMIT_BUTTON_IMAGE = 'submit_button.png'
ALERT_SOUND_PATH = r'C:\Users\orbar\Desktop\zoom_survey_alert\alert_sound.mp3'
CONFIDENCE = 0.8
CHECK_INTERVAL = 5  # seconds
ALERT_DURATION = 20  # seconds



def play_sound_for_duration(sound_path, duration=ALERT_DURATION):
    """Play the alert sound for the specified duration."""
    try:
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()
        end_time = time.time() + duration
        while time.time() < end_time:
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play()  # Restart if it stops unexpectedly
            time.sleep(0.6)  # Sleep briefly to avoid high CPU usage
        pygame.mixer.music.stop()
    except pygame.error as e:
        logging.error(f"Error during sound playback: {e}")
    except Exception as e:
        logging.error(f"Unexpected error in play_sound_for_duration: {type(e).__name__}")

def move_and_click(image, confidence=CONFIDENCE):
    """Locate the image on the screen, move to it, and click."""
    try:
        location = pyautogui.locateCenterOnScreen(image, confidence=confidence)
        if location:
            x, y = location
            logging.info(f"Moving to {image} at x: {x}, y: {y}")
            pyautogui.moveTo(x, y, duration=0.5)  # Move slowly to the target
            time.sleep(1)  # Pause to see the cursor position
            pyautogui.click(x, y)
        else:
            logging.warning(f"Image '{image}' not found on the screen with confidence {confidence}.")
    except pyautogui.ImageNotFoundException:
        logging.error(f"Image '{image}' not found on the screen.")
    except Exception as e:
        logging.error(f"Unexpected error in move_and_click: {type(e).__name__}")

def check_template_and_proceed():
    """Check for the presence of the template image and perform actions."""
    try:
        if pyautogui.locateOnScreen(TEMPLATE_IMAGE, confidence=CONFIDENCE) is not None:
            logging.info("Template detected on screen. Playing alert sound and proceeding with clicks.")
            
            # Play the alert
            play_sound_for_duration(ALERT_SOUND_PATH, 5)
            
            # Perform button clicks
            move_and_click(YES_BUTTON_IMAGE)
            move_and_click(SUBMIT_BUTTON_IMAGE)

            # Resume sound
            play_sound_for_duration(ALERT_SOUND_PATH)

        else:
            logging.warning("Template not detected. Retrying...")
    except pyautogui.ImageNotFoundException:
        logging.error("Template image not found, retrying...")
    except Exception as e:
        logging.error(f"Unexpected error in check_template_and_proceed: {type(e).__name__}")

def main():
    # Initialize sound mixer
    pygame.mixer.init()

    while True:
        try:
            check_template_and_proceed()
        except Exception as e:
            logging.error(f"Error in main loop: {type(e).__name__}")
        
        time.sleep(CHECK_INTERVAL)

if __name__ == '__main__':
    main()
