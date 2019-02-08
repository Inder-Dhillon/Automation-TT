import pyautogui
import pygetwindow as gw
import time
dispatch = gw.getWindowsWithTitle('Xpert IT Solutions - Transport Dispatch - [Dispatch Board - TRAVEL TRANSPORT]')[0]
dispatch.restore()
dispatch.maximize()
if (dispatch.isActive is True):
    while True:
            str = pyautogui.prompt('Enter Load Number to check status:')
            pyautogui.click(160, 650,2)
            pyautogui.typewrite(str)
            pyautogui.click(180, 610)
            time.sleep(0.5)
            im = pyautogui.screenshot()
            if pyautogui.pixelMatchesColor(1654,182,(0, 120, 215)):
                pyautogui.alert("Load Not Delivered")
            if pyautogui.pixelMatchesColor(1654,182,(255, 212, 229)):
                pyautogui.alert("Load Not Invoiced")
            if pyautogui.pixelMatchesColor(1654,182,(255, 255, 255)):
                pyautogui.alert("Load Invoiced")