import pyautogui as pg
import time
import keyboard as kb

def pause():
    while True:
        if kb.is_pressed('enter'):
            time.sleep(0.1)
            break

time.sleep(5)
with open("ans.txt", 'r') as f:
    for i in f.readlines():
        i = i.strip().replace('\n', '')
        if i == 'pause':
            pause()
        else:
            pg.write(i)
            pg.press('enter')
        time.sleep(0.01)

print("Successful!...")
