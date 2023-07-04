import os
import time
import pyautogui

APPLY_PROFILE_AUTOMATER = "auto-connect/ApplyProfile.app"

class MacAutoEnt:
    def __init__(self, ssid: str,
                 radius_username: str,
                 radius_password: str,
                 profile_path: str,
                 macos_password):
        self._ssid = ssid
        self._profile_path = profile_path
        self._radius_username = radius_username
        self._radius_password = radius_password
        self._macos_password = macos_password

    def connect(self):
        # Install the profile
        os.system(f"open ./{self._profile_path}")

        # Run apply profile macOS Automater Script
        os.system(f"open ./{APPLY_PROFILE_AUTOMATER}")

        # scroll then click on profile
        pyautogui.move(300, 0)
        pyautogui.scroll(-5)

        # Sleep to allow apply profile to run
        time.sleep(10)

        # Enter the macOS user password
        pyautogui.write(self._macos_password)
        pyautogui.press("enter")
