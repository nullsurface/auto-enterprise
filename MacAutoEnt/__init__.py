import os
import time
import pyautogui

APPLY_PROFILE_AUTOMATOR = "automator/ApplyProfile.app"
CLICK_INSTALL_AUTOMATOR = "automator/ClickInstall.app"

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
        os.system(f"open ./{APPLY_PROFILE_AUTOMATOR}")

        # Sleep to allow apply profile to run
        print("Waiting for automator to finish")
        for i in range(6):
            print(i)
            time.sleep(1)

        # scroll then click on profile
        pyautogui.move(300, 0)
        pyautogui.scroll(-100)
        pyautogui.move(0, 200)
        pyautogui.click()
        pyautogui.move(0, -625)
        print("Waiting for profiles to load")
        for i in range(2):
            print(i)
            time.sleep(1)
        pyautogui.click()
        pyautogui.press("enter")
        pyautogui.move(0, 580)
        pyautogui.move(-200, 0)
        print("Waiting for install page to load")
        time.sleep(1)
        pyautogui.click()
        pyautogui.move(200, 0)
        pyautogui.move(0, -200)
        pyautogui.click()
        print("Waiting for install page to load")
        time.sleep(1)
        pyautogui.click()

	# Click Install Automator
        os.system(f"open ./{CLICK_INSTALL_AUTOMATOR}")

        # Sleep to allow apply profile to run
        print("Waiting for automator to finish")
        for i in range(4):
            print(i)
            time.sleep(1)

        # Enter the macOS user password
        pyautogui.write(self._macos_password)
        pyautogui.press("enter")
