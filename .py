import random
import pyautogui as pg
import time
Input=random.randrange(a,z)
time.sleep(5)
for i in range(50):
    pg.write(Input)
    pg.press('enter')