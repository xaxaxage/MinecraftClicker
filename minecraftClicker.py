import keyboard
import pyautogui as  p
from time import sleep

def f():
    while True:
        sleep(0.5)
        if keyboard.is_pressed("t"):
            print('xxx')
            f2()

def f2():
    while True:
        p.click()
        if keyboard.is_pressed("r"):
            print('xxx2')
            f()

f()

