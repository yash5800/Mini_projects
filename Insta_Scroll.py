#To use it run this code and click on the app
import pyautogui #make sure to install pyautogui in your device using 'pip install pyautogui'
import time
import random
Times = [5,10,15] #change time if you want to 'Note:it is seconds'
while True:
    time.sleep(random.choice(Times)) 
    pyautogui.press('space')      
