# 对于梦境，1920的尽量朝里面靠


from ascript.android.system import R
from ascript.android.screen import FindColors
from ascript.android import action
from ascript.android.system import Device

from time import sleep
import time

rect = __import__(R.name+".main.utils.rect",fromlist=[''])
io = __import__(R.name+".main.utils.io",fromlist=[''])
battle = __import__(R.name+".main.function.basic.battle",fromlist=[''])
isSkill = __import__(R.name+".main.utils.isSkill",fromlist=[''])
rc = rect.rc1920
rc2 = rect.rc19202
c = action.click

display = Device.display()
width = display.widthPixels
height = display.heightPixels

jn_click_list = [rc2(598,984), rc2(849,986), rc2(1075,984), rc2(1312,989), rc2(1665,936)]

# 检索地图
def start(times,padding):
    time.sleep(1)
    start = FindColors.find("1461,910,#8BE366|1611,910,#8AE165|1542,838,#F0ECE1|1535,623,#F3F0E8|1546,374,#F5F3EB",rect=rc(1109,105,1877,1034),diff=0.9,ori= 1)
    if start:
        print("已经在永恒梦境")
        c(start,100)
        sleep(3)
    else:
        map_pos = FindColors.find("1695,982,#7B261E|1702,990,#F2CC71|1716,966,#3B3499|1742,986,#2AD635|1758,996,#E0B956",rect=rc(1384,880,1832,1061),diff=0.8,ori= 1)
        while not map_pos:
            print("检索地图暂未适配所有机型，请到梦境界面开启脚本（开始梦境之前的那个界面）")
            map_pos = FindColors.find("1695,982,#7B261E|1702,990,#F2CC71|1716,966,#3B3499|1742,986,#2AD635|1758,996,#E0B956",rect=rc(1384,880,1832,1061),diff=0.8,ori= 1)
            sleep(0.5)
        if map_pos:
            print("检索到地图")
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
        start1(padding)
        count += 1



def start1(padding):
    time.sleep(2)
    start = FindColors.find("1467,892,#80D05E|1467,923,#94F06C|1620,893,#80D05E|1619,929,#9EF771",rect=rc(1242,819,1723,965),diff=0.9)
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
    if width >= 2300:
        c(int(width * 0.25),int(height * 0.38))
    else:
        c(int(width * 0.21),int(height * 0.38))
    print("硬点击第二关")
    aft_g()
    
    sleep(2)
    if width >= 2300:
        c(int(width * 0.17),int(height * 0.58))
    else:
        c(int(width * 0.12),int(height * 0.58))
    print("硬点击第三关")
    sleep(2)
    c(int(width * 0.56),int(height * 0.70))
    sleep(5)

    if width >= 2300:
        c(int(width * 0.32),int(height * 0.72))
    else:
        c(int(width * 0.30),int(height * 0.72))
    print("硬点击第四关")
    sleep(2)
    if width >= 2300:
        c(int(width * 0.70),int(height * 0.71))
    else:
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
    if width >= 2300:
        c(int(width * 0.80),int(height * 0.52))
    else:
        c(int(width * 0.85),int(height * 0.52))
    print("硬点击第七关")
    sleep(2)
    if width >= 2300:
        c(int(width * 0.70),int(height * 0.71))
    else:
        c(int(width * 0.75),int(height * 0.71))

    sleep(5)
    if width >= 2300:
        c(int(width * 0.77),int(height * 0.24),100)
    else:  
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
    if width >= 2300:
        c(int(width * 0.80),int(height * 0.61))
    else:
        c(int(width * 0.91),int(height * 0.61))
    print("走过去肉搏")
    sleep(5)
    c(int(width * 0.54),int(height * 0.33))
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

    sleep(3)

def battle():
    jn_list = io.r_skill()
    
    if not jn_list:
        jn_list = ["1","1","1"]
    print(jn_list)
    jn1_list = list(map(int,jn_list[0]))
    jn2_list = list(map(int,jn_list[1]))
    jn3_list = list(map(int,jn_list[2]))


    in_battle = True
    i = 0
    while True:
        huihe = FindColors.find("964,43,#FFFFFF",rect=[int(width * 0.47),int(height * 0.01),int(width * 0.54),int(height * 0.09)])
        battle_win = FindColors.find("1653,215,#FDE87B|1688,214,#FDE87B",rect=[int(width * 0.54),int(height * 0.08),int(width * 0.87),int(height * 0.38)])
        if not huihe and battle_win:
            print("战斗胜利")
            sleep(5)
            c(int(width * 0.30),int(height * 0.91))
            sleep(3)
        
        chilun = FindColors.find("1861,56,#132126|1856,40,#FADBAB|1870,40,#F0CF9F|1877,51,#DEB594|1876,71,#222329|1862,75,#423422",rect=rc(1699,11,1911,107),diff=0.9)
        wushi = FindColors.find("1162,760,#A76F3D|1091,657,#FFF2D8|1242,655,#FFF2D8|1106,753,#F9DFAA|1261,765,#F0D6A6",rect=rc(984,626,1391,840))
        duiwu = FindColors.find("128,962,#FBAF72|98,938,#F5ECC0|166,941,#F8E69D|160,1004,#E7BE31|109,1043,#FFFFFF|91,998,#DFB630",rect=rc(14,913,389,1065),diff=0.9)
        if chilun or wushi or duiwu:
            print("战斗结束")
            if wushi:
                c(wushi,100)
            return

        huihe = FindColors.find("964,43,#FFFFFF",rect=[int(width * 0.47),int(height * 0.01),int(width * 0.54),int(height * 0.09)])
        click_return = FindColors.find("795,1035,#FEF1A4|1099,1035,#FFF2A5",rect=rc(725,977,1155,1070),diff=0.95)
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

        if in_battle and huihe:
            if isSkill.isSkill():
                print("检索到技能")
                time.sleep(0.5)
                len_jn2 = len(jn2_list)
                if i > len_jn2-1:
                    i = len_jn2-1
                # if cur_hero == 1:
                jn_click = jn_click_list[jn2_list[i]-1]
                action.click(jn_click[0],jn_click[1],100)
                print(f"点击{jn2_list[i]}号位技能")
                print(f"当前预设{jn2_list}")
                print(f"第{i+1}个预设技能")
                i += 1
                time.sleep(1)


            
        
def test():
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



   
        
    



