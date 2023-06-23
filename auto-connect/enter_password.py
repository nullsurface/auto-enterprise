import pyautogui
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--mac-password', required=True)
args = parser.parse_args()
pyautogui.write(args.mac_password)
pyautogui.press("enter")
