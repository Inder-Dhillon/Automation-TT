import pyautogui
import pygetwindow as gw
import time
dispatch = gw.getWindowsWithTitle('Xpert IT Solutions - Transport Dispatch - [Dispatch Board - TRAVEL TRANSPORT]')[0]
dispatch.restore()
dispatch.maximize()
time.sleep(1)
if (dispatch.isActive is True):
      pyautogui.click(75,105)
      pyautogui.click(515,215)
      pyautogui.typewrite('Woodbridge')
      pyautogui.click(120,190)
      pyautogui.click(890,230)
      pyautogui.typewrite('RY')
      pyautogui.typewrite(pyautogui.prompt('Enter RY Number'))
      pyautogui.click(920,265)
      pyautogui.typewrite(pyautogui.prompt('Enter Rate'))
      pyautogui.click(490,160)
      pyautogui.click(450,500)
      pyautogui.typewrite('Woodbridge')
      pyautogui.click(125,190)
      pyautogui.click(550,500,4)
      pyautogui.typewrite(pyautogui.prompt('Enter Date'))
      pyautogui.click(590,160)
      pyautogui.alert('Enter Recievers')
      pyautogui.click(572,518,4)
      pyautogui.typewrite(pyautogui.prompt('Enter Date'))
      pyautogui.click(45, 110)

# else:
#       if (dispatch.isActive is True):
#             pyautogui.click(75, 105)
#             pyautogui.click(515, 215)
#             pyautogui.typewrite(pyautogui.prompt('Enter Customer'))
#             time.sleep(4)
#             pyautogui.click(890, 230)
#             pyautogui.typewrite(pyautogui.prompt('Enter Load#'))
#             pyautogui.click(920, 265)
#             pyautogui.typewrite(pyautogui.prompt('Enter Rate'))
#             pyautogui.click(490, 160)
#             pyautogui.click(450, 500)
#             pyautogui.typewrite(pyautogui.prompt('Enter Shipper'))
#             time.sleep(4)
#             pyautogui.click(550, 500, 4)
#             pyautogui.typewrite(pyautogui.prompt('Enter Date'))
#             pyautogui.click(590, 160)
#             pyautogui.alert('Enter Recievers')
#             pyautogui.click(572, 518, 4)
#             pyautogui.typewrite(pyautogui.prompt('Enter Date'))
#             # pyautogui.click(45, 110)





