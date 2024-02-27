import pyautogui as pyag
import time
from datetime import datetime,timedelta
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
import pyttsx3
import sys

engine = pyttsx3.init()
ms = pyag.getWindowsWithTitle('Dream MS')[0]
ms.moveTo(0,0)
ms.activate()

def movement(direction):
    print('TP ' + direction)
    pressKey(direction)
    time.sleep(1.8)
    press('X',0.5)
    releaseKey(direction)
    time.sleep(0.2)


def movement_jump(direction):
    press(direction,0.5)
    time.sleep(0.1)
    press('ALT')
    time.sleep(0.2)


def attack(direction):
    time.sleep(0.2)
    print('Pressing D')
    press('d',0.3)
    time.sleep(0.1)
    print('Pressing D')
    press('d',0.3)
    time.sleep(1.2)
    movement(direction)


def attack_no_move():
    print('Pressing D')
    press('d',0.3)
    time.sleep(0.1)
    print('Pressing D')
    press('d',0.3)
    

def buff():
    time.sleep(0.6)
    press('6',0.3)
    time.sleep(0.4)
    press('6',0.3)
    time.sleep(0.4)
    press('6',0.3)
    time.sleep(0.4)
    press('7',0.3)
    time.sleep(0.6)
    press('8',0.3)
    time.sleep(0.6)
    press('9',0.3)
    time.sleep(1)


def mb():
    time.sleep(0.6)
    press('5',0.3)
    time.sleep(0.4)
    press('5',0.3)
    time.sleep(1)

    
def init_loot():
    #left 65 rope
    #top 148 top rope
    #yellow = pyag.locateOnScreen("yellow.jpg",region=(10,50,200,200),confidence=0.8)
    #get on rope
    try:
        pressKey('UP')
        while True:
            try:
                yellow = pyag.locateOnScreen("yellow.jpg",region=(10,50,200,200),confidence=0.8)
            except Exception as e:
                print(e)
                press('UP',1.5)
                press('LEFT',1.5)
                continue
            if yellow == None:
                press('UP',1.5)
                press('LEFT',1.5)
                continue
            if yellow.top <= 148:
                press('UP',0.6)
                break
            if yellow.left < 65:
                movement_jump('RIGHT')
            if yellow.left > 65:
                movement_jump('LEFT')
            if yellow.left == 65:
                press('ALT',0.3)
                time.sleep(0.1)
        releaseKey('UP')
    except Exception as e:
        releaseKey('UP')
        print(e)
    #loot right
    time.sleep(0.5)
    while True:
        try:
            yellow = pyag.locateOnScreen("yellow.jpg",region=(10,50,200,200),confidence=0.8)
            if yellow.left <= 100:
                press('RIGHT',0.3)
            else:
                break
        except Exception as e:
            print(e)
    time.sleep(0.3)
    press('LEFT',2)


def init_sell():
    #left 65 rope
    #top 148 top rope
    #yellow = pyag.locateOnScreen("yellow.jpg",region=(10,50,200,200),confidence=0.8)
    #get on rope
    while True:
        try:
            yellow = pyag.locateOnScreen("yellow.jpg",region=(10,50,200,200),confidence=0.8)
            if yellow == None:
                print('Cant find yellow; stuck on rope?')
                press('UP',1.5)
                press('LEFT',1)
                continue
            if yellow.top <= 157:
                if yellow.top <= 152:
                    press('DOWN',0.3)
                break
            if yellow.left < 65:
                pressKey('UP')
                movement_jump('RIGHT')
                time.sleep(0.2)
                releaseKey('UP')
            if yellow.left > 65:
                pressKey('UP')
                movement_jump('LEFT')
                time.sleep(0.2)
                releaseKey('UP')
            if yellow.left == 65:
                press('ALT',0.3)
                press('UP',0.3)
        except Exception as e:
            print('Exception: Cant find yellow; stuck on rope?')
            press('UP',1.5)
            press('LEFT',1)
    time.sleep(0.5)
    miu = None
    sell_all = None
    leave_store = None
    while miu is None:
        try:
            miu = pyag.locateCenterOnScreen('miu.jpg',confidence=0.9)
            if miu is None:
                press('I',0.3)
        except Exception as e:
            print(e)
            press('I',0.3)        
    pyag.doubleClick(miu)
    time.sleep(1)
    while sell_all is None:
        try:
            sell_all = pyag.locateCenterOnScreen('sell_all.jpg',confidence=0.8)
        except Exception as e:
            engine.say('Cannot sell all')
            engine.runAndWait()
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

def count_skele():
    skele,skele1,skele2,skele3 = 0,0,0,0
    try:
        skele = len(list(pyag.locateAllOnScreen('skeles.jpg',confidence=0.85)))
    except Exception as e:
        print(e)
    try:
        skele1 = len(list(pyag.locateAllOnScreen('eskele.jpg',confidence=0.85)))
    except Exception as e:
        print(e)
    try:
        skele2 = len(list(pyag.locateAllOnScreen('skeles2.jpg',confidence=0.85)))
    except Exception as e:
        print(e)
    try:
        skele3 = len(list(pyag.locateAllOnScreen('eskele2.jpg',confidence=0.85)))
    except Exception as e:
        print(e)
    return skele + skele1 + skele2 + skele3

print('Starting in 2 seconds.. navigate to MS')
last_buff = datetime.now() #- timedelta(seconds=160)
loot_mode = datetime.now()
pet_food = datetime.now()
now = datetime.now()
last_mb = now
loot_counter = 0
# yellow = pyag.locateOnScreen("yellow.jpg",confidence=0.7)
# print(yellow.left)
# sc = pyag.screenshot('yellow.jpg',region=(69,158,8,8))
# buffs = pyag.screenshot('buffs.jpg',region=(800,49,20,20))
# ds = pyag.screenshot('ds.jpg',region=(993,49,20,20))
#init_loot()
#init_sell()
high_counter_time = now
too_high_counter = 0
while True:
    now = datetime.now()
    try:
        minidgn = pyag.locateOnScreen('minidgn_rm.jpg',region=(10,50,200,200),confidence=0.85)
        # print(minidgn)
        if minidgn is None:
            print('Mini dungeon exit')
            minidgn_counter += 1
            engine.say('We are not in mini dungeon')
            engine.runAndWait()
            if minidgn_counter == 3:
                stop_maple_coords = pyag.locateCenterOnScreen('stop_maple.PNG',confidence=0.8)
                pyag.doubleClick(stop_maple_coords)
    except:
        if minidgn is None:
            print('Mini dungeon exit')
            minidgn_counter += 1
            engine.say('We are not in mini dungeon')
            engine.runAndWait()
            if minidgn_counter == 3:
                ms.close()
                sys.exit()
                stop_maple_coords = pyag.locateCenterOnScreen('stop_maple.PNG',confidence=0.8)
                pyag.doubleClick(stop_maple_coords)
    if now > (last_buff + timedelta(seconds=150)):
        print('Buff attempted')
        try:
            yellow = pyag.locateOnScreen("yellow.jpg",region=(10,50,200,200),confidence=0.8)
            if yellow.left >= 86:
                movement('LEFT')
        except:
            print('Couldnt find yellow for buff')
        last_buff = datetime.now()
        buff()
    if now > (last_mb + timedelta(seconds=65)):
        print('last_mb attempted')
        try:
            yellow = pyag.locateOnScreen("yellow.jpg",region=(10,50,200,200),confidence=0.8)
            if yellow.left >= 86:
                movement('LEFT')
        except:
            print('Couldnt find yellow for buff')
        last_mb = datetime.now()
        mb()
    if loot_counter == 2:
        loot_counter = 0
        print('attempt sell')
        try:
            yellow = pyag.locateOnScreen("yellow.jpg",region=(10,50,200,200),confidence=0.8)
            if yellow.left >= 76:
                movement('LEFT')
        except:
            print('Couldnt find yellow for buff')
        init_sell()
    if now > (loot_mode + timedelta(seconds=120)):
        print('trying loot')
        press('6',0.4)
        try:
            yellow = pyag.locateOnScreen("yellow.jpg",region=(10,50,200,200),confidence=0.8)
            if yellow.left >= 76:
                movement('LEFT')
        except:
            print('Couldnt find yellow for buff')
        init_loot()
        loot_counter += 1
        loot_mode = datetime.now()
    if now > (pet_food + timedelta(seconds=400)):
        print('trying pet_food')
        press('0')
        pet_food = now
    try:
        # yellow = pyag.locateOnScreen("yellow.jpg",confidence=0.8)
        try:
            skeles = count_skele()
            # print(skeles)
            if skeles <= 3:
                print('skele count too low, skipping: ' + str(skeles))
                continue
                time.sleep(0.1)
        except Exception as e:
            print(e)
        try:
            yellow = pyag.locateOnScreen("yellow.jpg",region=(10,50,200,200),confidence=0.9)
            print(yellow)
            if yellow == None:
                print('Cant find yellow; stuck on rope?')
                press('UP',1.5)
            if yellow.left ==65 and yellow.top>=154:
                pressKey('RIGHT')
                press('ALT',0.3)
                releaseKey('RIGHT')
            if yellow.top <= 148:
                print('We are too high up - ' + str(too_high_counter))
                too_high_counter += 1
                if too_high_counter >= 3 and now > high_counter_time + timedelta(seconds=20):
                    too_high_counter = 0 
                    time.sleep(2)
                    pressKey('DOWN')
                    press('ALT',0.3)
                    press('RIGHT',0.2)
                    releaseKey('DOWN')
                if too_high_counter > 0 and now > high_counter_time + timedelta(seconds=61):
                    too_high_counter = 0
            if yellow.left >= 100:
                press('LEFT',2)
            if yellow.left >= 89:
                attack('LEFT')
            elif yellow.left <=63:
                attack('RIGHT')
            else:
                attack_no_move()
            if yellow.top > 170:
                engine.say('Character has fallen')
                engine.runAndWait()
        except Exception as e:
            print('Failed to find yellow')
            press('UP',0.5)
            press('LEFT',0.5)
        
    except Exception as e:
        print('Failed to get yellow coords')
