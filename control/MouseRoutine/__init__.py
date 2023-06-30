import json
import time
import pyautogui
from typing import TypeVar, List, Tuple
from pynput import mouse
from control.MouseRoutine.MoveClickWait import MoveClickWait

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

    def load(self, path: str):
        with open(f"routines/{path}", "r") as file:
            routine = json.load(file)
        for mcw in routine:
            print(routine[mcw])
            self._routine.append(MoveClickWait(int(routine[mcw]["x_pos"]),
                                               int(routine[mcw]["y_pos"]),
                                               int(routine[mcw]["wait_time"])))

    def save(self, path: str):
        routine = {}

        for k,v in enumerate(self._routine):
            routine.update({f"{k}": {"x_pos": f"{v._x}",
                                    "y_pos": f"{v._y}",
                                    "wait_time": f"{v._wait}"}})

        with open(f"routines/{path}", "w") as file:
            json.dump(routine, file)
