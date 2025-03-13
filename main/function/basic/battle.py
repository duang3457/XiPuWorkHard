
from ascript.android import action
from ascript.android.system import R
from ascript.android.screen import FindColors
from ascript.android.system import Device
from ascript.android.screen.gp import GPStack
import cv2
from ascript.android.screen.gp_tasks import CvFontLib
from ascript.android.screen import FindImages


import time
from time import sleep

rect = __import__(R.name+".main.utils.rect",fromlist=[''])
isSkill = __import__(R.name+".main.utils.isSkill",fromlist=[''])
rc = rect.rc1920

display = Device.display()
width = display.widthPixels
height = display.heightPixels
# path = R.res("/img/a.png")

def find(index):
    def gp(cv_img=None):
        gp_stack = GPStack(cv_img)
        if index == 0: # 回音蟹
            gp_stack.add(CvFontLib([R.rel(__file__,"../../../res/img/回音蟹.png"),],['回音蟹',],rect = rc(132,417,1132,735), confidence= 0.55))
        elif index == 1: # 游戏小熊
            gp_stack.add(CvFontLib([R.rel(__file__,"../../../res/img/游戏小熊.png"),],['游戏小熊',],rect = rc(734,420,1880,888), confidence= 0.55))
        elif index == 2: # 浮水波尼（魔防）
            gp_stack.add(CvFontLib([R.rel(__file__,"../../../res/img/浮水波尼.png"),],['浮水波尼',],rect = rc(621,448,1544,953), confidence= 0.50))
        elif index == 3: # 兔宝
            gp_stack.add(CvFontLib([R.rel(__file__,"../../../res/img/兔宝.png"),],['兔宝',],rect = rc(931,253,1908,910), confidence= 0.55))
        elif index == 4: # 精灵集团
            gp_stack.add(CvFontLib([R.rel(__file__,"../../../res/img/精灵集团.png"),],['精灵集团',],rect = rc(327,265,1437,704), confidence= 0.5))
            #FindImages.find(path,rect = rc(931,253,1908,910),confidence=0.1)
        gp_result = gp_stack.run()
        return gp_result

    while True:
        if FindColors.find("964,38,#FFFFFF|964,62,#FFFFFF|936,44,#3E547A|980,49,#7BA4F3",rect=rc(847,8,1058,107),diff=0.9):
            print("进入局内")
            return
        while True:
            res = gp()
            if FindColors.find("964,38,#FFFFFF|964,62,#FFFFFF|936,44,#3E547A|980,49,#7BA4F3",rect=rc(847,8,1058,107),diff=0.9):
                print("进入局内")
                return
            if res.data:
                print(res.data)
                break   
        #print(res.__dict__)
        print(res.data)
        # print(res.data['words'][0][0]['result'])
        x,y = res.data['words'][0][0]['result']
        action.click(x-50,y-100,100)
        action.click(x-50,y-100,100)
        print("光速连击")
        time.sleep(3)
        # 回合
        

def battle(width = width,height = height, **kwargs):
    width = kwargs.get('width', width)
    height = kwargs.get('height', height)
    in_battle = kwargs.get('in_battle', True)
    ptr_ok = kwargs.get('ptr_ok', False)
    finish_FB = kwargs.get('finish_FB', True)
    finish_battle = kwargs.get('finish_battle', False)
    count = kwargs.get('count', 0)
    pokemon_index = kwargs.get('pokemon_index', 0)
    _list = kwargs.get('_list', ['第'])
    padding = kwargs.get('padding', False)
    index = kwargs.get('index', 0)
  
    find(index)
    print("进入局内")
    time.sleep(1)
    while True: 
        huihe = FindColors.find("964,43,#FFFFFF",rect=[int(width * 0.47),int(height * 0.01),int(width * 0.54),int(height * 0.09)], diff=0.92)
        click_return = FindColors.find("795,1035,#FEF1A4|1099,1035,#FFF2A5",rect=rc(725,977,1155,1070),diff=0.95)
        if not huihe:
            in_battle = False
        if not huihe and click_return and finish_battle:
            in_battle = False
            finish_FB = True
            print("点击返回键")
            action.click(click_return)
            time.sleep(1)
        
        newlearn = FindColors.find("1468,941,#FDDDA6|1599,947,#FFDFA9",rect=[int(width * 0.58),int(height * 0.80),int(width * 0.71),int(height * 0.94)])
        if newlearn:
            print("检索到替换技能")
            action.click(newlearn)
            sleep(2)
            
        if in_battle and huihe:
            if isSkill.isSkill():
                action.click(int(width * 0.30),int(height * 0.91))
            finish_battle = True
            time.sleep(2)
        if FindColors.find("195,783,#FFD36E|202,792,#FFDA73",rect=[int(width * 0.00),int(height * 0.63),int(width * 0.12),int(height * 0.80)]):
            print("结束战斗")
            break
    time.sleep(1)


def battle_old(width = width,height = height, **kwargs):
    width = kwargs.get('width', width)
    height = kwargs.get('height', height)
    in_battle = kwargs.get('in_battle', False)
    ptr_ok = kwargs.get('ptr_ok', False)
    finish_FB = kwargs.get('finish_FB', True)
    finish_battle = kwargs.get('finish_battle', False)
    count = kwargs.get('count', 0)
    pokemon_index = kwargs.get('pokemon_index', 0)
    _list = kwargs.get('_list', ['第'])
    padding = kwargs.get('padding', False)
    times = kwargs.get('times', 0)
    yise = kwargs.get('yise', False)
    yise_count = 0

    print("battle模块加载")
    while True: 

        huihe = FindColors.find("964,43,#FFFFFF",rect=[int(width * 0.47),int(height * 0.01),int(width * 0.54),int(height * 0.09)], diff=0.92)
        # 检索自动战斗键(一样)
        if not in_battle and not ptr_ok:
            FB = FindColors.find("195,783,#FFD36E|202,792,#FFDA73",rect=[int(width * 0.00),int(height * 0.63),int(width * 0.12),int(height * 0.80)])
            if FB:
                print("点击自动战斗")
                yise_count = 0
                action.click(FB)
                time.sleep(0.5)

        # 检索自动战斗确认键
        if not padding:
            FB2 = FindColors.find("1624,800,#FFCF7F|1587,789,#675246|1607,777,#FAC479|1629,765,#675246|1660,831,#FFF997|1625,842,#675246",rect=rc(1437,733,1801,907),diff=0.92)
        else:
            FB2 = FindColors.find("1817,777,#FAC479|1854,790,#FCC97A|1876,794,#675246|1824,811,#FEDB89",rect=[int(width * 0.68),int(height * 0.57),int(width * 0.88),int(height * 0.95)],diff=0.9)
        if FB2 and finish_FB:
            action.click(FB2)
            print("点击自动战斗确认键,次数+1")
            yise_count = 0
            ptr_ok = True
            finish_FB = False
            count += 1
            print(f"{_list[pokemon_index]} ",count," 次")
            time.sleep(1.5)
        
        # 检索停止自动战斗键(穿插战斗技能选择)
        if huihe:
            print("检索到在局内")
            finish_battle = True
            yise_count += 1
            print(f"异色计时器{yise_count}")
            if _list[pokemon_index] == "异种":
                time.sleep(0.5)
            else:
                time.sleep(0.2)
            if not padding:
                stop_FB = FindColors.find("1267,381,#FFFCE6|1282,382,#FFFCE6",rect=[int(width * 0.61),int(height * 0.27),int(width * 0.77),int(height * 0.42)])
            else:
                stop_FB = FindColors.find("1475,376,#FEFCE6|1493,373,#FFFCE6|1477,387,#FFFCE6|1493,388,#FFFCE6",rect=[int(width * 0.55),int(height * 0.24),int(width * 0.76),int(height * 0.44)])
            
            if stop_FB:
                time.sleep(0.2)
                print("点击停止自动战斗")
                action.click(stop_FB)
                in_battle = True
                
                time.sleep(3)
        
        if yise:
            if yise_count >= 20:
                print("单局时间过长，捕捉异色")
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
                yise_count = 0
        
        click_return = FindColors.find("795,1035,#FEF1A4|1099,1035,#FFF2A5",rect=rc(725,977,1155,1070),diff=0.95)
        if not huihe:
            in_battle = False
        if not huihe and click_return and finish_battle:
            in_battle = False
            finish_FB = True
            finish_battle = False
            print("点击返回键")
            action.click(click_return)
            if count >= times:
                break
            time.sleep(1)
        
        newlearn = FindColors.find("1468,941,#FDDDA6|1599,947,#FFDFA9",rect=[int(width * 0.58),int(height * 0.80),int(width * 0.71),int(height * 0.94)])
        if newlearn:
            print("检索到替换技能")
            action.click(newlearn)
            sleep(2)
            

        if in_battle and huihe:
            if isSkill.isSkill():
                action.click(int(width * 0.30),int(height * 0.91))
            finish_battle = True
            ptr_ok = False
            time.sleep(2)

    time.sleep(1)
    while True:
        click_return2 = FindColors.find("795,1035,#FEF1A4|1099,1035,#FFF2A5",rect=rc(725,977,1155,1070),diff=0.95)
        if click_return2:
            print("点击返回键")
            action.click(click_return2)
            time.sleep(1)
        # 技能替换提示，检索取消键
        newlearn2 = FindColors.find("1468,941,#FDDDA6|1599,947,#FFDFA9",rect=[int(width * 0.58),int(height * 0.80),int(width * 0.71),int(height * 0.94)])
        if newlearn2:
            print("检索到替换技能")
            action.click(newlearn2)
            sleep(2)
        # 找到自动战斗结束
        if FindColors.find("195,783,#FFD36E|202,792,#FFDA73",rect=[int(width * 0.00),int(height * 0.63),int(width * 0.12),int(height * 0.80)]):
            break


