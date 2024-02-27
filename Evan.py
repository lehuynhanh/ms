import pyautogui as pyag
import time
from datetime import datetime,timedelta
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
import pyttsx3

engine = pyttsx3.init()
ms = pyag.getWindowsWithTitle('Dream MS')[0]
ms.moveTo(0,0)
ms.activate()

#pyag.position() #gets the mouse coordinates
#pyag.screenshot(region=(0,366,1030,400))
#pyag.screenshot("bottom_half.jpg",region=(0,366,1030,400)).show()
#pyag.screenshot("bottom_half.jpg",region=(0,366,1030,400)).show()

def movement(direction):
    print('TP ' + direction)
    pressKey(direction)
    time.sleep(1.5)
    press('SPACEBAR',0.5)
    releaseKey(direction)
    time.sleep(0.2)


def attack(direction):
    time.sleep(0.2)
    print('Pressing D ' + direction)
    press(direction,0.4)
    press('d',0.4)
    # time.sleep(0.4)
    # movement(direction)


def attack_no_move():
    time.sleep(0.2)
    print('Pressing D')
    press('d',0.4)
    time.sleep(0.2)
    print('Pressing D')
    press('d',0.4)
    time.sleep(2.3)
    

def buff():
    time.sleep(0.6)
    press('1',0.5)
    time.sleep(2)
    press('2',0.5)
    time.sleep(2)
    press('3',0.5)
    time.sleep(0.6)
    press('4',0.5)
    time.sleep(1)


def init_loot():
    #left 65 rope
    #top 148 top rope
    yellow = pyag.locateOnScreen(yellow_path,region=(10,50,200,200),confidence=0.8)
    #get on rope
    while True:
        try:
            yellow = pyag.locateOnScreen(yellow_path,region=(10,50,200,200),confidence=0.8)
            if yellow == None:
                print('Cant find yellow; stuck on rope?')
                press('UP',1.5)
            if yellow.top <= 148:
                press('UP',0.6)
                break
            if yellow.left < 65:
                movement_jump('RIGHT')
                press('UP',0.8)
            if yellow.left > 65:
                movement_jump('LEFT')
                press('UP',0.8)
            if yellow.left == 65:
                press('ALT',0.3)
                time.sleep(0.2)
                press('UP',1)

        except Exception as e:
            print(e)
    #loot right
    time.sleep(0.5)
    while True:
        try:
            yellow = pyag.locateOnScreen(yellow_path,region=(10,50,200,200),confidence=0.8)
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
    yellow = pyag.locateOnScreen(yellow_path,region=(10,50,200,200),confidence=0.8)
    #get on rope
    while True:
        yellow = pyag.locateOnScreen(yellow_path,region=(10,50,200,200),confidence=0.8)
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
            movement_jump('RIGHT')
            press('UP',0.8)
        if yellow.left > 65:
            movement_jump('LEFT')
            press('UP',0.8)
        if yellow.left == 65:
            press('UP',0.3)
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


def movement_jump(direction):
    press(direction,0.6)
    time.sleep(0.05)
    press('ALT')


last_jump_direction = 'LEFT'
def get_hs():
    global last_jump_direction
    def get_first_rope():
        #need to jump to top 188
        #82, 209 under rope
        try:
            yellow = pyag.locateOnScreen(r"yellow.jpg",region=(10,50,200,200),confidence=0.8)
            while yellow == None or yellow.top > 188:
                if yellow == None:
                    pressKey('UP')
                    press('ALT',0.5)
                    press('LEFT',0.3)
                    releaseKey('UP')
                    yellow = pyag.locateOnScreen(r"yellow.jpg",region=(10,50,200,200),confidence=0.8)
                    continue
                if yellow.left < 82:
                    pressKey('UP')
                    movement_jump('RIGHT')
                    releaseKey('UP')
                if yellow.left > 82:
                    pressKey('UP')
                    movement_jump('LEFT')
                    releaseKey('UP')
                if yellow.left == 82:
                    pressKey('UP')
                    press('ALT',0.5)
                    releaseKey('UP')
                yellow = pyag.locateOnScreen(r"yellow.jpg",region=(10,50,200,200),confidence=0.8)
        except Exception as e:
            print(e)
    def get_second_rope():
        #left 78, top 178
        while True:
            try:
                yellow = pyag.locateOnScreen(r"yellow.jpg",region=(10,50,200,200),confidence=0.8)
                print(yellow)
                if yellow == None:
                    print('Not found for yellow 2nd rope')
                if yellow.left < 78 and yellow.top <= 195:
                    pressKey('UP')
                    press('RIGHT',0.5)
                    press('ALT',0.3)
                    time.sleep(0.1)
                    releaseKey('UP')
                elif yellow.left > 78 and yellow.top <= 195:
                    pressKey('UP')
                    press('LEFT',0.5)
                    press('ALT',0.3)
                    time.sleep(0.1)
                    releaseKey('UP')
                elif yellow.left == 78 and yellow.top >= 179:
                    pressKey('UP')
                    press('ALT',0.3)
                    press('RIGHT',0.3)
                    releaseKey('UP')
                elif yellow.top <= 175:
                    print('We are too high 2nd rope')
                    press('DOWN',0.2)
                elif yellow.left == 78 and (yellow.top == 178 or yellow.top == 177 or yellow.top == 176):
                    break
                elif yellow.top >= 200:
                    get_first_rope()
            except Exception as e:
                print('Found an error while locating yellow dot 2nd rope')
                print(e)
    get_first_rope()
    get_second_rope()
    #Type HS please
    time.sleep(1)
    press('ENTER',0.2)
    time.sleep(0.1)
    press('r')
    press('b')
    press('SPACEBAR')
    press('p')
    press('l')
    press('s')
    press('ENTER',0.2)
    pyag.click(985,450)
    hs_img = None
    get_hs_counter = 0
    while hs_img is None:
        if get_hs_counter == 5:
            get_second_rope()
        get_hs_counter += 1
        hs_img = pyag.locateOnScreen(r"hs.jpg",confidence=0.9)
        time.sleep(3)
    if last_jump_direction == 'RIGHT':
        pressKey('LEFT')
        press('ALT',0.3)
        time.sleep(0.5)
        releaseKey('LEFT')
        last_jump_direction = 'LEFT'
    if last_jump_direction == 'LEFT':
        pressKey('RIGHT')
        press('ALT',0.3)
        time.sleep(6)
        releaseKey('RIGHT')
        last_jump_direction = 'RIGHT'
    
def count_skele(skele_direction):
    if skele_direction == 'LEFT':
        return (len(list(pyag.locateAllOnScreen('skeles.jpg',region=(0,366,515,400),confidence=0.85))) +
    len(list(pyag.locateAllOnScreen('eskele.jpg',region=(0,366,515,400),confidence=0.85))) +
    len(list(pyag.locateAllOnScreen('skeles2.jpg',region=(0,366,515,400),confidence=0.85))) +
    len(list(pyag.locateAllOnScreen('eskele2.jpg',region=(0,366,515,400),confidence=0.85)))
    )
    if skele_direction == 'RIGHT':
        return (len(list(pyag.locateAllOnScreen('skeles.jpg',region=(515,366,515,400),confidence=0.85))) +
    len(list(pyag.locateAllOnScreen('eskele.jpg',region=(515,366,515,400),confidence=0.85))) +
    len(list(pyag.locateAllOnScreen('skeles2.jpg',region=(515,366,515,400),confidence=0.85))) +
    len(list(pyag.locateAllOnScreen('eskele2.jpg',region=(515,366,515,400),confidence=0.85)))
    )
    
    
print('Starting in 2 seconds.. navigate to MS')
last_buff = datetime.now() - timedelta(seconds=160)
loot_mode = datetime.now()
pet_food = datetime.now()
last_hs = datetime.now() - timedelta(seconds=151)
now = datetime.now()
loot_counter = 0
yellow_path = r"yellow_evan.jpg"
# yellow = None
# last_yellow = None
last_tp = 'LEFT'
#get_hs()
while True:
    now = datetime.now()
    if now > (last_buff + timedelta(seconds=150)):
        print('Buff attempted')
        last_buff = now
        buff()
    if now > (pet_food + timedelta(seconds=400)):
        print('trying pet_food')
        press('U')
        pet_food = now
    if now > (last_hs + timedelta(seconds=150)):
        print('Getting HS')
        time.sleep(2)
        press('1',0.5)
        get_hs()
        last_hs = datetime.now()
    try:
        # yellow = pyag.locateOnScreen(yellow_path,confidence=0.8)
#pyag.screenshot("bottom_half.jpg",region=(0,366,1030,400)).show()
#pyag.screenshot("bottom_half.jpg",region=(0,366,1030,400)).show()
        # try:
            # skeles = len(list(pyag.locateAllOnScreen('skeles.jpg',region=(0,366,515,400),confidence=0.7)))
            # skeles2 = len(list(pyag.locateAllOnScreen('skeles2.jpg',region=(515,366,515,400),confidence=0.7)))
            # skele_count = skeles + skeles2
            # print(skele_count)
            # # if skele_count < 4:
                # # print('skele count too low, skipping: ' + str(skeles + skeles2))
                # # continue
                # # time.sleep(0.1)
        # except Exception as e:
            # print(e)
        yellow = pyag.locateOnScreen(r"yellow.jpg",region=(30,190,130,50),confidence=0.80)
        print(yellow)
        # last_yellow = yellow
        if yellow == None:
            press('LEFT',2)
        if yellow.left <= 74:
            movement('RIGHT')
        if yellow.left >= 105:
            movement('LEFT')
        else:
            skelecl = count_skele('LEFT')
            skelecr = count_skele('RIGHT')
            print(skelecl)
            print(skelecr)
            if skelecl > 0:
                attack('LEFT')
                if count_skele('LEFT') > 0:
                    attack('LEFT')
            if skelecr > 0:
                attack('RIGHT')
                if count_skele('RIGHT') > 0:
                    attack('RIGHT')
            #look at right attack right if greater than 0
    except Exception as e:
        print('Failed to get yellow coords')

import pyautogui as pyag
import time
while True:
    #yellow = pyag.locateOnScreen(r"yellow.jpg",region=(30,190,130,50),confidence=0.80)
    yellow = pyag.locateOnScreen(r"yellow.jpg",region=(10,50,200,200),confidence=0.8)
    print(yellow)
    time.sleep(1)
