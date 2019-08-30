import pyautogui
import pygetwindow as gw
import time
dispatch = gw.getWindowsWithTitle('Xpert IT Solutions - Transport Dispatch - [Dispatch Board - 2449285 ONTARIO INC/TRAVEL TRANSPORT]')[0]
dispatch.minimize()
dispatch.restore()
dispatch.maximize()
if (dispatch.isActive is True):
    while True:
            str = pyautogui.prompt('Enter Load Number to check status:')
            pyautogui.click(160, 650,2)
            pyautogui.typewrite(str)
            pyautogui.click(180, 610)