import pyautogui
import pygetwindow as gw
import re
import time
dispatch = gw.getWindowsWithTitle('Xpert IT Solutions - Transport Dispatch - [Dispatch Board - 2449285 ONTARIO INC/TRAVEL TRANSPORT]')[0]
dispatch.minimize()
dispatch.restore()
dispatch.maximize()
time.sleep(1)
if (dispatch.isActive is True):
    str = pyautogui.prompt('Enter Invoice Numbers (dot-seperated)')
    num_of_orders = str.count('.') + 1
    list_orders = str.split(".")
    for x in range(num_of_orders):
        pyautogui.click(145, 650, 2)
        pyautogui.typewrite(list_orders[x])
        pyautogui.click(190, 606)
        time.sleep(1)
        pyautogui.click(400, 180)
        time.sleep(1)
        pyautogui.click(70, 373)
        time.sleep(1)
        pyautogui.click(325, 320, button='right')
        time.sleep(1)
        pyautogui.click(398, 396)
        time.sleep(2)
        pyautogui.click(290, 490)
        time.sleep(2)
        pyautogui.click(1905, 30)
        time.sleep(1)
        pyautogui.click(225, 110)




