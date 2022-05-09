import pyautogui as pag
import time
import pyperclip

icon = (951 , 1063)
newProf = (1594 , 153)
proxy = (132 , 240)
conType = (485 , 164)
http = (473 , 250)
ipPort = (530 , 253)
crt = (1796 , 679)
selectAll = (414 , 153)
action = (621 , 149)
startSelectedProfile = (750 , 171)

it = 6
cnt = 10
start = it*cnt
end = start+cnt
filename = "demo.txt"
j = 0
f = open(filename, "r")

pag.click(icon)
time.sleep(0.5)

for i in range((start), (end)):
    if(j == 0):
        while(j != i):
            x = f.readline()
            j += 1
        j = -1

    ip = f.readline()

    pyperclip.copy(ip)
    pag.click(newProf)
    time.sleep(0.5)

    pag.click(proxy)
    time.sleep(0.5)

    pag.click(conType)
    time.sleep(0.5)

    pag.click(http)
    time.sleep(0.5)

    pag.click(ipPort)
    time.sleep(0.5)

    pag.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pag.click(crt)
    time.sleep(0.5)

pag.click(selectAll)
time.sleep(0.7)
pag.click(action)
time.sleep(0.7)
pag.click(startSelectedProfile)
time.sleep(0.7)