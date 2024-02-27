import pyautogui as pyag
import time
from datetime import datetime,timedelta
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
import pyttsx3

engine = pyttsx3.init()
ms = pyag.getWindowsWithTitle('Dream MS')[0]
ms.moveTo(0,0)

def movement(direction):
    print('Jumping ' + direction)
    time.sleep(0.4)
    press(direction,0.3)
    press('ALT',0.2)
    time.sleep(0.1)
    press('X',0.2)


# def movement_reduced(direction):
#     print('Jumping ' + direction)
#     time.sleep(0.65)
#     press(direction,0.3)
#     press('ALT',0.2)
#     time.sleep(0.3)
#     press('X',0.2)


def attack(direction):
    pyag.press(direction)
    time.sleep(0.2)
    press('D',0.3)
    time.sleep(0.2)
    press('ALT',0.1)
    press('X',0.1)
    time.sleep(0.1)
    press('D',0.3)
    time.sleep(0.3)
    press('ALT',0.3)
    time.sleep(0.3)
    press('D')



def attack_no_move():
    time.sleep(0.2)
    press('D',0.5)
    time.sleep(0.2)
    press('D',0.3)
    time.sleep(0.82)


def buff():
    time.sleep(0.6)
    press('6',0.3)
    time.sleep(0.3)
    press('7',0.3)
    time.sleep(0.3)
    press('7',0.3)
    time.sleep(0.8)
    press('8',0.5)
    time.sleep(0.8)
    press('9',0.5)
    time.sleep(0.4)


def thorns():
    time.sleep(0.7)
    press('6',0.3)
    time.sleep(0.3)
    press('6',0.3)
    time.sleep(0.6)


def init_loot():
    #left 65 rope
    #top 148 top rope
    yellow = pyag.locateOnScreen(yellow_path,region=(10,50,200,200),confidence=0.8)
    #get on rope
    while True:
        try:
            yellow = pyag.locateOnScreen(yellow_path,region=(10,50,200,200),confidence=0.8)
            if yellow.top <= 148:
                press('UP',0.6)
                break
            if yellow.left < 65:
                movement('RIGHT')
                press('UP',0.8)
            if yellow.left > 65:
                movement('LEFT')
                press('UP',0.8)
            if yellow.left == 65:
                press('UP',0.8)
            if yellow == None:
                print('None found for yellow, loot loop')
                pyag.press('UP',1)
        except Exception as e:
            print(e)
    #loot right
    time.sleep(0.5)
    while True:
        try:
            yellow = pyag.locateOnScreen(yellow_path,region=(10,50,200,200),confidence=0.8)
            if yellow.left <= 101:
                press('RIGHT',0.3)
            else:
                break
        except Exception as e:
            print(e)
    time.sleep(0.3)
    press('LEFT',1)
    press('C',0.4)
    time.sleep(0.4)
    press('C',0.4)


def init_sell():
    #left 65 rope
    #top 148 top rope
    yellow = pyag.locateOnScreen(yellow_path,region=(10,50,200,200),confidence=0.8)
    #get on rope
    while True:
        try:
            yellow = pyag.locateOnScreen(yellow_path,region=(10,50,200,200),confidence=0.8)
            if yellow.top <= 157:
                if yellow.top <= 152:
                    press('DOWN',0.5)
                break
            if yellow.left < 65:
                movement('RIGHT')
                press('UP',0.8)
            if yellow.left > 65:
                movement('LEFT')
                press('UP',0.8)
            if yellow.left == 65:
                press('UP',0.3)
            if yellow == None:
                print('None found for yellow, loot loop')
                pyag.press('UP',1)
        except Exception as e:
            print(e)
    time.sleep(0.5)
    miu = None
    sell_all = None
    leave_store = None
    while miu is None:
        print('Finding Miu')
        try:
            miu = pyag.locateCenterOnScreen('miu.jpg',confidence=0.9)
        except Exception as e:
            try:
                inv_button = pyag.locateCenterOnScreen('inv_but.jpg',confidence=0.8)
                print('Found inv button')
                pyag.click(inv_button)
            except Exception as e:
                print(e)
            press('I',0.3)
    pyag.doubleClick(miu)
    time.sleep(1)
    print('Sell all time')
    while sell_all is None:
        try:
            sell_all = pyag.locateCenterOnScreen('sell_all.jpg',confidence=0.8)
        except Exception as e:
            engine.say('Cannot sell all')
            print(e)
    pyag.doubleClick(sell_all)
    time.sleep(1)
    press('ENTER',0.5)
    time.sleep(1)
    while leave_store is None:
        try:
            leave_store = pyag.locateCenterOnScreen('leave_store.jpg',confidence=0.9)
        except:
            engine.say('Cant leave store')
    pyag.click(leave_store)
    time.sleep(1)
    miu = None
    sell_all = None
    leave_store = None
    press('DOWN',2)


print('Starting in 2 seconds.. navigate to MS')
time.sleep(2)
last_buff = datetime.now() - timedelta(seconds=101)
last_thorns = datetime.now() - timedelta(seconds=61)
loot_mode = datetime.now()
pet_food = datetime.now()
now = datetime.now()
loot_counter = 0
yellow_path = r"C:\\Users\\Michael\\Desktop\\MapleStory\\yellow.jpg"
ds_img = r"C:\\Users\\Michael\\Desktop\\MapleStory\\ds.jpg"
# yellow = pyag.locateOnScreen(yellow_path,confidence=0.7)
# print(yellow.left)
# sc = pyag.screenshot('yellow.jpg',region=(69,158,8,8))
# buffs = pyag.screenshot('buffs.jpg',region=(800,49,20,20))
# ds = pyag.screenshot('ds.jpg',region=(993,49,20,20))
init_sell()
while True:
    now = datetime.now()
    print('Loot counter is at ' + str(loot_counter))
    if now > (last_buff + timedelta(seconds=150)):
        print('Buff attempted')
        last_buff = now
        buff()
    if now > (last_thorns + timedelta(seconds=150)):
        print('Thorns attempted')
        last_thorns = now
        thorns()
    if loot_counter >= 3:
        loot_counter = 0
        print('attempt sell')
        init_sell()
    if now > (loot_mode + timedelta(seconds=100)):
        print('trying loot')
        init_loot()
        loot_counter += 1
        loot_mode = now
    if now > (pet_food + timedelta(seconds=500)):
        print('trying pet_food')
        press('U')
        pet_food = now
    try:
        # yellow = pyag.locateOnScreen(yellow_path,confidence=0.8)
        yellow = pyag.locateOnScreen(yellow_path,region=(10,50,200,200),confidence=0.8)
        print(yellow)
        if yellow.left >= 88:
            attack('LEFT')
        else:
            attack('RIGHT')
        if yellow.top > 170:
            engine.say('Character has fallen')
            engine.runAndWait()
            # stop_maple_coords = pyag.locateCenterOnScreen('stop_maple.PNG',confidence=0.8)
            # pyag.doubleClick(stop_maple_coords)
        if yellow == None:
            print('None found for yellow, main loop')
            pyag.press('Down',1)
    except Exception as e:
        print('Failed to get yellow coords')
    # try:
    #     ds_loc = pyag.locateOnScreen(ds_img,region=(900,49,120,30),confidence=0.7)
    #     print(ds_loc.left)
    # except Exception as e:
    #     print(e)
    #     time.sleep(0.3)
    #     press('T',0.3)
    
# ds = r"C:\\Users\\Michael\\Desktop\\MapleStory\\ds.jpg"
# while True:
#     try:
#         ds_location = pyag.locateOnScreen(ds,region=(900,49,120,30))
#         print('DS found')
#     except:
#         print('No DS found')
#     time.sleep(1)