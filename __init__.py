# __init__.py 为初始化加载文件

# 导入系统资源模块
from ascript.android.system import R

# 获取屏幕信息
from ascript.android.system import Device
from ascript.android.ui import WebWindow
from ascript.android.screen import FindColors

import json
import time

from .main.function import highStar
from .main.function import levelUp
from .main.function import xinghun
from .main.function.activities import mengjing

display = Device.display()
width = display.widthPixels
height = display.heightPixels

values = {}
isPadding = False

def start():
    def tunnel(k, v):
        global values
        global isPadding
        values = json.loads(v)
        print(f"Received from HTML: {values}")
        w.close()
        if values['UI'] == 'unpadding':
            isPadding = False
        else:
            isPadding = True

        #星魂
        if values["choice"] == 'soul':
            if values['1']:
                if isPadding:
                    xinghun.xinghunP(0,values['upgradeCount'])
                else:
                    xinghun.xinghun(0,values['upgradeCount'])

            if values['2']:
                if isPadding:
                    xinghun.xinghunP(1,values['upgradeCount'])
                else:
                    xinghun.xinghun(1,values['upgradeCount'])
          
            if values['3']:
                if isPadding:
                    xinghun.xinghunP(2,values['upgradeCount'])
                else:
                    xinghun.xinghun(2,values['upgradeCount'])
          
            if values['4']:
                if isPadding:
                    xinghun.xinghunP(3,values['upgradeCount'])
                else:
                    xinghun.xinghun(3,values['upgradeCount'])
        
            if values['5']:
                if isPadding:
                    xinghun.xinghunP(4,values['upgradeCount'])
                else:
                    xinghun.xinghun(4,values['upgradeCount'])
          
        #升级
        if values['choice'] == 'upgrade':
            if isPadding:
                levelUp.levelUpP(values['upgradeCount'])
            else:
                levelUp.levelUp(values['upgradeCount'])

        if values['choice'] == 'dream':
            mengjing.start(values['upgradeCount'])

    w = WebWindow(R.ui('a.html'),tunnel)
    print("加载网页")
    w.mode(1)
    w.show()


start()



