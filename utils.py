import pyautogui as py
import time

def locate_image(file_name):
    try:
        return py.locateCenterOnScreen("img/" + file_name, confidence=0.9)
    except Exception as e:
        print('-- image not found')
        return None

def locate_image_strong(file_name):
    try:
        return py.locateCenterOnScreen("img/" + file_name)
    except Exception as e:
        return None