# 导入系统资源模块
from ascript.android.system import R
# 导入动作模块
from ascript.android import action
# 导入图色检索模块
from ascript.android import screen
from ascript.android.screen import FindColors

# 获取屏幕信息
from ascript.android.system import Device

import time

display = Device.display()
width = display.widthPixels
height = display.heightPixels
density = display.density
in_battle = False
print("屏幕密度：",density)
print("屏幕宽度：",width)
print("屏幕高度：",height)

def highStar():
    print("抓四星")
    global in_battle
    while True:
        # 检索自动战斗键
        FB = FindColors.find("195,783,#FFD36E|202,792,#FFDA73",rect=[126,724,282,875])
        if FB:
            # isEncounter = False
            in_battle = False
            action.click(FB)
            time.sleep(1)

        # 检索自动战斗确认键
        FB2 = FindColors.find("1817,777,#FAC479|1854,790,#FCC97A|1876,794,#675246|1824,811,#FEDB89",rect=[1618,618,2088,1031])
        if FB2:
            action.click(FB2)
            time.sleep(3)

        # 检索停止自动战斗键
        stop_FB = FindColors.find("1475,376,#FEFCE6|1493,373,#FFFCE6|1477,387,#FFFCE6|1493,388,#FFFCE6",rect=[1305,260,1789,476])
        if stop_FB:
            action.click(stop_FB)
            time.sleep(1)
            in_battle = True
        if in_battle:
            # if isEncounter or FindColors.find("782,661,#FFFFBD|788,652,#554411",rect=[742,588,831,700]):
            #     isEncounter = True
            #     action.click(1014,983,100)
            #     time.sleep(1)
            if FindColors.find("782,661,#FFFFBD|788,652,#554411",rect=[1685,610,1801,703]):
                break
            else:
                action.click(712,986,100)
            time.sleep(1)
        else:
            print("回到主界面后再打开脚本")

        # 技能替换提示，检索取消键
        newlearn = FindColors.find("1468,941,#FDDDA6|1599,947,#FFDFA9",rect=[1379,867,1693,1016])
        if newlearn:
            action.click(newlearn)
