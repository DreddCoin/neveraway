import pyautogui
import time
t = 5
offset = 400
while True:
    pyautogui.move(offset,0)
    time.sleep(t)
    pyautogui.move(0,-offset)
    time.sleep(t)
    pyautogui.move(-offset,0)
    time.sleep(t)
    pyautogui.move(0,offset)
    time.sleep(t)
