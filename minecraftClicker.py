import keyboard
import pyautogui as  p
from time import sleep

def f():
    while True:
        sleep(0.5)
        if keyboard.is_pressed("t"):
            f2()
        
        if keyboard.is_pressed("f"):
            f3()  

def f2():
    while True:
        p.click(clicks=5, interval=0.03)
        if keyboard.is_pressed("r"):
            f()

def f3():
    while True:
        p.click(button="right", clicks=5, interval=0.03)
        if keyboard.is_pressed("r"):
            f()

f()

