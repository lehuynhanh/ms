import pyautogui as pyag
import time
from datetime import datetime,timedelta
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
import pyttsx3
from PIL import Image

      
engine = pyttsx3.init()
ms = pyag.getWindowsWithTitle('Dream MS')[0]
ms.moveTo(0,0)
ms.activate()

stop_tpx = 10

def detect_same_map(map_name):
    print('Trying to detect' + map_name)
    try:
        if pyag.locateOnScreen(map_name +".jpg",region=(10,50,250,160),confidence=0.8):
            return map_name
        else:
            return ''
    except Exception as e:
        return ''
        
        
def get_yellow():
    try:
        return pyag.locateOnScreen(r"yellow.jpg",region=(10,50,250,160),confidence=0.8)
    except Exception as e:
        return ''

def tp(direction):
    pressKey(direction)
    time.sleep(0.5)
    press('X',0.4)
    releaseKey(direction)

def first_map_walk():
    # print('First map walk')
    time.sleep(40)
    while detect_same_map('otwps') == 'otwps':
        # print('Detected first map')
        try:
            yellow = pyag.locateOnScreen(r"yellow.jpg",region=(10,50,250,160),confidence=0.8)
            if yellow == None:
                print('No yellow found; walking right')
                press('LEFT',1)
            if yellow.left < 232-stop_tpx:
                tp('RIGHT')
            elif yellow.left < 232:
                pressKey('UP')
                press('RIGHT',1)
                releaseKey('UP')
            elif yellow.left >= 233:
                pressKey('UP')
                press('LEFT',0.15)
                releaseKey('UP')
            elif yellow.left == 232:
                pressKey('UP')
                press('ALT',0.2)
                press('X',0.4)
                releaseKey('UP')
            elif yellow.left == 232 and yellow.top == 172:
                press('UP',0.5)
                break
        except Exception as  e:
            press('LEFT',1)

    

def second_map_walk():
    print('Second map walk')
    while detect_same_map('tthots') == 'tthots':
        # print('Detected 2nd map')
        try:
            yellow = pyag.locateOnScreen(r"yellow.jpg",region=(10,50,250,160),confidence=0.8)
            if yellow == None:
                print('No yellow found; walking right')
                # press('LEFT',1)
                press('LEFT',1)
            if yellow.left < 167-stop_tpx:
                tp('RIGHT')
            elif yellow.left < 167:
                pressKey('UP')
                press('RIGHT',1)
                releaseKey('UP')
            elif yellow.left >= 168:
                pressKey('UP')
                press('LEFT',0.15)
                releaseKey('UP')
            elif yellow.left == 167:
                press('UP',0.5)
                break
        except Exception as  e:
            press('LEFT',1)

            
def third_map_walk():
    #156,167
    while detect_same_map('ttd1') == 'ttd1':
        # print('Detected ttd1 map')
        try:
            yellow = pyag.locateOnScreen(r"yellow.jpg",region=(10,50,250,160),confidence=0.8)
            if yellow == None:
                print('No yellow found; walking right')
                press('LEFT',1)
            elif yellow.left < 156-stop_tpx:
                tp('RIGHT')
            elif yellow.left < 156:
                press('RIGHT',1)
            elif yellow.left >= 157:
                pressKey('UP')
                press('LEFT',0.15)
                releaseKey('UP')
            elif yellow.left == 156:
                press('UP',0.5)
                break
        except Exception as  e:            
            press('LEFT',1)

            
def fourth_map_walk():
    #152,167
    while detect_same_map('ttd2') == 'ttd2':
        # print('Detected ttd2 map')
        try:
            yellow = pyag.locateOnScreen(r"yellow.jpg",region=(10,50,250,160),confidence=0.8)
            if yellow == None:
                print('No yellow found; walking right')
                press('LEFT',1)

            elif yellow.left < 153-stop_tpx:
                tp('RIGHT')
            elif yellow.left < 153:
                press('RIGHT',1)
            elif yellow.left >= 154:
                pressKey('UP')
                press('LEFT',0.15)
                releaseKey('UP')
            elif yellow.left == 153:
                press('UP',0.5)
                break
        except Exception as  e:
            press('LEFT',1)
            
            
def fifth_map_walk():
    #131,155
    while detect_same_map('elimpir') == 'elimpir':
        # print('Detected elimpir map')
        try:
            yellow = pyag.locateOnScreen(r"yellow.jpg",region=(10,50,250,160),confidence=0.8)
            if yellow == None:
                print('No yellow found; walking right')
                press('LEFT',1)
            elif yellow.left < 131-stop_tpx:
                tp('RIGHT')
            elif yellow.left < 131:
                pressKey('UP')
                press('RIGHT',1)
                releaseKey('UP')
            elif yellow.left >= 132:
                pressKey('UP')
                press('LEFT',0.15)
                releaseKey('UP')
            elif yellow.left == 131:
                press('UP',0.5)
                break
        except Exception as  e:            
            press('RIGHT',1)
            
            

def detect_map():
    try:
        if pyag.locateOnScreen(r"otwps.jpg",region=(10,50,250,160),confidence=0.8):
            return 'otwps'
    except Exception as e:
        pass
    try:
        if pyag.locateOnScreen(r"tthots.jpg",region=(10,50,250,160),confidence=0.8):
            return 'tthots'
    except Exception as e:
        pass
    try:
        if pyag.locateOnScreen(r"ttd1.jpg",region=(10,50,250,160),confidence=0.98):
            return 'ttd1'
    except Exception as e:
        pass
    try:
        if pyag.locateOnScreen(r"ttd2.jpg",region=(10,50,250,160),confidence=0.98):
            return 'ttd2'
    except Exception as e:
        pass
    try:
        if pyag.locateOnScreen(r"elimpir.jpg",region=(10,50,250,160),confidence=0.8):
            return 'elimpir'
    except Exception as e:
        pass
    try:
        if pyag.locateOnScreen(r"ppqboss_rm.jpg",region=(10,50,250,160),confidence=0.8):
            return 'ppqboss_rm'
    except Exception as e:
        pass

magicguard = datetime.now () - timedelta(seconds=300)
petfood = datetime.now()
while True:
    now = datetime.now()
    if now > magicguard + timedelta(seconds=300):
        ('Buffing magic guard')
        press('6')
        magicguard = datetime.now()
    if now > petfood + timedelta(seconds=300):
        ('Petfood')
        press('0')
        petfood = datetime.now()
    map = detect_map()
    if map == 'otwps':
        first_map_walk()
    elif map == 'tthots':
        second_map_walk()
    elif map == 'ttd1':
        third_map_walk()
    elif map == 'ttd2':
        fourth_map_walk()
    elif map == 'elimpir':
        fifth_map_walk()
    elif map == 'ppqboss_rm':
        time.sleep(10)
    elif map == '':
        time.sleep(1)
        
        
        
        
        
        
        
        
        
        
        
        
