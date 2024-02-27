import pyautogui as pyag
import time
from datetime import datetime,timedelta
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
import pyttsx3

engine = pyttsx3.init()
ms = pyag.getWindowsWithTitle('Dream MS')[0]
ms.moveTo(0,0)
ms.activate()

while True:
    press('Z',0.3)
    time.sleep(0.1)