# __init__.py 为初始化加载文件

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
from time import sleep

c = action.click

display = Device.display()
width = display.widthPixels
height = display.heightPixels
in_battle = False


def levelUpP(times):
    print("升级")
    global in_battle
    count = 0
    while True: 
        # int(width * 0.05),int(height * 0.65),int(width * 0.12),int(height * 0.80)
        # 检索自动战斗键
        FB = FindColors.find("195,783,#FFD36E|202,792,#FFDA73",rect=[int(width * 0.00),int(height * 0.63),int(width * 0.12),int(height * 0.80)])
        if FB:
            if count >= times:
                break
            in_battle = False
            action.click(FB)
            time.sleep(1)

        # 检索自动战斗确认键
        FB2 = FindColors.find("1817,777,#FAC479|1854,790,#FCC97A|1876,794,#675246|1824,811,#FEDB89",rect=[int(width * 0.68),int(height * 0.57),int(width * 0.88),int(height * 0.95)])
        if FB2:
            action.click(FB2)
            count += 1
            print(f"升级第 ",count," 次")
            time.sleep(3)
        
        # 检索停止自动战斗键(穿插战斗技能选择)
        stop_FB = FindColors.find("1475,376,#FEFCE6|1493,373,#FFFCE6|1477,387,#FFFCE6|1493,388,#FFFCE6",rect=[int(width * 0.55),int(height * 0.24),int(width * 0.76),int(height * 0.44)])
        if stop_FB:
            action.click(stop_FB)
            time.sleep(1)
            in_battle = True

        huihe = FindColors.find("964,43,#FFFFFF",rect=[int(width * 0.47),int(height * 0.01),int(width * 0.54),int(height * 0.09)])
        battle_win = FindColors.find("1653,215,#FDE87B|1688,214,#FDE87B",rect=[int(width * 0.54),int(height * 0.08),int(width * 0.87),int(height * 0.38)])
        click_return = FindColors.find("795,1035,#FEF1A4|1099,1035,#FFF2A5",rect=[725,977,1155,1070],diff=0.8)
        if not huihe and click_return:
            print("检索到返回键")
            action.click(click_return)
            in_battle = False
            time.sleep(2)

        if in_battle:
            action.click(int(width * 0.30),int(height * 0.91))
            time.sleep(3)
            
        # 技能替换提示，检索取消键
        newlearn = FindColors.find("1468,941,#FDDDA6|1599,947,#FFDFA9",rect=[int(width * 0.58),int(height * 0.80),int(width * 0.71),int(height * 0.94)])
        if newlearn:
            print("检索到替换技能")
            c(newlearn)
            sleep(2)
                


def levelUp(times):
    print("升级")
    global in_battle
    count = 0
    while True: # 3物防
        # 检索自动战斗键
        FB = FindColors.find("195,783,#FFD36E|202,792,#FFDA73",rect=[int(width * 0.00),int(height * 0.63),int(width * 0.12),int(height * 0.80)])
        if FB:
            if count >= times:
                break
            in_battle = False
            action.click(FB)
            time.sleep(1)

        # 检索自动战斗确认键
        FB2 = FindColors.find("1584,791,#675246|1664,834,#FFFD9E",rect=[int(width * 0.63),int(height * 0.62),int(width * 0.94),int(height * 0.88)])
        if FB2:
            action.click(FB2)
            count += 1
            print(f"升级第 ",count," 次")
            time.sleep(3)
        
        # 检索停止自动战斗键(穿插战斗技能选择)
        stop_FB = FindColors.find("1267,381,#FFFCE6|1282,382,#FFFCE6",rect=[int(width * 0.61),int(height * 0.27),int(width * 0.77),int(height * 0.42)])
        if stop_FB:
            action.click(stop_FB)
            time.sleep(1)
            in_battle = True
        
        huihe = FindColors.find("964,43,#FFFFFF",rect=[int(width * 0.47),int(height * 0.01),int(width * 0.54),int(height * 0.09)])
        battle_win = FindColors.find("1653,215,#FDE87B|1688,214,#FDE87B",rect=[int(width * 0.57),int(height * 0.07),int(width * 0.97),int(height * 0.43)])
        click_return = FindColors.find("795,1035,#FEF1A4|1099,1035,#FFF2A5",rect=[725,977,1155,1070],diff=0.95)
        # sleep(0.5)
        if not huihe and click_return:
            in_battle = False
            print("检索到返回键")
            action.click(click_return)
            time.sleep(2)
            
        # 技能替换提示，检索取消键
        newlearn = FindColors.find("1468,941,#FDDDA6|1599,947,#FFDFA9",rect=[int(width * 0.58),int(height * 0.80),int(width * 0.71),int(height * 0.94)])
        if newlearn:
            print("检索到替换技能")
            c(newlearn)
            sleep(2)

        if in_battle:
            action.click(int(width * 0.30),int(height * 0.91))
            time.sleep(3)


    
# if FloatWindow.add_menu("1",R.img("level.png"),levelUp,False):
#     print("等级模块添加成功")
# if FloatWindow.add_menu("2",R.img("hun.png"),xinghun,True):
#     print("星魂模块添加成功")

# # 物攻，魔攻，物防，魔防，体力，速度
# xhLsit = [0,0,0,0,0,0]

# def tunnel(k, v):
#     if k == 'radioValues':
#         values = json.loads(v)
#         print(f"Received from HTML: {values}")

# # w = WebWindow(R.ui('a.html'),tunnel)
# # w.mode(1)
# # w.show()

