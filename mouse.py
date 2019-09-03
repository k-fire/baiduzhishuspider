import pyautogui

while True:
    screenWidth, screenHeight = pyautogui.size()  #获取屏幕的尺寸
    x,y = pyautogui.position()   #获取当前鼠标的位置
    print("[!]当前鼠标坐标：           ",end='\r')
    print("[!]当前鼠标坐标：%s , %s"%(x,y),end='\r')
