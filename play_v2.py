import pyautogui as gui
import keyboard
import time
import math
import cv2
import numpy as np

# Screen Dimensions for screen of size 1920X1080
top, left, width, height = 293, 0, 700, 465

# 200,550,255,250
                  
# helper variables to calculate time
last = 0
total_time = 0

# the intervals where the bot will search for obstacles
y_search_cactus, x_start, x_end = 350, 350, 380
y_search_bird = 275 # for the birds


time.sleep(4)
while True:
    t1 = time.time()
    if keyboard.is_pressed('q'): # Emergency Button
        break

    # increase the search width every second to simulate the dino acceleration
    if math.floor(total_time) != last:
        x_end += 4
        if x_end >= width:                                                       
            x_end = width
        last = math.floor(total_time)

    # Get a screen shot
    screenshot = gui.screenshot(region=(left,top, width, height))
    pixels = screenshot.load()

    image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    # cv2.imshow('image',image)
    # if cv2.waitKey(25) & 0xFF == ord('q'):
    #     cv2.destroyAllWindows()
    #     break

    background_color = pixels[440, 30]

    for i in reversed(range(x_start, x_end)):
        if pixels[i, y_search_cactus] != background_color\
                or pixels[i, y_search_bird] != background_color:
            keyboard.press(' ') # jump
            break

    t2 = time.time()-t1
    total_time += t2