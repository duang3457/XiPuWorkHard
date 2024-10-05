from ascript.android.system import R
from ascript.android.screen import FindColors
from ascript.android import action
from ascript.android.system import Device

from time import sleep
import time

rect = __import__(R.name+".main.utils.rect",fromlist=[''])
rc = rect.rect_convert
c = action.click

display = Device.display()
width = display.widthPixels
height = display.heightPixels

# 检索地图
def start(times):
    start = FindColors.find("1461,910,#8BE366|1611,910,#8AE165|1542,838,#F0ECE1|1535,623,#F3F0E8|1546,374,#F5F3EB",rect=rc(1109,105,1877,1034),diff=0.9,ori= 1)
    if start:
        print("已经在永恒梦境")
        c(start,100)
        sleep(3)
    else:
        map_pos = FindColors.find("1695,982,#7B261E|1702,990,#F2CC71|1716,966,#3B3499|1742,986,#2AD635|1758,996,#E0B956",rect=[1384,880,1832,1061],diff=0.8,ori= 1)
        while not map_pos:
            print("未检索到呼噜猫旅店")
            map_pos = FindColors.find("1695,982,#7B261E|1702,990,#F2CC71|1716,966,#3B3499|1742,986,#2AD635|1758,996,#E0B956",rect=[1384,880,1832,1061],diff=0.8,ori= 1)
            sleep(0.5)
        if map_pos:
            print("检索到呼噜猫旅店")
            c(map_pos,100)
        sleep(3)
        mj_logo_pos = FindColors.find("422,978,#C2B0AF|472,973,#F7F2FA|517,981,#C2AFB4",rect=rc(214,856,746,1070),diff=0.9,ori= 6)
        while not mj_logo_pos:
            print("未检索到永恒梦境")
            mj_logo_pos = FindColors.find("422,978,#C2B0AF|472,973,#F7F2FA|517,981,#C2AFB4",rect=rc(214,856,746,1070),diff=0.9,ori= 6)
            sleep(0.5)
        if mj_logo_pos:
            print("检索到永恒梦境")
            c(mj_logo_pos,100)
        
        sleep(2)
        up_arrow = FindColors.find("588,82,#FFFFFF|612,59,#FFFFFF|633,82,#FFFFFF",rect=rc(501,6,722,172))
        if up_arrow:
            action.click(up_arrow.x,up_arrow.y-10,100)
            sleep(2)
        else:
            print("到达最高层")

        no9 = FindColors.find("576,325,#FFFDFD|588,323,#403467|602,323,#FFFBFE|617,319,#4E3C5B",rect=rc(399,157,858,456),diff=0.9)
        if no9:
            print("检索到第九层")
            c(no9,100)
    
    count = 0
    while count < times:
        start1()
        count += 1



def start1():
    time.sleep(2)
    start = FindColors.find("1467,892,#80D05E|1467,923,#94F06C|1620,893,#80D05E|1619,929,#9EF771",rect=[1242,819,1723,965],diff=0.9)
    if start:
        print("检索到开始")
        c(start,100)
        sleep(3)
    else:
        print("未检索到开始")
    
    # g1 = FindColors.find("772,530,#EE90B1|800,516,#FBF093|808,538,#182971|790,557,#67CDFB",rect=[565,378,1009,662],diff=0.9)
    # if g1:
    #     print("检索到第一关")
    #     aft_g(g1,1)
    c(int(width * 0.42),int(height * 0.49))
    print("硬点击第一关")
    aft_g()

    sleep(2)
    # g2 = FindColors.find("377,378,#E8BD6B|358,406,#F3E7CF|397,412,#F3E6CF|375,430,#EEDFC4",rect=[217,290,656,511],diff=0.9,ori= 1)
    # if g2:
    #     print("检索到第二关")
    #     aft_g(g2,2)
    c(int(width * 0.21),int(height * 0.38))
    print("硬点击第二关")
    aft_g()
    
    sleep(2)
    c(int(width * 0.12),int(height * 0.58))
    print("硬点击第三关")
    sleep(2)
    c(int(width * 0.56),int(height * 0.70))
    sleep(5)

    c(int(width * 0.30),int(height * 0.72))
    print("硬点击第四关")
    sleep(2)
    c(int(width * 0.75),int(height * 0.71))
    sleep(5)

    c(int(width * 0.50),int(height * 0.75))
    print("硬点击第五关")
    aft_g()

    sleep(2)
    c(int(width * 0.70),int(height * 0.71))
    print("硬点击第六关")
    aft_g()

    sleep(3)
    c(int(width * 0.85),int(height * 0.52))
    print("硬点击第七关")
    sleep(2)
    c(int(width * 0.75),int(height * 0.71))

    sleep(5)
    c(int(width * 0.82),int(height * 0.24),100)
    print("硬点击第八关")
    sleep(3)
    c(int(width * 0.5),int(height * 0.68),100)
    sleep(4)

    c(int(width * 0.84),int(height * 0.79),100)
    print("没事走两步")
    print("由于跳过点击经常卡住，看完吧，用不了几秒")
    sleep(23)
    # c(int(width * 0.92),int(height * 0.10))
    # c(int(width * 0.92),int(height * 0.10))
    
    sleep(2)
    c(int(width * 0.91),int(height * 0.61))
    print("走过去肉搏")
    sleep(5)
    c(int(width * 0.55),int(height * 0.33))
    print("gan ta!")
    sleep(6)
    c(int(width * 0.7),int(height * 0.68))
    print("爱情无价！")
    sleep(3)
    battle()
    c(int(width * 0.88),int(height * 0.59))
    print("没事走两步")
    sleep(3)
    mf = FindColors.find("1423,301,#2D297D|1464,291,#9C8EBB|1504,297,#9D9AD5|1529,339,#5359C3",rect=rc(1112,130,1732,444),diff=0.9,ori= 1)
    while not mf:
        mf = FindColors.find("1423,301,#2D297D|1464,291,#9C8EBB|1504,297,#9D9AD5|1529,339,#5359C3",rect=rc(1112,130,1732,444),diff=0.9,ori= 1)
    if mf:
        print("检索到魔方")
        c(mf,100)
        sleep(3)
        c(int(width * 0.5),int(height * 0.9))
        sleep(3)
        c(mf,100)
        print("点击魔方退出副本")
        sleep(3)
    c(int(width * 0.50),int(height * 0.62))
    sleep(5)
    c(int(width * 0.49),int(height * 0.70))
    print("确认领取奖励")
    sleep(1)


def aft_g():
    sleep(2)
    c(int(width * 0.5),int(height * 0.5),100)
    sleep(4)
    battle()

    for _ in range(6):
        # 技能替换提示，检索取消键
        newlearn = FindColors.find("1468,941,#FDDDA6|1599,947,#FFDFA9",rect=[int(width * 0.58),int(height * 0.80),int(width * 0.71),int(height * 0.94)])
        if newlearn:
            print("检索到替换技能")
            c(newlearn)
            sleep(2)
        # 新技能提示，检索当前技能字样
        newlearn2 = FindColors.find("1371,486,#6C6975|1407,410,#FFFF9B|1429,486,#FFFFFF|1593,489,#6F6B75",rect=[1182,396,1729,568],diff=0.7,ori= 1)
        if newlearn2:
            print("检索到新技能")
            c(int(width * 0.50),int(height * 0.86))
            sleep(2)
    
    c(int(width * 0.6),int(height * 0.70),200)
    print("点击无视")
    sleep(3)

def battle():
    in_battle = True
    while True:
        huihe = FindColors.find("964,43,#FFFFFF",rect=[int(width * 0.47),int(height * 0.01),int(width * 0.54),int(height * 0.09)])
        battle_win = FindColors.find("1653,215,#FDE87B|1688,214,#FDE87B",rect=[int(width * 0.54),int(height * 0.08),int(width * 0.87),int(height * 0.38)])
        if not huihe and battle_win:
            print("战斗胜利")
            sleep(5)
            c(int(width * 0.30),int(height * 0.91))
            sleep(3)
            return

        if in_battle:
            sleep(1)
            c(int(width * 0.30),int(height * 0.91))
                
        
def test():
    while not FindColors.find("1848,50,#FDDFAE|1863,56,#17232E|1874,61,#E2B799",rect=[1641,12,1913,108],diff=0.8,ori= 1):
        # 技能替换提示，检索取消键
        newlearn = FindColors.find("1468,941,#FDDDA6|1599,947,#FFDFA9",rect=[int(width * 0.58),int(height * 0.80),int(width * 0.71),int(height * 0.94)])
        if newlearn:
            print("检索到替换技能")
            c(newlearn)
            sleep(1)
        # 新技能提示，检索当前技能字样
        newlearn2 = FindColors.find("1371,486,#6C6975|1407,410,#FFFF9B|1429,486,#FFFFFF|1593,489,#6F6B75",rect=[1182,396,1729,568],diff=0.7,ori= 1)
        if newlearn2:
            print("检索到新技能")
            c(int(width * 0.50),int(height * 0.86))
            sleep(2)
        else:
            print("未检索到")
            sleep(1)


   
        
    



