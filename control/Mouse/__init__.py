import time
import pyautogui
from typing import TypeVar, List, Tuple
from pynput import mouse
from MoveClickWait import MoveClickWait

class MouseRoutine():
    _routine: List[MoveClickWait]

    def __init__(self):
        self._routine = []

    def play(self):
        for mcw in self._routine:
            print(f"Clicking: ({mcw._x}, {mcw._y}), waiting: {mcw._y}")
            pyautogui.click(x=mcw._x, y=mcw._y)
            time.sleep(mcw._wait)

    def record(self):
        with mouse.Listener(on_click=self.record_pos) as listener:
            listener.join()

    def record_pos(self, x, y, button, pressed):
        if pressed:
            if button == mouse.Button.right:
                return False
            pos = pyautogui.position()
            self._routine.append(MoveClickWait(pos[0], pos[1], 2))
            print(f"Mouse clicked at ({x}, {y}) with button {button}")

def main():
    mouse = MouseRoutine()
    mouse.record()
    mouse.play()



if __name__ == "__main__":
    main()
