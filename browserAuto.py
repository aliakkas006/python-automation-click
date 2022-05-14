import pyautogui
import time
import pyperclip

browser_pos = 948
link_pos_y = 433

filename = "https://internetoffer24.com/offer/"
pyperclip.copy(filename)
j = 0

for i in range(0, 10):
    if(j == 0):
        while(j != i):
            j += 1
        j = -1

    pyautogui.click(browser_pos , 1052)
    time.sleep(1)
    browser_pos += 55

    pyautogui.click(293 , 85)
    time.sleep(1)

    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

    pyautogui.press('enter')
    time.sleep(10)

    pyautogui.click(170 , link_pos_y)
    time.sleep(1)
    link_pos_y += 62