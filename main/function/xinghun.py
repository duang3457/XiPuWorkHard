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

from . import levelUp

import time
from time import sleep
c = action.click

display = Device.display()
width = display.widthPixels
height = display.heightPixels
in_battle = False


# area1x = [int(width * 0.54),int(width * 0.65)]
# area1y = [int(height * 0.30),int(height * 0.54)]
# area2x = [int(width * 0.67),int(width * 0.74)]
# area2y = [int(height * 0.30),int(height * 0.51)]
_list = ["回音蟹（物防）","游戏小熊（魔攻）","浮水波尼（魔防）","兔宝（速度）","圣山之巅（物攻+体力）"]

# 检索6大星魂怪
def checkPokemon(index):
    if index == 0:  # 回音蟹（物防）
        return FindColors.find("1428,436,#FCE7B1|1430,464,#FFBC58|1431,502,#584131",rect=[int(width * 0.54),int(height * 0.29),int(width * 0.84),int(height * 0.56)])
    elif index == 1: # 游戏小熊（魔攻）
        return FindColors.find("1402,433,#FFD46B|1414,455,#F966B7|1451,494,#584131",rect=[int(width * 0.55),int(height * 0.29),int(width * 0.84),int(height * 0.56)])
    elif index == 2: # 浮水波尼（魔防）
        return FindColors.find("1370,467,#66A1E2|1447,425,#584131",rect=[int(width * 0.55),int(height * 0.29),int(width * 0.84),int(height * 0.56)])
    elif index == 3: # 兔宝（速度）
        return FindColors.find("1651,423,#99E06A|1668,423,#584131|1710,421,#99E06A",rect=[int(width * 0.55),int(height * 0.29),int(width * 0.84),int(height * 0.56)])
    
# 检索自动战斗中pokemon选项
def xhadjust(p_index):
    # 圣山之巅不用检查
    if p_index == 4:
        return
    time.sleep(2)
    pokemon_pos = checkPokemon(p_index)
    if pokemon_pos:
        # 检索第一区域对勾
        temp1 = FindColors.find("1491,551,#FFEE83|1502,563,#FFF98A|1514,563,#675246",rect=[int(width * 0.61),int(height * 0.45),int(width * 0.70),int(height * 0.55)])
        # 检索第二区域对勾
        temp2 = FindColors.find("1754,550,#FFEC83|1763,560,#FFF689|1779,562,#675246",rect=[int(width * 0.71),int(height * 0.44),int(width * 0.83),int(height * 0.57)])
        if pokemon_pos.x < int(width*0.68):
            print(f"{_list[p_index]}在第一区域")
            if temp1:
                print(f"{_list[p_index]}已勾选")
                if temp2:
                    action.click(temp2)
                    time.sleep(1)
                    print("取消第二区域")
                else:
                    print("第二区域未勾选")
            else:
                action.click(FindColors.find("1491,542,#675246|1509,544,#675246|1511,562,#675246",rect=[int(width * 0.61),int(height * 0.45),int(width * 0.70),int(height * 0.56)]))
                print(f"{_list[p_index]}勾选")
                if temp2:
                    time.sleep(0.5)
                    action.click(temp2)
                    time.sleep(1)
                    print("取消第二区域")
                else:
                    print("第二区域未勾选")
        else:
            print(f"{_list[p_index]}在第二区域")
            if temp2:
                print(f"{_list[p_index]}已勾选")
                if temp1:
                    action.click(temp1)
                    time.sleep(1)
                    print("取消第一区域")
                else:
                    print("第一区域未勾选")
            else:
                action.click(FindColors.find("1756,543,#675246|1777,543,#665246|1776,564,#665246",rect=[int(width * 0.71),int(height * 0.44),int(width * 0.83),int(height * 0.57)]))
                print(f"{_list[p_index]}勾选")
                if temp1:
                    time.sleep(0.5)
                    action.click(temp1)
                    time.sleep(1)
                    print("取消第一区域")
                else:
                    print("第一区域未勾选")

    else:
        print("未检索到怪物")

def toAddressP(p_index): 
    action.click(int(width * 0.86),int(height * 0.91),200)
       
    time.sleep(3)
    if p_index == 0 or p_index == 1:
        action.slide(int(width * 0.11),int(height * 0.72),int(width * 0.38),int(height * 0.54),800) # 向左下
        action.slide(int(width * 0.11),int(height * 0.72),int(width * 0.38),int(height * 0.54),800) # 向左下
        time.sleep(1)
        action.click(int(width * 0.41),int(height * 0.70),500) # 点击诺亚方舟
        time.sleep(2)
        action.click(int(width * 0.80),int(height * 0.26),100) # 点击居民区三层
        print(int(width * 0.79),int(height * 0.26))
        time.sleep(4)
        print("来到居民区三层")
    elif p_index == 2 or p_index == 3:
        action.slide(int(width * 0.11),int(height * 0.72),int(width * 0.38),int(height * 0.54),800) # 向左下
        action.slide(int(width * 0.11),int(height * 0.72),int(width * 0.38),int(height * 0.54),800) # 向左下
        time.sleep(1)
        action.click(int(width * 0.66),int(height * 0.29),500) # 敬意之湖
        time.sleep(2)
        action.click(int(width * 0.69),int(height * 0.46),100) # 点击晨光果园
        time.sleep(4)
        print("来到晨光果园")
    else:
        action.slide(int(width * 0.86),int(height * 0.21),int(width * 0.61),int(height * 0.54),800) # 向右上
        action.slide(int(width * 0.86),int(height * 0.21),int(width * 0.61),int(height * 0.54),800) # 向右上
        time.sleep(1)
        action.click(int(width * 0.37),int(height * 0.22),500) #飞岩群山
        time.sleep(2)
        action.slide(int(width * 0.90),int(height * 0.19),int(width * 0.89),int(height * 0.77),800) # 向下
        action.slide(int(width * 0.90),int(height * 0.19),int(width * 0.89),int(height * 0.77),800) # 向下
        time.sleep(1)
        action.click(int(width * 0.51),int(height * 0.14),100) # 点击圣山之巅
        time.sleep(4)
        print("来到圣山之巅")
   
def toAddress(p_index): 
    time.sleep(0.5)
    action.click(int(width * 0.86),int(height * 0.90),200)
    
    time.sleep(3)
    if p_index == 0 or p_index == 1:
        action.slide(int(width * 0.11),int(height * 0.72),int(width * 0.68),int(height * 0.24),800) # 向左下
        time.sleep(0.5)
        action.slide(int(width * 0.11),int(height * 0.72),int(width * 0.68),int(height * 0.24),800) # 向左下
        time.sleep(1)
        action.click(int(width * 0.5),int(height * 0.70),500) # 点击诺亚方舟
        time.sleep(2)
        action.click(int(width * 0.87),int(height * 0.27),100) # 点击居民区三层
        time.sleep(4)
        print("来到居民区三层")
    elif p_index == 2 or p_index == 3:
        action.slide(int(width * 0.11),int(height * 0.72),int(width * 0.68),int(height * 0.24),800) # 向左下
        time.sleep(0.5)
        action.slide(int(width * 0.11),int(height * 0.72),int(width * 0.68),int(height * 0.24),800) # 向左下
        time.sleep(1)
        action.click(int(width * 0.81),int(height * 0.25),500) # 敬意之湖
        time.sleep(2)
        action.click(int(width * 0.76),int(height * 0.47),100) # 点击晨光果园
        time.sleep(4)
        print("来到晨光果园")
    else:
        action.slide(int(width * 0.86),int(height * 0.21),int(width * 0.41),int(height * 0.54),500) # 向右上
        time.sleep(0.5)
        action.slide(int(width * 0.86),int(height * 0.21),int(width * 0.41),int(height * 0.54),500) # 向右上
        time.sleep(1)
        action.click(int(width * 0.24),int(height * 0.27),500) #飞岩群山
        time.sleep(2)
        action.slide(int(width * 0.90),int(height * 0.19),int(width * 0.89),int(height * 0.77),500) # 向下
        action.slide(int(width * 0.90),int(height * 0.19),int(width * 0.89),int(height * 0.77),500) # 向下
        time.sleep(1)
        action.click(int(width * 0.53),int(height * 0.16),100) # 点击圣山之巅
        time.sleep(4)
        print("来到圣山之巅")


alr_in_0 = False
alr_in_2 = False
def xinghunP(pokemon_index,times):
    print(f"现在去打{_list[pokemon_index]}星魂")
    global alr_in_0
    global alr_in_2
    if alr_in_0 and pokemon_index == 1:
        print("已经在居民区三层")
    elif alr_in_2 and pokemon_index == 3:
        print("已经在晨光果园")
    else:
        time.sleep(1)
        toAddressP(pokemon_index)
    if pokemon_index == 0:
        alr_in_0 = True
    if pokemon_index == 2:
        alr_in_2 = True
    print(f"来到{_list[pokemon_index]}的地图")

    if pokemon_index == 4:
        levelUp.levelUpP(times)
        return
 
    global in_battle
    close1Num = 0
    pokemon_pos = None
    battle_win = None
    FB = None
    # 先打开一次自动战斗
    while not FB:
        FB = FindColors.find("195,783,#FFD36E|202,792,#FFDA73",rect=[int(width * 0.05),int(height * 0.65),int(width * 0.12),int(height * 0.80)])
        if FB:
            in_battle = False
            action.click(FB)
            close1Num += 1
            print(f"{_list[pokemon_index]} ",close1Num," 次")
            time.sleep(1)
    
    # 选择自动战斗中所需怪物选项
    xhadjust(pokemon_index)

    # 检索自动战斗确认键
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
        FB2 = FindColors.find("1817,777,#FAC479|1854,790,#FCC97A|1876,794,#675246|1824,811,#FEDB89",rect=[int(width * 0.68),int(height * 0.57),int(width * 0.88),int(height * 0.95)])
        if FB2:
            action.click(FB2)
            time.sleep(3)
        
        # 检索停止自动战斗键(穿插战斗技能选择)
        stop_FB = FindColors.find("1475,376,#FEFCE6|1493,373,#FFFCE6|1477,387,#FFFCE6|1493,388,#FFFCE6",rect=[int(width * 0.55),int(height * 0.24),int(width * 0.76),int(height * 0.44)])
        if stop_FB:
            action.click(stop_FB)
            time.sleep(1)
            in_battle = True
        
        huihe = FindColors.find("964,43,#FFFFFF",rect=[int(width * 0.47),int(height * 0.01),int(width * 0.54),int(height * 0.09)])
        battle_win = FindColors.find("1653,215,#FDE87B|1688,214,#FDE87B",rect=[int(width * 0.54),int(height * 0.08),int(width * 0.87),int(height * 0.38)])
        if not huihe and battle_win:
            print("战斗胜利")
            time.sleep(5)
            action.click(int(width * 0.30),int(height * 0.91))
            in_battle = False
            close1Num += 1
            print(f"{_list[pokemon_index]} ",close1Num," 次")
            time.sleep(2)

        if in_battle:
            time.sleep(1)
            action.click(int(width * 0.30),int(height * 0.91))
            
        for _ in range(6):
            # 技能替换提示，检索取消键
            newlearn = FindColors.find("1468,941,#FDDDA6|1599,947,#FFDFA9",rect=[int(width * 0.58),int(height * 0.80),int(width * 0.71),int(height * 0.94)])
            if newlearn:
                action.click(newlearn)
            # 新技能提示，检索当前技能字样
            newlearn2 = FindColors.find("1371,486,#6C6975|1407,410,#FFFF9B|1429,486,#FFFFFF|1593,489,#6F6B75",rect=[1182,396,1729,568],diff=0.7,ori= 1)
            if newlearn2:
                print("检索到新技能")
                c(int(width * 0.50),int(height * 0.86))
                sleep(2)

    print(f"{_list[pokemon_index]}星魂已打完")
    time.sleep(2)


def xinghun(pokemon_index,times):
    print(f"现在去打{_list[pokemon_index]}星魂")
    global alr_in_0
    global alr_in_2
    if alr_in_0 and pokemon_index == 1:
        print("已经在居民区三层")
    elif alr_in_2 and pokemon_index == 3:
        print("已经在晨光果园")
    else:
        time.sleep(1)
        toAddress(pokemon_index)
    if pokemon_index == 0:
        alr_in_0 = True
    if pokemon_index == 2:
        alr_in_2 = True
    print(f"来到{_list[pokemon_index]}的地图")

    if pokemon_index == 4:
        levelUp.levelUp(times)
        return
 
    global in_battle
    close1Num = 0
    pokemon_pos = None
    battle_win = None
    FB = None
    # 先打开一次自动战斗
    while not FB:
        FB = FindColors.find("195,783,#FFD36E|202,792,#FFDA73",rect=[int(width * 0.00),int(height * 0.63),int(width * 0.12),int(height * 0.80)])
        if FB:
            in_battle = False
            action.click(FB)
            close1Num += 1
            print(f"{_list[pokemon_index]} ",close1Num," 次")
            time.sleep(1)
    
    # 选择自动战斗中所需怪物选项
    xhadjust(pokemon_index)
    count = 0
    # 检索自动战斗确认键
    while True: 
        # 检索自动战斗键
        FB = FindColors.find("195,783,#FFD36E|202,792,#FFDA73",rect=[int(width * 0.00),int(height * 0.63),int(width * 0.12),int(height * 0.80)])
        if FB:
            if count >= times:
                break
            in_battle = False
            action.click(FB)
            time.sleep(1)

        # 检索自动战斗确认键
        FB2 = FindColors.find("1584,791,#675246|1664,834,#FFFD9E",rect=[int(width * 0.63),int(height * 0.62),int(width * 0.94),int(height * 0.88)],diff=0.9)
        if FB2:
            action.click(FB2)
            count += 1
            print(f"{_list[pokemon_index]} ",count," 次")
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
        # time.sleep(0.5)
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
            time.sleep(2)


    print(f"{_list[pokemon_index]}星魂已打完")
    time.sleep(2)



# if FloatWindow.add_menu("1",R.img("level.png"),levelUp,False):
#     print("等级模块添加成功")
# if FloatWindow.add_menu("2",R.img("hun.png"),xinghun,True):
#     print("星魂模块添加成功")

# 物攻，魔攻，物防，魔防，体力，速度
# xhLsit = [0,0,0,0,0,0]



