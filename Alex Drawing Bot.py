#--------------MADE BOT WHICH CAN DRAW ALEX!!!!!!!----------------------------------


import pyautogui
import time

pyautogui.hotkey('win', 'run')
time.sleep(0.0001)
pyautogui.typewrite('paint')
time.sleep(3)
pyautogui.hotkey('enter')

time.sleep(5)
pyautogui.moveTo(935,640)

#------------DRAWING PART----------------------------
#DRAWING FACE
    #STEP 1
time.sleep(2)
pyautogui.dragTo(935,570)
    #STEP 2
time.sleep(0.0001)
pyautogui.dragTo(1015,570)
    #STEP 3
time.sleep(0.0001)
pyautogui.dragTo(1015,640)
    #STEP 4
time.sleep(0.0001)
pyautogui.dragTo(935,640)

#DRAWING ARMS AND BODY
time.sleep(0.0001)
pyautogui.moveTo(935,640)
pyautogui.dragTo(895,640)

pyautogui.dragTo(895,740)

time.sleep(0.0001)
pyautogui.dragTo(925,740)

time.sleep(0.0001)
pyautogui.dragTo(925,680)

time.sleep(0.0001)
pyautogui.dragTo(935,680)

time.sleep(0.0001)
pyautogui.dragTo(935,770)

time.sleep(0.0001)
pyautogui.dragTo(1015,770)

time.sleep(0.0001)
pyautogui.dragTo(1015,680)

time.sleep(0.0001)
pyautogui.dragTo(1025,680)

time.sleep(0.0001)
pyautogui.dragTo(1025,740)

time.sleep(0.0001)
pyautogui.dragTo(1055,740)

time.sleep(0.0001)
pyautogui.dragTo(1055,640)

    #STEP 11
time.sleep(0.0001)
pyautogui.dragTo(1015,640)

#DRAWING SLEEVES
time.sleep(0.0001)
pyautogui.moveTo(925,680)

time.sleep(0.0001)
pyautogui.dragTo(895,680)

time.sleep(0.0001)
pyautogui.moveTo(1025,680)

time.sleep(0.0001)
pyautogui.dragTo(1055,680)

#DRAWING LEGS
time.sleep(0.0001)
pyautogui.moveTo(935,770)

time.sleep(0.0001)
pyautogui.dragTo(935,840)

time.sleep(0.0001)
pyautogui.dragTo(935,840)

time.sleep(0.0001)
pyautogui.dragTo(1015,840)

time.sleep(0.0001)
pyautogui.dragTo(1015,770)

time.sleep(0.0001)
pyautogui.moveTo(935,805)

time.sleep(0.0001)
pyautogui.dragTo(1015,805)

time.sleep(0.0001)
pyautogui.moveTo(975,825)

#DRAWING SASH
time.sleep(0.0001)
pyautogui.moveTo(935,725)

time.sleep(0.0001)
pyautogui.dragTo(1015,725)

time.sleep(0.0001)
pyautogui.moveTo(935,745)

time.sleep(0.0001)
pyautogui.dragTo(1015,745)

#DRAWING NECK
time.sleep(0.0001)
pyautogui.moveTo(945,640)

time.sleep(0.0001)
pyautogui.dragTo(945,660)

time.sleep(0.0001)
pyautogui.dragTo(955,660)

time.sleep(0.0001)
pyautogui.dragTo(955,670)

time.sleep(0.0001)
pyautogui.dragTo(995,670)

time.sleep(0.0001)
pyautogui.dragTo(995,660)

time.sleep(0.0001)
pyautogui.dragTo(1005,660)

time.sleep(0.0001)
pyautogui.dragTo(1005,640)

#DRAWING LEFT EYE
time.sleep(0.0001)
pyautogui.moveTo(945,590)

time.sleep(0.0001)
pyautogui.dragTo(945,610)

time.sleep(0.0001)
pyautogui.dragTo(970,610)

time.sleep(0.0001)
pyautogui.dragTo(970,590)

time.sleep(0.0001)
pyautogui.dragTo(945,590)

 #drawing line in eye
time.sleep(0.0001)
pyautogui.moveTo(960,590)

time.sleep(0.0001)
pyautogui.dragTo(960,610)

#DRAWING RIGHT EYE
time.sleep(0.0001)
pyautogui.moveTo(980,590)

time.sleep(0.0001)
pyautogui.dragTo(980,610)

time.sleep(0.0001)
pyautogui.dragTo(1003,610)

time.sleep(0.0001)
pyautogui.dragTo(1003,590)

time.sleep(0.0001)
pyautogui.dragTo(980,590)

#DRAWING LINE
time.sleep(0.0001)
pyautogui.moveTo(990,590)

time.sleep(0.0001)
pyautogui.dragTo(990, 610)

#DRAWING MOUTH
time.sleep(0.0001)
pyautogui.moveTo(965,620)

time.sleep(0.0001)
pyautogui.dragTo(965,630)

time.sleep(0.0001)
pyautogui.dragTo(985,630)

time.sleep(0.0001)
pyautogui.dragTo(985,620)

time.sleep(0.0001)
pyautogui.dragTo(965,620)

#DRAWING HAIR
time.sleep(0.0001)
pyautogui.moveTo(935,620)

time.sleep(0.0001)
pyautogui.dragTo(925,620)

time.sleep(0.0001)
pyautogui.dragTo(925,550)

time.sleep(0.0001)
pyautogui.dragTo(925,550)

time.sleep(0.0001)
pyautogui.dragTo(1025,550)

time.sleep(0.0001)
pyautogui.dragTo(1025,620)

time.sleep(0.0001)
pyautogui.dragTo(1045,620)

time.sleep(0.0001)
pyautogui.dragTo(1045,640)

time.sleep(0.0001)
pyautogui.moveTo(1015,630)

time.sleep(0.0001)
pyautogui.dragTo(1035,630)

time.sleep(0.0001)
pyautogui.dragTo(1035,640)

#------------PAINTING PART----------------------------
#pnt hair
time.sleep(0.0001)
for x in range(19):
    pyautogui.hotkey('tab')
    time.sleep(0.0001)
pyautogui.hotkey('enter')

for x in range(9):
    pyautogui.hotkey('tab')
    time.sleep(0.0001)

for x in range(4):
    pyautogui.hotkey('right')
    time.sleep(0.0001)
pyautogui.hotkey('enter')

time.sleep(0.0001)
pyautogui.moveTo(1018,615)

time.sleep(0.0001)
pyautogui.dragTo(1018,615)
pyautogui.click()

#pnt mouth
for x in range(27):
    pyautogui.hotkey('tab')
    time.sleep(0.0001)

pyautogui.hotkey('left')
time.sleep(0.0001)
pyautogui.hotkey('down')
pyautogui.hotkey('enter')

time.sleep(0.0001)
pyautogui.moveTo(967,627)

time.sleep(0.0001)
pyautogui.dragTo(967,627)
pyautogui.click()

#pnt eyes
for x in range(27):
    pyautogui.hotkey('tab')
    time.sleep(0.0001)

pyautogui.hotkey('up')
time.sleep(0.0001)

for x in range(3):
    pyautogui.hotkey('right')
    time.sleep(0.0001)
pyautogui.hotkey('enter')

time.sleep(0.0001)
pyautogui.moveTo(987,608)

time.sleep(0.0001)
pyautogui.dragTo(987,608)       
pyautogui.click()

time.sleep(0.0001)
pyautogui.moveTo(962,592)                                       
                                        
time.sleep(0.0001)
pyautogui.dragTo(962,592)
pyautogui.click()

#pnt sash
time.sleep(0.0001)
pyautogui.moveTo(938,728)                                       
                                        
time.sleep(0.0001)
pyautogui.dragTo(938,728)
pyautogui.click()

#pnt shirt
for x in range(27):
    pyautogui.hotkey('tab')
    time.sleep(0.0001)

pyautogui.hotkey('down')
pyautogui.hotkey('enter')

    #first part of shirt
time.sleep(0.0001)
pyautogui.moveTo(937,642)

time.sleep(0.0001)
pyautogui.dragTo(937,642)

    #second part
time.sleep(0.0001)
pyautogui.moveTo(937,747)

time.sleep(0.0001)
pyautogui.dragTo(937,747)
pyautogui.click()

#pnt arms, and face
for x in range(27):
    pyautogui.hotkey('tab')
    time.sleep(0.0001)

pyautogui.hotkey('left')
pyautogui.hotkey('enter')

    #drawing face
time.sleep(0.0001)
pyautogui.moveTo(937,637)

time.sleep(0.0001)
pyautogui.dragTo(937,637)
pyautogui.click()

    #drawing left arm
time.sleep(0.0001)
pyautogui.moveTo(897,737)

time.sleep(0.0001)
pyautogui.dragTo(897,737)
pyautogui.click()

    #drawing right arm
time.sleep(0.0001)
pyautogui.moveTo(1027,737)

time.sleep(0.0001)
pyautogui.dragTo(1027,737)
pyautogui.click()

#pnt neck
time.sleep(0.0001)
pyautogui.moveTo(947,657)

time.sleep(0.0001)
pyautogui.dragTo(947,657)
pyautogui.click()
#pnt pants
for x in range(27):
    pyautogui.hotkey('tab')
    time.sleep(0.0001)

for x in range(3):
    pyautogui.hotkey('left')
pyautogui.hotkey('enter')

    #brown part
time.sleep(0.0001)
pyautogui.moveTo(937,772)

time.sleep(0.0001)
pyautogui.dragTo(937,772)
pyautogui.click()

    #green part
for x in range(27):
    pyautogui.hotkey('tab')
    time.sleep(0.0001)
pyautogui.hotkey('left')
pyautogui.hotkey('up')
pyautogui.hotkey('enter')
time.sleep(0.0001)
pyautogui.moveTo(937,838)

time.sleep(0.0001)
pyautogui.dragTo(937,838)
pyautogui.click()

#WRITING SIGNATURE
time.sleep(0.0001)
for x in range(23):
    pyautogui.hotkey('tab')
    time.sleep(0.0001)
pyautogui.hotkey('enter')

for x in range(4):
    pyautogui.hotkey('tab')
    time.sleep(0.0001)
pyautogui.hotkey('left')
pyautogui.hotkey('enter')

#drawing I
time.sleep(0.0001)
pyautogui.moveTo(1040,825)

time.sleep(0.0001)
pyautogui.dragTo(1040,845)

#drawing M
time.sleep(0.0001)
pyautogui.moveTo(1050,825)

time.sleep(0.0001)
pyautogui.dragTo(1050,845)

time.sleep(0.0001)
pyautogui.moveTo(1050,825)

time.sleep(0.0001)
pyautogui.dragTo(1060,825)

time.sleep(0.0001)
pyautogui.dragTo(1060,835)

time.sleep(0.0001)
pyautogui.moveTo(1060,825)

time.sleep(0.0001)
pyautogui.dragTo(1070,825)

time.sleep(0.0001)
pyautogui.dragTo(1070,845)
