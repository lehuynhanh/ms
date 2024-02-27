def open_miu():
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