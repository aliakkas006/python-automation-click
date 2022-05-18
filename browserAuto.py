import pyautogui
import time
import pyperclip

pyperclip.copy("https://internetoffer24.com/offer/")

browser_pos = 970
link_pos_y = 433

for i in range(0, 10):

    pyautogui.click(browser_pos , 1050)
    time.sleep(0.5)
    browser_pos += 54

    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)

    pyautogui.press('enter')
    time.sleep(10)

    pyautogui.click(170 , link_pos_y)
    time.sleep(1)
    link_pos_y += 62



