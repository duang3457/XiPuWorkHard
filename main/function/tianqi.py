from ascript.android.system import R
from ascript.android import action
from ascript.android.screen import FindColors
from ascript.android.system import Device

import time
from time import sleep

rect = __import__(R.name+".main.utils.rect",fromlist=[''])
io = __import__(R.name+".main.utils.io",fromlist=[''])
battle = __import__(R.name+".main.function.basic.battle",fromlist=[''])
isSkill = __import__(R.name+".main.utils.isSkill",fromlist=[''])

rc = rect.rc1920
rc2 = rect.rc19202

display = Device.display()
width = display.widthPixels
height = display.heightPixels

jn_click_list = [rc2(598,984), rc2(849,986), rc2(1075,984), rc2(1312,989), rc2(1665,936)]

def starttq(padding,index):
    
    print("天启开始")
    
    jn_list = io.r_skill()
    if not jn_list:
        jn_list = ["1","1","1"]
    print(jn_list)
    jn1_list = list(map(int,jn_list[0]))

    in_battle = True
    count = 0
    skill_count = 0
    # cur_hero = 1
    time.sleep(2)

    # 我要变强（不区分padding）
    bq = FindColors.find("1789,55,#F5F1EC|1771,57,#B99773|1767,71,#F9F2D7|1805,81,#F6F2E2|1775,47,#A6B9BE",rect=[int(width * 0.74),int(height * 0.02),int(width * 0.92),int(height * 0.12)],diff=0.9)
    if bq:
        print("点击我要变强")
        action.click(bq)
        time.sleep(2)
    else:
        print("未检索到我要变强")

    # 选择天启纪元
    tq = FindColors.find("820,686,#CFBEEE|818,675,#40366A|826,674,#2E335E|814,699,#9582E8|826,702,#FDF7FF",rect=rc(688,468,996,907),diff=0.85)
    if tq:
        print("选择天启纪元")
        action.click(tq)
        time.sleep(2)
    
    # 前往
    qianwang = FindColors.find("1644,733,#FFEEBC|1634,712,#77675E|1670,717,#77675E|1629,733,#FFC96A|1656,740,#FFD06E",rect=rc(1408,617,1790,834),diff=0.85)
    if qianwang:
        print("点击前往")
        action.click(qianwang)
        time.sleep(4)

    # 老虎
    if index == 0:
        lh = FindColors.find("375,371,#EDCCA1|345,351,#CE6A20|391,335,#EECC77|434,352,#FFFFC9|355,412,#FD8A26",rect=rc(200,236,638,510),diff=0.85)
        if lh:
            print("点击老虎")
            action.click(lh)
            time.sleep(2)
    # 猫
    elif index == 1:
        mao = FindColors.find("1451,353,#5CBAE8|1422,315,#B93200|1446,307,#5FC4EE|1497,356,#FFFFE4|1434,353,#0D0D2E",rect=rc(1197,217,1708,504),diff=0.9)
        if mao:
            print("点击猫")
            action.click(mao)
            time.sleep(2)
        
    # 点挑战（跳转地图）
    action.click(int(width * 0.90),int(height * 0.57))
    print("点击挑战")
    time.sleep(2)

    # 点目标（老虎）
    if index == 0:
        action.click(int(width * 0.68),int(height * 0.36))
        print("点击老虎")
        time.sleep(4)
    # 点猫
    elif index == 1:
        if width >= 2300:
            action.click(int(width * 0.75),int(height * 0.40))
            print("点击猫")
        else:
            action.click(int(width * 0.83),int(height * 0.40))
            print("点击猫")
        time.sleep(8)

    # 点普通
    putong = FindColors.find("1638,831,#FFFAC8|1606,808,#FFFFD2|1636,793,#7B4248|1667,809,#FFFFD2|1622,822,#573035",rect=rc(1493,735,1900,905),diff=0.5,ori=1)
    if putong:
        print("普通")
        action.click(putong)
    else:
        print("未检索到普通")

    for _ in range(2):
        i = 0
        time.sleep(2)
        action.click(int(width * 0.5),int(height * 0.5),100)
        time.sleep(2)
        print("点击开始战斗")
        time.sleep(3)
        while True: 
            # 检测挑战
            if FindColors.find_all("960,543,#FFFFFF|898,479,#FFFFFF|879,502,#EAD9AD|1014,480,#FFFEFF|1006,529,#E7DBAB|924,593,#FFE79A",rect=rc(759,380,1166,699),diff=0.95):
                print("结束本轮战斗")
                break
            
            huihe = FindColors.find("964,43,#FFFFFF",rect=[int(width * 0.47),int(height * 0.01),int(width * 0.54),int(height * 0.09)], diff=0.92)
            fail_click_return = FindColors.find_all("795,1031,#9ED4DF|807,1032,#9BD0DE|872,1030,#A1D7E2|962,1030,#9CD3DF|1099,1032,#9FD4E1",rect=rc(756,986,1135,1065),diff=0.85,ori= 1)
            click_return = FindColors.find("795,1035,#FEF1A4|1099,1035,#FFF2A5",rect=rc(725,977,1155,1070),diff=0.95)
            if huihe:
                in_battle = True
            else:
                in_battle = False
            if not huihe and click_return:
                in_battle = False
                print("点击返回键")
                action.click(click_return)
                time.sleep(1)
                
            # 技能替换提示，检索取消键
            newlearn = FindColors.find("1468,941,#FDDDA6|1599,947,#FFDFA9",rect=[int(width * 0.58),int(height * 0.80),int(width * 0.71),int(height * 0.94)])
            if newlearn:
                print("检索到替换技能")
                action.click(newlearn)
                sleep(2)

            if in_battle and huihe:
                if isSkill.isSkill():
                    print("检索到技能")
                    time.sleep(0.5)
                    len_jn1 = len(jn1_list)
                    if i > len_jn1-1:
                        i = len_jn1-1
                    # if cur_hero == 1:
                    jn_click = jn_click_list[jn1_list[i]-1]
                    action.click(jn_click[0],jn_click[1],100)
                    print(f"点击{jn1_list[i]}号位技能")
                    print(f"当前预设{jn1_list}")
                    print(f"这是预设中的{i+1}个")
                    i += 1
                    time.sleep(1)

            
            
    # 点击返回
    time.sleep(2)
    fanhui = None
    while not fanhui:
        fanhui = FindColors.find("60,70,#564523|54,60,#FFF6BC|54,82,#F3E79E|81,66,#EBDB92|95,86,#E2C78D",rect=rc(2,11,302,132),diff=0.9)
    if fanhui:
        action.click(fanhui)
        time.sleep(2)


def startyj(padding,index):
    print("异界开始")
    
    jn_list = io.r_skill()
    if not jn_list:
        jn_list = ["1","1","1"]
    print(jn_list)
    jn3_list = list(map(int,jn_list[2]))

    in_battle = True
    count = 0
    skill_count = 0
    # cur_hero = 1
    time.sleep(2)

    # 我要变强（不区分padding）
    bq = FindColors.find("1789,55,#F5F1EC|1771,57,#B99773|1767,71,#F9F2D7|1805,81,#F6F2E2|1775,47,#A6B9BE",rect=[int(width * 0.74),int(height * 0.02),int(width * 0.92),int(height * 0.12)],diff=0.9)
    if bq:
        print("点击我要变强")
        action.click(bq)
        time.sleep(2)
    else:
        print("未检索到我要变强")

    # 选择天启纪元
    yj = FindColors.find("605,391,#411045|604,365,#6D3792|581,418,#552A6C|648,380,#FFD7FB|657,437,#F7F6EE",rect=rc(302,157,643,623),diff=0.9)
    if yj:
        print("选择异界入侵")
        action.click(tq)
        time.sleep(2)
    
    # 前往
    qianwang = FindColors.find("1644,733,#FFEEBC|1634,712,#77675E|1670,717,#77675E|1629,733,#FFC96A|1656,740,#FFD06E",rect=rc(1408,617,1790,834),diff=0.85)
    if qianwang:
        print("点击前往")
        action.click(qianwang)
        time.sleep(2)

    # 点击合作模式
    turn_hz = FindColors.find("2231,430,#FFFFFF|2238,421,#FFFFFF|2248,430,#FFFFFF|2220,444,#FFFFFF|2228,453,#FFFFFF|2252,445,#FFFFFF",rect=rc(1660,358,1857,499),diff=0.9)
    if turn_hz:
        print("点击合作模式")
        action.click(turn_hz)
        time.sleep(2)
    
    # 硬点开始
    action.click(int(width * 0.49),int(height * 0.62))
    time.sleep(2)

    # 硬选一号位1920
    while True:
        one = FindColors.find("940,195,#82E3FF|940,218,#9FFFFF|939,235,#C2FFFF|977,215,#99FFFF",rect=rc(880,129,1033,293),diff=0.95)
        if one:
            action.click(int(width * 0.32),int(height * 0.90))
            break

    
    i = 0
    time.sleep(2)
    action.click(int(width * 0.5),int(height * 0.5),100)
    time.sleep(2)
    time.sleep(3)
    while True: 
        # 检测挑战
        if FindColors.find_all("960,543,#FFFFFF|898,479,#FFFFFF|879,502,#EAD9AD|1014,480,#FFFEFF|1006,529,#E7DBAB|924,593,#FFE79A",rect=rc(759,380,1166,699),diff=0.95):
            print("结束本轮战斗")
            break
        
        huihe = FindColors.find("964,43,#FFFFFF",rect=[int(width * 0.47),int(height * 0.01),int(width * 0.54),int(height * 0.09)], diff=0.92)
        fail_click_return = FindColors.find_all("795,1031,#9ED4DF|807,1032,#9BD0DE|872,1030,#A1D7E2|962,1030,#9CD3DF|1099,1032,#9FD4E1",rect=rc(756,986,1135,1065),diff=0.85,ori= 1)
        click_return = FindColors.find("795,1035,#FEF1A4|1099,1035,#FFF2A5",rect=rc(725,977,1155,1070),diff=0.95)
        if huihe:
            in_battle = True
        else:
            in_battle = False
        if not huihe and click_return:
            in_battle = False
            print("点击返回键")
            action.click(click_return)
            time.sleep(1)
            
        # 技能替换提示，检索取消键
        newlearn = FindColors.find("1468,941,#FDDDA6|1599,947,#FFDFA9",rect=[int(width * 0.58),int(height * 0.80),int(width * 0.71),int(height * 0.94)])
        if newlearn:
            print("检索到替换技能")
            action.click(newlearn)
            sleep(2)

        if in_battle and huihe:
            if isSkill.isSkill():
                print("检索到技能")
                time.sleep(0.5)
                len_jn1 = len(jn3_list)
                if i > len_jn1-1:
                    i = len_jn1-1
                # if cur_hero == 1:
                jn_click = jn_click_list[jn3_list[i]-1]
                action.click(jn_click[0],jn_click[1],100)
                print(f"点击{jn3_list[i]}号位技能")
                print(f"当前预设{jn3_list}")
                print(f"这是预设中的{i+1}个")
                i += 1
                time.sleep(1)

        
            



