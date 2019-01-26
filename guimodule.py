# -*- coding: utf-8 -*-
import pyautogui as pg
#print(dir(pyautogui))
print(pg.size())
a,b=pg.size()
print(a,b)
#pg.moveTo(1000,600, duration=1)
"""
for i in range(3):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)"""
"""    
for i in range(10):
    pyautogui.moveRel(100, 0, duration=0.25)
    pyautogui.moveRel(0, 100, duration=0.25)
    #Controlling the Keyboard and Mouse with GUI Automation 417
    pyautogui.moveRel(-100, 0, duration=0.25)
    pyautogui.moveRel(0, -100, duration=0.25)
    """
"""    
a=pg.position()
print(a)"""
"""
print(pg.click(1000,500,button='right'))
print(pg.click(1000,400))"""
#pg.doubleClick(x=60,y=180,duration=100)
"""pg.rightClick()
pg.dragTo()
pg.dragrel()"""
pg.scroll(1000)
pg.screenshot()
pg.locateOnScreen("name of path or image")
pg.click()
pg.typewrite("how are you")
pg.typewrite(['a','ctrl'])
pg.press('enter')