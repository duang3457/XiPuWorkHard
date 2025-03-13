#这里是星魂模块

from ascript.android.system import R
from ascript.android import action
from ascript.android import screen
from ascript.android.screen import FindColors
from ascript.android.system import Device

from . import levelUp

import time
from time import sleep

rect = __import__(R.name+".main.utils.rect",fromlist=[''])
battle = __import__(R.name+".main.function.basic.battle",fromlist=[''])
rc = rect.rc1920

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
# 大范围，适合两种机型
def checkPokemon(index):
    if index == 0:  # 回音蟹（物防）
        return FindColors.find("1428,436,#FCE7B1|1430,464,#FFBC58|1431,502,#584131",rect=[int(width * 0.54),int(height * 0.29),int(width * 0.84),int(height * 0.56)])
    elif index == 1: # 游戏小熊（魔攻）
        return FindColors.find("1402,433,#FFD46B|1414,455,#F966B7|1451,494,#584131",rect=[int(width * 0.55),int(height * 0.29),int(width * 0.84),int(height * 0.56)])
    elif index == 2: # 浮水波尼（魔防）
        return FindColors.find("1370,467,#66A1E2|1447,425,#584131",rect=[int(width * 0.55),int(height * 0.29),int(width * 0.84),int(height * 0.56)])
    elif index == 3: # 兔宝（速度）
        return FindColors.find("1651,423,#99E06A|1668,423,#584131|1710,421,#99E06A",rect=[int(width * 0.55),int(height * 0.29),int(width * 0.84),int(height * 0.56)],diff=0.9)
    # elif index == 5: # 哈尼熊
    #     return FindColors.find("1193,440,#FCF2E2|1193,456,#FFFFFF|1200,477,#FDF4E4|1178,489,#C18B36",rect=[int(width * 0.55),int(height * 0.29),int(width * 0.84),int(height * 0.56)],diff=0.9)


# 检索自动战斗中pokemon选项
def soulAdjust(p_index,padding):
    # 圣山之巅不用检查
    if p_index == 4:
        return
    time.sleep(2)
    pokemon_pos = None
    while not pokemon_pos:
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

   
def toAddress(p_index,padding): 
    time.sleep(0.5)
    # 点击地图
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

def new_toAddress(p_index, padding):
    # 我要变强（不区分padding）
    bq = FindColors.find("1789,55,#F5F1EC|1771,57,#B99773|1767,71,#F9F2D7|1805,81,#F6F2E2|1775,47,#A6B9BE",rect=[int(width * 0.74),int(height * 0.02),int(width * 0.92),int(height * 0.12)],diff=0.9)
    if bq:
        action.click(bq)
        time.sleep(2)
    else:
        print("未检索到我要变强")
    # 精灵成长（不区分padding）
    action.click(int(width * 0.14),int(height * 0.57),200)
    time.sleep(2)
    # 前往（不区分padding）
    qw = FindColors.find("1871,720,#FFDC75|1835,694,#77665E|1822,745,#88756B|1904,697,#77665E|1905,744,#88756B|1843,720,#FFDC75|1879,702,#FEFADD",rect=[int(width * 0.77),int(height * 0.60),int(width * 0.89),int(height * 0.73)],diff=0.95)
    if qw:
        action.click(qw)
        time.sleep(2)
    else:
        print("未检索到前往")
    if p_index == 2 or p_index == 3:
        # 晨光果园的前往挑战（不区分padding）
        chenguang = FindColors.find("1670,376,#FFD181|1640,368,#77665E|1682,361,#FFFFFF|1689,392,#FFFC9B|1660,412,#F3F3ED",rect=[int(width * 0.67),int(height * 0.28),int(width * 0.82),int(height * 0.43)],diff=0.85)
        if chenguang:
            action.click(chenguang)
            time.sleep(2)
        else:
            print("未检索到晨光果园")
    elif p_index == 0 or p_index == 1:
        daoyu = FindColors.find("1698,853,#917C6E|1685,841,#907B6D|1713,840,#917B6E|1684,866,#8E786B|1713,867,#907B6E",rect=[int(width * 0.69),int(height * 0.75),int(width * 0.83),int(height * 0.84)],diff=0.85)
        if daoyu:
            action.click(daoyu)
            time.sleep(1)
        # 居民区三层的前往挑战（不区分padding）
        jumin = FindColors.find("1670,376,#FFD181|1640,368,#77665E|1682,361,#FFFFFF|1689,392,#FFFC9B|1660,412,#F3F3ED",rect=[int(width * 0.68),int(height * 0.46),int(width * 0.83),int(height * 0.60)],diff=0.85)
        if jumin:
            action.click(jumin)
            time.sleep(2)
        else:
            print("未检索到居民区三层")
    
    else:
        daoyu = FindColors.find("1698,853,#917C6E|1685,841,#907B6D|1713,840,#917B6E|1684,866,#8E786B|1713,867,#907B6E",rect=[int(width * 0.69),int(height * 0.75),int(width * 0.83),int(height * 0.84)],diff=0.85)
        if daoyu:
            action.click(daoyu)
            time.sleep(1)
        # 圣山之巅的前往挑战（不区分padding）
        shengshan = FindColors.find("1670,376,#FFD181|1640,368,#77665E|1682,361,#FFFFFF|1689,392,#FFFC9B|1660,412,#F3F3ED",rect=[int(width * 0.40),int(height * 0.29),int(width * 0.49),int(height * 0.42)],diff=0.85)
        if shengshan:
            action.click(shengshan)
            time.sleep(3)
            action.click(int(width * 0.49),int(height * 0.07))
            action.click(int(width * 0.49),int(height * 0.07))
            time.sleep(4)
            action.click(int(width * 0.5),int(height * 0.07))
            time.sleep(2)
        else:
            print("未检索到圣山之巅")

alr_in_0 = False
alr_in_2 = False

def xinghun(pokemon_index,times,padding):
    print(f"现在去打{_list[pokemon_index]}星魂")
    time.sleep(2)
    global alr_in_0
    global alr_in_2
    if alr_in_0 and pokemon_index == 1:
        print("已经在居民区三层")
    elif alr_in_2 and pokemon_index == 3:
        print("已经在晨光果园")
    else:
        time.sleep(1)
        new_toAddress(pokemon_index,padding)
    if pokemon_index == 0:
        alr_in_0 = True
    if pokemon_index == 2:
        alr_in_2 = True
    print(f"来到{_list[pokemon_index]}的地图")

 
    in_battle = False
    pokemon_pos = None
    FB = None
    ptr_ok = False
    finish_FB = False
    finish_battle = False

    for _ in range(times):
        print("开始战斗")
        battle.battle( padding = padding,
                        index = pokemon_index,
                        pokemon_index = pokemon_index,
                        _list = _list)

    print(f"{_list[pokemon_index]}星魂已打完")
    time.sleep(2)



