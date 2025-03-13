
from ascript.android.system import R
from ascript.android import action
from ascript.android import screen
from ascript.android.screen import FindColors
from ascript.android.system import Device

rect = __import__(R.name+".main.utils.rect",fromlist=[''])
output = __import__(R.name+".main.utils.io",fromlist=[''])
rc = rect.rc1920
op = output.record
gS = output.getScreen
c = action.click

import time
from time import sleep

display = Device.display()
width = display.widthPixels
height = display.heightPixels
density = display.density

def start(padding):
    print("抓四星")
    in_battle = False
    count = 0
    hs = None
    qiu = None
    huangguan = None
    buzhuo = None
    finish_battle = False
    while True: 
        huihe = FindColors.find("964,43,#FFFFFF",rect=[int(width * 0.47),int(height * 0.01),int(width * 0.54),int(height * 0.09)])
        # 检索自动战斗键
        FB = FindColors.find("195,783,#FFD36E|202,792,#FFDA73",rect=[int(width * 0.00),int(height * 0.63),int(width * 0.12),int(height * 0.80)])
        if FB:
            in_battle = False
            # 更新高星状态
            hs = None
            #print("检索到自动战斗,关闭战斗模式")
            action.click(FB)
            time.sleep(1)

        # 检索自动战斗确认键
        if not padding:
            FB2 = FindColors.find("1584,791,#675246|1664,834,#FFFD9E",rect=[int(width * 0.63),int(height * 0.62),int(width * 0.94),int(height * 0.88)],diff=0.98)
        else:
            FB2 = FindColors.find("1817,777,#FAC479|1854,790,#FCC97A|1876,794,#675246|1824,811,#FEDB89",rect=[int(width * 0.68),int(height * 0.57),int(width * 0.88),int(height * 0.95)])
        if FB2:
            action.click(FB2)
            count += 1
            print(f"抓捕第 ",count," 次")
            time.sleep(2)
        
        # 检索停止自动战斗键(穿插战斗技能选择)
        if huihe:
            print("在战斗中")
            time.sleep(0.2)
            if not padding:
                stop_FB = FindColors.find("1267,381,#FFFCE6|1282,382,#FFFCE6",rect=[int(width * 0.61),int(height * 0.27),int(width * 0.77),int(height * 0.42)])
            else:
                stop_FB = FindColors.find("1475,376,#FEFCE6|1493,373,#FFFCE6|1477,387,#FFFCE6|1493,388,#FFFCE6",rect=[int(width * 0.55),int(height * 0.24),int(width * 0.76),int(height * 0.44)])
            if stop_FB:
                action.click(stop_FB)
                print("点击停止自动战斗")
                time.sleep(1)
                finish_battle = True
                in_battle = True
        
        
        click_return = FindColors.find("795,1035,#FEF1A4|1099,1035,#FFF2A5",rect=rc(725,977,1155,1070),diff=0.95)
        if not huihe and click_return:
            in_battle = False
            #print("检索到返回键")
            action.click(click_return)
            time.sleep(2)
            
        # 技能替换提示，检索取消键
        newlearn = FindColors.find("1468,941,#FDDDA6|1599,947,#FFDFA9",rect=[int(width * 0.58),int(height * 0.80),int(width * 0.71),int(height * 0.94)])
        if newlearn:
            print("检索到替换技能")
            c(newlearn)
            sleep(2)

        if in_battle:
            if not hs:  # 高星和皇冠有可能混淆在hs里
                print("检索高星/皇冠")
                # 2340 X 1080
                # FindColors.find("1736,652,#F2DC9B|1728,659,#F7DF84|1730,668,#F3D87D|1742,668,#F5E087|1744,659,#FCDA88|1736,661,#FFFFBD",rect=rc(1623,598,1986,747),diff=0.9)
                hs = FindColors.find("567,653,#E1CD8F|559,659,#EFD67D|562,669,#FFF186|573,669,#F8E993|576,659,#F6D385|567,661,#FFFFBD",rect=rc(1397,577,1629,746),diff=0.90)
                hs1 = FindColors.find("567,653,#E1CD8F|559,659,#EFD67D|562,669,#FFF186|573,669,#F8E993|576,659,#F6D385|567,661,#FFFFBD",rect=rc(1397,577,1629,746),diff=0.90)
                hs2 = FindColors.find("567,653,#E1CD8F|559,659,#EFD67D|562,669,#FFF186|573,669,#F8E993|576,659,#F6D385|567,661,#FFFFBD",rect=rc(1397,577,1629,746),diff=0.90)
                huangguan = FindColors.find("1505,657,#C38926|1515,657,#BE8F29|1510,666,#F6EF9D|1510,651,#58420B",rect=rc(1397,577,1629,746),diff=0.88)
            if huangguan:
                print("检索到皇冠")
            if hs or hs1 or hs2 and not huangguan:
                print("检索到高星非皇冠！！！！")
                buzhuo = False
                qiu = False
                # 硬点手下留情
                time.sleep(2)
                print("手下留情")
                action.click(int(width * 0.46),int(height * 0.91))
                time.sleep(3)
                # 捕捉按钮
                while not buzhuo:
                    buzhuo = FindColors.find("675,854,#5B6058|657,842,#EDEBD1|650,873,#4F5E4C|700,873,#505D4C|675,832,#AEAEA7|652,855,#4C574C",rect=rc(507,764,846,922),diff=0.88)
                    if buzhuo:
                        action.click(buzhuo)
                        time.sleep(1)
                while not qiu:
                    qiu = FindColors.find("823,977,#EFF3D7|824,1009,#51B6EE|841,1022,#839D6C|779,952,#B5AEAC",rect=rc(698,843,1216,1067),diff=0.88)
                    if qiu:
                        action.click(qiu)
                        time.sleep(1)
                        action.click(int(width * 0.75),int(height * 0.53))
                        time.sleep(1)
                print("捕捉完成")
                

            if not hs or huangguan and finish_battle:
                print("没有检索到高星,撤退")
                # 重置状态
                qiu = None
                huangguan = None
                finish_battle = False
                # action.click(int(width * 0.30),int(height * 0.91))
                quit = FindColors.find("61,48,#E8CD90|49,50,#EAD293|59,39,#DBC289|59,59,#EEE9A2|73,51,#ECD394|83,63,#EEEEAA|81,40,#DCC289",rect=rc(3,6,335,102),diff=0.9)
                if quit:
                    action.click(quit)
                    time.sleep(1)
                    quit_qd = FindColors.find("1065,663,#81D25E|1200,664,#82D360|1057,689,#90EA69|1212,691,#90EA69",rect=rc(952,574,1357,765))
                    if quit_qd:
                        print("点击确定退出")
                        action.click(quit_qd)
                        time.sleep(4)
                    action.click(int(width * 0.30),int(height * 0.91))
                    print("点击返回")
                    time.sleep(1)

            time.sleep(2)

