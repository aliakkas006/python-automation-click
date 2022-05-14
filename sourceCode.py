import pyautogui
import time
import pyperclip

it = 20
cnt = 10
start = it*cnt
end = start+cnt
filename = "demo1.txt"
j = 0
f = open(filename, "r")

pyautogui.click(951 , 1063)
time.sleep(0.5)

for i in range((start), (end)):
    if(j == 0):
        while(j != i):
            x = f.readline()
            j += 1
        j = -1

    ip = f.readline()

    pyperclip.copy(ip)
    pyautogui.click(1594 , 153)
    time.sleep(0.5)
    pyautogui.click(132 , 240)
    time.sleep(0.5)
    pyautogui.click(485 , 164)
    time.sleep(0.5)
    pyautogui.click(473 , 250)
    time.sleep(0.5)
    pyautogui.click(530 , 253)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.click(1796 , 679)
    time.sleep(0.5)


pyautogui.click(414 , 153)
time.sleep(0.7)
pyautogui.click(621 , 149)
time.sleep(0.7)
pyautogui.click(750 , 171)
time.sleep(0.7)