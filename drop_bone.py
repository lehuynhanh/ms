import pyautogui as pyag
import time
from datetime import datetime,timedelta
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
import pyttsx3
import sys
import os
import threading

engine = pyttsx3.init()
ms = pyag.getWindowsWithTitle('Dream MS')[0]
ms.moveTo(0,0)
ms.activate()
time.sleep(2)

def drop_skele():
    ms.activate()
    try:
        oldneckbone = pyag.locateCenterOnScreen('oldneckbone.jpg',confidence=0.90)
        pyag.click(oldneckbone)
        time.sleep(0.1)
        pyag.moveTo(400,400)
        pyag.click()
        time.sleep(0.1)
        press('ENTER')
    except: 
        pass



while 'Dream' in pyag.getActiveWindow().title:
    drop_skele()