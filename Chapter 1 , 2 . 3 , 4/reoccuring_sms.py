import pyautogui
import time
time.sleep(5)

for i in range(1,50):
    pyautogui.typewrite(f"I am so sorry ")
    time.sleep(4)
    pyautogui.press("enter")

