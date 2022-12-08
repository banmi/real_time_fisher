import time

import pyautogui

#wow window should start at 0,0

class Catch:
    def try_catch(points):
        global position

        if points:
            position = points

        else:
            pyautogui.moveTo(position[0])
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(2)
            pyautogui.press('1')