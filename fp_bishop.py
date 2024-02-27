import pyautogui as pyag
import time
from datetime import datetime,timedelta
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
import pyttsx3
import sys
import os
import threading

engine = pyttsx3.init()
cmdpt = pyag.getActiveWindow()
cmdpt.moveTo(1031,0)
cmdpt.resizeTo(600,300)
ms = pyag.getWindowsWithTitle('Dream MS')[0]
ms.moveTo(0,0)
ms.activate()

pyag.FAILSAFE = False


def movement(direction):
    print(str(datetime.now().strftime("%H:%M:%S")) + ' - TP ' + direction)
    pressKey(direction)
    time.sleep(1.8)
    press('X',0.5)
    releaseKey(direction)
    time.sleep(0.2)


def movement_jump(direction):
    press(direction,0.6)
    time.sleep(0.1)
    press('ALT')
    time.sleep(0.2)


def attack(direction):
    time.sleep(0.2)
    print(str(datetime.now().strftime("%H:%M:%S")) + ' - Pressing D')
    press('d',0.3)
    time.sleep(0.1)
    print(str(datetime.now().strftime("%H:%M:%S")) + ' - Pressing D')
    press('d',0.3)
    time.sleep(1.2)
    movement(direction)


def attack_no_move():
    print(str(datetime.now().strftime("%H:%M:%S")) + ' - Pressing D')
    press('d',0.3)
    time.sleep(0.1)
    print(str(datetime.now().strftime("%H:%M:%S")) + ' - Pressing D')
    press('d',0.3)
    

def buff():
    time.sleep(0.6)
    press('5',0.3)
    time.sleep(0.6)
    press('5',0.3)
    time.sleep(0.6)
    press('6',0.3)
    time.sleep(0.4)
    press('6',0.3)
    time.sleep(0.4)
    press('7',0.3)
    time.sleep(0.6)
    press('8',0.3)
    time.sleep(0.6)
    press('9',0.3)
    time.sleep(0.6)
    press('-',0.3)
    time.sleep(1)

    

def get_yellow():
    try:
        yellow = pyag.locateOnScreen("yellow.jpg",region=(10,50,200,160),confidence=0.8)
        print(yellow)
    except Exception as e:
        print(e)



def init_loot():
    #get on rope
    try:
        pressKey('UP')
        loot_attempt = 0
        while True:
            print("Trying to loot - " + str(loot_attempt))
            loot_attempt += 1
            if loot_attempt >= 30:
                break
            try:
                yellow = pyag.locateOnScreen("yellow.jpg",region=(10,50,200,200),confidence=0.8)
                print(yellow)
                #print(str(datetime.now().strftime("%H:%M:%S")) + ' - We are trying to loot')
            except Exception as e:
                print(e)
                press('UP',1.5)
                press('LEFT',1.5)
                continue
            if yellow == None:
                press('UP',1.5)
                press('LEFT',1.5)
                continue
            if yellow.top >= 148:
                engine.say('Character has fallen')
                engine.runAndWait()
                break
            if yellow.top <= 128:
                press('UP',0.6)
                press('ALT',0.5)
                break
            if yellow.left < 65 and yellow.top <= 145:
                movement_jump('RIGHT')
            if yellow.left > 65 and yellow.top <= 145:
                movement_jump('LEFT')
            if yellow.left == 65:
                press('ALT',0.3)
                time.sleep(0.1)
        releaseKey('UP')
    except Exception as e:
        print(str(datetime.now().strftime("%H:%M:%S")) + ' - Failure in looting')
        releaseKey('UP')
        print(e)
    #loot right
    time.sleep(0.5)
    while True:
        try:
            yellow = pyag.locateOnScreen("yellow.jpg",region=(10,50,200,160),confidence=0.8)
            if yellow.left == 65:
                pressKey('LEFT')
                time.sleep(0.1)
                press('ALT',0.3)
                releaseKey('LEFT')
            if yellow.left <= 100:
                press('RIGHT',0.3)
            else:
                break
        except Exception as e:
            print(e)
    time.sleep(0.3)
    press('LEFT',2)


def open_miu():
    ms.activate()
    press('ENTER',0.2)
    time.sleep(0.1)
    press('@')
    press('m')
    press('i')
    press('u')
    press('ENTER',0.2)



def init_sell():
    def sell_etc():
        ms.activate()
        try: 
            miu_etc = pyag.locateCenterOnScreen('miu_etc.jpg',confidence=0.9)
            pyag.doubleClick(miu_etc)
            time.sleep(1)
            miu_down = pyag.locateCenterOnScreen('miu_down.jpg',confidence=0.98)
            pyag.doubleClick(miu_down.x,miu_down.y-10)
            pyag.doubleClick(miu_down.x,miu_down.y-10)
            pyag.doubleClick(miu_down.x,miu_down.y-10)
            try:
                oldneckbone = pyag.locateCenterOnScreen('oldneckbone.jpg',confidence=0.9)
            except: 
                oldneckbone = False
                pass
            try:
                brokenhorn = pyag.locateCenterOnScreen('brokenhorn.jpg',confidence=0.9)
            except:
                brokenhorn = False
                pass
            while oldneckbone or brokenhorn:
                try:
                    oldneckbone = pyag.locateCenterOnScreen('oldneckbone.jpg',confidence=0.90)
                    pyag.doubleClick(oldneckbone)
                    time.sleep(0.2)
                    press('ENTER')
                    pyag.moveTo(100,100)
                    time.sleep(1)
                except: 
                    oldneckbone = False
                    pass
                try:
                    brokenhorn = pyag.locateCenterOnScreen('brokenhorn.jpg',confidence=0.90)
                    pyag.doubleClick(brokenhorn)
                    time.sleep(0.2)
                    press('ENTER')
                    pyag.moveTo(100,100)
                    time.sleep(1)
                except:
                    brokenhorn = False
                    pass
                try:
                    aqua_ore = pyag.locateCenterOnScreen('aqua_ore.jpg',confidence=0.90)
                    pyag.doubleClick(aqua_ore)
                    time.sleep(0.2)
                    press('ENTER')
                    pyag.moveTo(100,100)
                    time.sleep(1)
                except: 
                    pass
                try:
                    top_ore = pyag.locateCenterOnScreen('top_ore.jpg',confidence=0.90)
                    pyag.doubleClick(top_ore)
                    time.sleep(0.2)
                    press('ENTER')
                    pyag.moveTo(100,100)
                    time.sleep(1)
                except:
                    pass
                try:
                    amy_ore = pyag.locateCenterOnScreen('amy_ore.jpg',confidence=0.90)
                    pyag.doubleClick(amy_ore)
                    time.sleep(0.2)
                    press('ENTER')
                    pyag.moveTo(100,100)
                    time.sleep(1)
                except: 
                    pass
                try:
                    dragonspirit = pyag.locateCenterOnScreen('dragonspirit.jpg',confidence=0.90)
                    pyag.doubleClick(dragonspirit)
                    time.sleep(0.2)
                    press('ENTER')
                    pyag.moveTo(100,100)
                    time.sleep(1)
                except:
                    pass
                try:
                    dragonscale = pyag.locateCenterOnScreen('dragonscale.jpg',confidence=0.90)
                    pyag.doubleClick(dragonscale)
                    time.sleep(0.2)
                    press('ENTER')
                    pyag.moveTo(100,100)
                    time.sleep(1)
                except: 
                    pass
                try:
                    stim = pyag.locateCenterOnScreen('stim.jpg',confidence=0.90)
                    pyag.doubleClick(stim)
                    time.sleep(0.2)
                    press('ENTER')
                    pyag.moveTo(100,100)
                    time.sleep(1)
                except:
                    pass
        except:
            pass
    attempt_sell_counter = 0
    while True:
        attempt_sell_counter  += 1
        if attempt_sell_counter >= 30:
            break
        try:
            yellow = pyag.locateOnScreen("yellow.jpg",region=(10,50,200,160),confidence=0.8)
            if yellow == None:
                print(str(datetime.now().strftime("%H:%M:%S")) + ' - Cant find yellow; stuck on rope?')
                pressKey('LEFT')
                press('ALT',0.4)
                releaseKey('LEFT')
                continue
            if yellow.top <= 128:
                press('DOWN',0.4)
                break
            elif yellow.top >= 148:
                engine.say('Character has fallen')
                engine.runAndWait()
                break
            elif yellow.left < 65:
                pressKey('UP')
                movement_jump('RIGHT')
                time.sleep(0.2)
                releaseKey('UP')
            elif yellow.left > 65:
                pressKey('UP')
                movement_jump('LEFT')
                time.sleep(0.2)
                releaseKey('UP')
            elif yellow.left == 65:
                press('ALT',0.3)
                press('UP',0.3)
        except Exception as e:
            print(str(datetime.now().strftime("%H:%M:%S")) + ' - Exception: Cant find yellow; stuck on rope?')
            press('UP',1.5)
            press('LEFT',1)
    time.sleep(0.5)
    sell_all = None
    leave_store = None
    open_miu()
    time.sleep(1.5)
    while sell_all is None:
        try:
            sell_all = pyag.locateCenterOnScreen('sell_all.jpg',confidence=0.8)
            pyag.doubleClick(sell_all)
            time.sleep(1)
            press('ENTER',0.5)
        except Exception as e:
            print(str(datetime.now().strftime("%H:%M:%S")) + ' - Cannot sell all')
            # engine.say('Cannot sell all')
            # engine.runAndWait()
            open_miu()
            print(e)
    time.sleep(3)
    sell_etc()
    while leave_store is None:
        try:
            leave_store = pyag.locateCenterOnScreen('leave_store.jpg',confidence=0.9)
            pyag.doubleClick(leave_store)
            time.sleep(1)
        except:
            engine.say('Cant leave store')
            engine.runAndWait()
            print(e)
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
        pass
        # print(e)
    try:
        skele1 = len(list(pyag.locateAllOnScreen('eskele.jpg',confidence=0.85)))
    except Exception as e:
        pass
        # print(e)
    try:
        skele2 = len(list(pyag.locateAllOnScreen('skeles2.jpg',confidence=0.85)))
    except Exception as e:
        pass
        # print(e)
    try:
        skele3 = len(list(pyag.locateAllOnScreen('eskele2.jpg',confidence=0.85)))
    except Exception as e:
        pass
        # print(e)
    return skele + skele1 + skele2 + skele3



def deaggro():
    ms.activate()
    press('O',0.3)
    time.sleep(0.1)
    press('DOWN',0.3)
    time.sleep(0.1)
    press('DOWN',0.3)
    time.sleep(0.1)
    press('DOWN',0.3)
    time.sleep(0.1)
    press('DOWN',0.3)
    time.sleep(0.1)
    press('DOWN',0.3)
    time.sleep(0.1)
    press('ENTER',0.3)
    time.sleep(2)
    fm = None
    while fm is None:
        try:
            fm = pyag.locateOnScreen('fm.jpg',confidence=0.9)
            time.sleep(1)
            press('UP',0.3)
        except Exception as e:
            print(e)
    time.sleep(1)



def reenterdgn():
    ms.activate()
    #change channel, right portal - left=153, top=170
    # left platform of dgn = left=125, top=188,
    #left platform, right top portal left=138, top=168,
    press('6',0.4)
    yellow = None
    while yellow == None:
        try:
            yellow = pyag.locateOnScreen("yellow.jpg",region=(10,50,200,160),confidence=0.8)
        except Exception as e:
            print(e)
            deaggro()
            time.sleep(3)
    if yellow.left == 63 and yellow.top < 105: #left=63, top=124, top left portal platform
        while yellow.left < 120 or yellow == None:
            pressKey('RIGHT')
            time.sleep(0.6)
            press('ALT',0.2)
            press('X',0.4)
            releaseKey('RIGHT')
            yellow = pyag.locateOnScreen("yellow.jpg",region=(10,50,200,160),confidence=0.8)
        deaggro()
    elif yellow.left == 125 and yellow.top == 165: # left plat dgn
        ms.activate()
        pressKey('RIGHT')
        time.sleep(0.6)
        press('ALT',0.4)
        press('X',0.4)
        releaseKey('RIGHT')
        time.sleep(0.2)
        press('RIGHT',0.4)
        press('UP')
    elif yellow.left == 153 and yellow.top == 147: # top right portal
        pressKey('DOWN')
        time.sleep(0.2)
        press('ALT',0.4)
        time.sleep(0.6)
        press('ALT',0.4)
        time.sleep(0.5)
        releaseKey('DOWN')
        press('LEFT',0.5)
        press('UP',0.3)
    elif yellow.left == 138 and yellow.top == 145: #left platform, right portal
        pressKey('DOWN')
        time.sleep(0.2)
        press('ALT',0.4)
        time.sleep(0.5)
        releaseKey('DOWN')
        press('RIGHT',1.2)
        press('UP',0.3)
    else:
        deaggro()
    time.sleep(3)
    try:
        minidgn = pyag.locateOnScreen('minidgn_rm.jpg',region=(10,50,200,160),confidence=0.85)
        # we are in minidgn, go to attack area
        time.sleep(1)
        pressKey('LEFT')
        time.sleep(0.6)
        press('ALT',0.3)
        releaseKey('LEFT')
        time.sleep(0.2)
        press('LEFT',0.5)
        pressKey('UP')
        press('ALT',0.3)
        time.sleep(2)
        releaseKey('UP')
        press('J')
        pressKey('LEFT')
        time.sleep(0.4)
        press('ALT',0.4)
        press('X',0.4)
        releaseKey('LEFT')
        movement('LEFT')
        movement('LEFT')
    except:
        reenterdgn()



def check_map():
    global minidgn_counter
    try:
        minidgn = pyag.locateOnScreen('minidgn_rm.jpg',region=(10,50,200,160),confidence=0.85)
        #print(str(datetime.now().strftime("%H:%M:%S")) + ' - We are in mini dungeon')
        return True
    except:
        #ms.close()
        print(str(datetime.now().strftime("%H:%M:%S")) + ' - We are outside dungeon')
        time.sleep(3)
        try:
            dragon_nest = pyag.locateOnScreen('dragon_nest.png',region=(10,50,200,160),confidence=0.85)
            print(dragon_nest)
            reenterdgn()
        except Exception as e:
            os._exit(1)
    time.sleep(1)



def char_fallen():
    def get_first_rope():
        #need to jump to top 188
        #82, 209 under rope
        try:
            yellow = pyag.locateOnScreen("yellow.jpg",region=(10,50,200,160),confidence=0.8)
            while yellow == None or yellow.top > 166:
                if yellow == None:
                    pressKey('UP')
                    time.sleep(0.1)
                    press('ALT',0.5)
                    press('LEFT',0.3)
                    releaseKey('UP')
                    yellow = pyag.locateOnScreen("yellow.jpg",region=(10,50,200,160),confidence=0.8)
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
                yellow = pyag.locateOnScreen("yellow.jpg",region=(10,50,200,160),confidence=0.8)
        except Exception as e:
            print(e)
    def get_second_rope():
        #left 78, top 178
        while True:
            try:
                yellow = pyag.locateOnScreen("yellow.jpg",region=(10,50,200,160),confidence=0.8)
                print(yellow)
                if yellow.left < 78 and (165 <= yellow.top <= 170): #below 2nd rope
                    pressKey('UP')
                    press('RIGHT',0.5)
                    press('ALT',0.3)
                    time.sleep(0.25)
                    releaseKey('UP')
                elif yellow.left > 78 and (165 <= yellow.top <= 170): #below 2nd rope
                    pressKey('UP')
                    press('LEFT',0.5)
                    press('ALT',0.3)
                    time.sleep(0.25)
                    releaseKey('UP')
                elif yellow.left == 78 and yellow.top >= 166: # not yet on rope, need to climb from under
                    pressKey('UP')
                    time.sleep(0.1)
                    press('ALT',0.3)
                    press('RIGHT',0.3)
                    time.sleep(0.1)
                    releaseKey('UP')
                elif yellow.top >= 153 and yellow.left == 78: #on rope
                    print(str(datetime.now().strftime("%H:%M:%S")) + ' - We are too low 2nd rope')
                    press('UP',0.5)
                elif yellow.top<=152:
                    press('ALT',0.3)
                    press('UP',0.8)
                    break
                elif yellow.top >= 170:
                    get_first_rope()
            except Exception as e:
                print(str(datetime.now().strftime("%H:%M:%S")) + ' - Found an error while locating yellow dot 2nd rope')
                press('ALT',0.3)
                press('UP',0.5)
                print(e)
    if check_map():
        get_first_rope()
        get_second_rope()
        time.sleep(1)

    
# thrObj = threading.Thread(target=check_map)
# thrObj.start()

print(str(datetime.now().strftime("%H:%M:%S")) + ' - Starting in 2 seconds.. navigate to MS')
last_buff = datetime.now() #- timedelta(seconds=160)
loot_mode = datetime.now()
pet_food = datetime.now()
now = datetime.now()
loot_counter = 0
minidgn_counter = 0
# yellow = pyag.locateOnScreen("yellow.jpg",confidence=0.7)
# print(yellow.left)
# sc = pyag.screenshot('yellow.jpg',region=(69,158,8,8))
# buffs = pyag.screenshot('buffs.jpg',region=(800,49,20,20))
# ds = pyag.screenshot('ds.jpg',region=(993,49,20,20))
#init_loot()
#init_sell()
buff()
time.sleep(1)
high_counter_time = now
too_high_counter = 0
click_counter = 0
while True:
    now = datetime.now()
    check_map()
    if click_counter >=5:
        pyag.click(584,639)
        click_counter = 0
        try:
            monsterbookx = pyag.locateOnScreen("monsterbookx.jpg",region=(0,50,1000,700),confidence=0.95)
            pyag.click(monsterbookx)
        except:
            pass
    else:
        click_counter += 1
    if now > (last_buff + timedelta(seconds=150)):
        print(str(datetime.now().strftime("%H:%M:%S")) + ' - Buff attempted')
        try:
            yellow = pyag.locateOnScreen("yellow.jpg",region=(10,50,200,160),confidence=0.8)
            if yellow.left >= 86:
                movement('LEFT')
        except:
            print(str(datetime.now().strftime("%H:%M:%S")) + ' - Couldnt find yellow for buff')
        last_buff = datetime.now()
        buff()
    if loot_counter == 2:
        loot_counter = 0
        print(str(datetime.now().strftime("%H:%M:%S")) + ' - attempt sell')
        try:
            yellow = pyag.locateOnScreen("yellow.jpg",region=(10,50,200,160),confidence=0.8)
            if yellow.left >= 76:
                movement('LEFT')
        except:
            print(str(datetime.now().strftime("%H:%M:%S")) + ' - Couldnt find yellow for buff')
        init_sell()
        time.sleep(1)
        try:
            monsterbookx = pyag.locateOnScreen("monsterbookx.jpg",region=(0,50,1000,700),confidence=0.95)
            pyag.click(monsterbookx)
        except:
            pass
        try:
            yellow = pyag.locateOnScreen("yellow.jpg",region=(10,50,200,160),confidence=0.8)
            if yellow.left >= 76:
                movement('LEFT')
        except:
            print(str(datetime.now().strftime("%H:%M:%S")) + ' - Couldnt find yellow for buff')
        loot_mode = datetime.now()
    if now > (loot_mode + timedelta(seconds=120)):
        print(str(datetime.now().strftime("%H:%M:%S")) + ' - trying loot')
        press('6',0.4)
        try:
            yellow = pyag.locateOnScreen("yellow.jpg",region=(10,50,200,160),confidence=0.8)
            if yellow.left >= 76:
                movement('LEFT')
        except:
            print(str(datetime.now().strftime("%H:%M:%S")) + ' - Couldnt find yellow for buff')
        init_loot()
        loot_counter += 1
        loot_mode = datetime.now()
        try:
            yellow = pyag.locateOnScreen("yellow.jpg",region=(10,50,200,160),confidence=0.8)
            if yellow.left >= 76:
                movement('LEFT')
        except:
            print(str(datetime.now().strftime("%H:%M:%S")) + ' - Couldnt find yellow for buff')
    if now > (pet_food + timedelta(seconds=400)):
        print(str(datetime.now().strftime("%H:%M:%S")) + ' - trying pet_food')
        press('0')
        pet_food = now
    try:
        try:
            skeles = count_skele()
            # print(skeles)
            if skeles <= 3:
                print(str(datetime.now().strftime("%H:%M:%S")) + ' - skele count too low, skipping: ' + str(skeles))
                continue
                time.sleep(0.1)
        except Exception as e:
            print(e)
        try:
            yellow = pyag.locateOnScreen("yellow.jpg",region=(10,50,200,160),confidence=0.8)
            print(yellow)
            if yellow.left == 65 and yellow.top>=128 and yellow.top<=138:
                #We are on rope, need to jump off
                pressKey('RIGHT')
                time.sleep(0.1)
                press('ALT',0.3)
                releaseKey('RIGHT')
                continue
            if yellow.top <= 128 and yellow.left < 100:
                #We are too high, need to jump down
                time.sleep(2)
                pressKey('DOWN')
                time.sleep(1)
                press('ALT',0.3)
                press('RIGHT',0.2)
                releaseKey('DOWN')
            if yellow.left >= 100:
                press('LEFT',2)
            if yellow.left >= 89:
                attack('LEFT')
            elif yellow.left <=63:
                attack('RIGHT')
            else:
                attack_no_move()
            if yellow.top > 148:
                print(str(datetime.now().strftime("%H:%M:%S")) + ' - Char has fallen')
                engine.say('Character has fallen')
                engine.runAndWait()
                char_fallen()
        except Exception as e:
            print(str(datetime.now().strftime("%H:%M:%S")) + ' - Failed to find yellow')
            press('UP',0.5)
            press('LEFT',0.5)
    except Exception as e:
        print(str(datetime.now().strftime("%H:%M:%S")) + ' - Failed to get yellow coords')
