import pyautogui as pag
import time
import pyperclip

time.sleep(8)
print(pag.position().x,",", pag.position().y)
pag.confirm('This displays text and has an OK and Cancel button.')