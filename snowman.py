import pyautogui as pyag
import time
from datetime import datetime,timedelta
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
import pyttsx3
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'c:\\Program Files\\Tesseract-OCR\\tesseract.exe'

print(pytesseract.image_to_string(Image.open(r'map.jpg')))
      
engine = pyttsx3.init()
ms = pyag.getWindowsWithTitle('Dream MS')[0]
ms.moveTo(0,0)
ms.activate()

yellow_path = r"C:\\Users\\Michael\\Desktop\\MapleStory\\yellow.jpg"
#exit
#pyag.screenshot('snowman.jpg',region=(10,50,140,20)).show()
### check maps
### if map =

def start_pq():
    time.sleep(2) #debug
    press('LEFT',0.15)
    time.sleep(0.1)
    press('ALT',0.2)
    press('X',0.2)
    press('Y',0.2)
    time.sleep(0.1)
    press('Y',0.2)
    time.sleep(0.3)
    press('ALT',0.2)
    press('X',0.2)

def attack():
    try:
        ds_loc = pyag.locateOnScreen(ds_img,region=(900,49,120,30),confidence=0.7)
        if ds_loc is None:
            time.sleep(0.3)
            press('T',0.3)
    except Exception as e:
        print(e)
    try:
        eyes = len(list(pyag.locateAllOnScreen('eyes.jpg',confidence=0.8)))
        stirges = len(list(pyag.locateAllOnScreen('stirges.jpg',confidence=0.8)))
        ghosts = len(list(pyag.locateAllOnScreen('ghosts.jpg',confidence=0.8)))
        if eyes+stirges+ghosts > 2:
            time.sleep(0.8)
            press('A',0.3)
            time.sleep(0.5)
            press('A',0.3)
            time.sleep(0.5)
            press('A',0.3)
    except Exception as e:
        print(e)


def check_map():
    #try happyville, snowman, exit
    try:
        happyville = pyag.locateOnScreen('happyville.jpg',region=(0,0,400,400),confidence=0.9)
        if happyville is not None:
            return 'happyville'
    except:
        pass
    try:
        snowman = pyag.locateOnScreen('snowman.jpg',region=(0,0,400,400),confidence=0.9)
        if snowman is not None:
            return 'snowman'
    except:
        pass
    try:
        exit = pyag.locateOnScreen('exit.jpg',region=(0,0,400,400),confidence=0.9)
        if exit is not None:
            return 'exit'
    except:
        pass


def buff():
    time.sleep(0.8)
    press('6',0.4)
    time.sleep(0.3)
    press('6',0.4)
    time.sleep(0.3)
    press('7',0.3)
    time.sleep(0.3)
    press('7',0.3)
    time.sleep(0.8)
    press('8',0.5)
    time.sleep(0.8)
    press('9',0.5)
    time.sleep(0.8)



def exit_pq():
    while check_map() == 'snowman':
        snowman_head = pyag.locateCenterOnScreen('snowman_head.png',confidence=0.8)
        try:
            pyag.doubleClick(snowman_head)
            press('LEFT',0.5)
        except Exception as e:
            print(e)
        press('Y',0.3)


def click_fairy():
    if map == 'snowman':
        print('Finding fairy at snowman')
        try:
            fairyup = pyag.locateCenterOnScreen('fairyup.jpg', confidence=0.9)
            fairydown = pyag.locateCenterOnScreen('fairydown.jpg', confidence=0.9)
            if fairyup is not None:
                pyag.doubleClick(fairyup)
                time.sleep(0.8)
                pyag.click(528,412)
                time.sleep(0.3)
            if fairydown is not None:
                pyag.doubleClick(fairydown)
                time.sleep(0.8)
                pyag.click(528,412)
                time.sleep(0.3)
            if (fairydown is not None or fairyup is not None) and map == 'snowman':
                try:
                    print('looking for defeat')
                    defeat = pyag.locateCenterOnScreen('defeat.jpg',confidence=0.8)
                    if defeat is not None:
                        press('Y',0.3)
                        time.sleep(0.3)
                        press('Y',0.3)
                        print('Exit PQ')
                        exit_pq()
                except Exception as e:
                    print(e)
            if map == 'snowman':
                press('Y',0.3)
            last_fairy = now
        except Exception as e:
            print(e)
    if map == 'happyville':
        print('Finding fairy at happyville')
        fairyup = pyag.locateCenterOnScreen('fairyup.jpg', confidence=0.9)
        fairydown = pyag.locateCenterOnScreen('fairydown.jpg', confidence=0.9)
        if fairyup is not None:
            pyag.doubleClick(fairyup)
            time.sleep(0.8)
            pyag.click(528,412)
            time.sleep(0.3)
        if fairydown is not None:
            pyag.doubleClick(fairydown)
            time.sleep(0.8)
            pyag.click(528,412)
            time.sleep(0.3)
        try:
            party_here = pyag.locateOnScreen('2of2.jpg',region=(570,700,300,50),confidence=0.95)
            if party_here is not None:
                pyag.doubleClick(512,442)
                print('Found our party')
                press('ENTER',0.3)
        except Exception as e:
            print(e)


### if map = Snow Man's Land
yellow = pyag.locateOnScreen(yellow_path,region=(10,50,100,150),confidence=0.7)
ds_img = r"C:\\Users\\Michael\\Desktop\\MapleStory\\ds.jpg"
now = datetime.now()
pet_food = now
### if map = Exit after snowman's land
started_pq = False
boss = False
last_fairy = now - timedelta(seconds=4)

while True:
    now = datetime.now()
    map = check_map()
    # print(map)
    if now > (pet_food + timedelta(seconds=500)):
        print('trying pet_food')
        press('U')
        pet_food = now
    if map == 'happyville':
        started_pq = False
    if map == 'snowman' and started_pq == False:
        pyag.click(528,412)
        buff() #haste
        time.sleep(0.4)
        press('T',0.3)
        time.sleep(0.1)
        start_pq()
        started_pq = True
    if map == 'snowman' and started_pq == True:
        attack()
    try:
        boss = pyag.locateOnScreen('boss.jpg',confidence=0.8)
        counter = 0
        while boss is not None:
            press('A',0.3)
            time.sleep(0.1)
            boss = pyag.locateOnScreen('boss.jpg',confidence=0.8)
            if counter > 8:
                press('PGUP',0.3)
    except Exception as e:
        print(e)
    # print(boss)
    # print(last_fairy)
    if now > last_fairy + timedelta(seconds=5):
        last_fairy = now
        click_fairy()
    if map == 'exit':
        time.sleep(1)
        pressKey('UP')
        pressKey('RIGHT')
        time.sleep(2.8)
        releaseKey('RIGHT')
        time.sleep(0.1)
        releaseKey('UP')
        time.sleep(0.5)

