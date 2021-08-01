from pyautogui import press, typewrite, hotkey
from time import sleep

DELAY=5

instruction1='''make sure first page of magna is opened and enter the number of pages in this chapter:'''
pages=int(input(instruction1))
instruction2='''how many page downs to press on a single page:'''
downs_per_page=int(input(instruction2))+1
hotkey('alt', 'tab') # switch to browser
for i in range(pages):
    for j in range(downs_per_page):
        sleep(DELAY)
        press('pagedown')
    press('right')
#typewrite('quick brown fox')
