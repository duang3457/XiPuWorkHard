# __init__.py 为初始化加载文件
# 启动页

# 导入ascript模块
from ascript.android.system import R
from ascript.android.system import Device
from ascript.android.ui import WebWindow
from ascript.android.screen import FindColors
from ascript.android.ui import Dialog
from ascript.android.screen import FindImages
from ascript.android import action

from .main.function import highStar
from .main.function import levelUp
from .main.function import xinghun
from .main.function import yizhong
from .main.function import tianqi
from .main.function.activities import mengjing

import json
import time
import os

rect = __import__(R.name+".main.utils.rect",fromlist=[''])
io = __import__(R.name+".main.utils.io",fromlist=[''])
test = __import__(R.name+".main.utils.test",fromlist=[''])
rc = rect.rc1920

display = Device.display()
width = display.widthPixels
height = display.heightPixels
print("width: ",width)
print("height: ",height)

isPadding = False

def start():
    def tunnel(k, v):
        global isPadding
        values = json.loads(v)
        print(f"Received from HTML: {values}")
        if k == '1':
            w.close()
    
        if k == '1':
            # 星魂
            if values['UI'] == 'unpadding':
                isPadding = False
            else:
                isPadding = True

            if values["choice"] == 'soul':
                for i in range(5):
                    if values[str(i+1)]:
                        xinghun.xinghun(i,values['upgradeCount'],isPadding)
            
            # 升级
            if values['choice'] == 'upgrade':
                print("升级")
                xinghun.xinghun(4,values['upgradeCount'],isPadding)

            # 梦境
            if values['choice'] == 'dream':
                mengjing.start(values['upgradeCount'],isPadding)

            #抓高星
            if values['choice'] == 'highStar':
                highStar.start(isPadding)
            
            #异色不捕捉
            if values['choice'] == 'yise1':
                yizhong.start(yise=False, padding=isPadding)

            #异色捕捉
            if values['choice'] == 'yise2':
                yizhong.start(yise=True, padding=isPadding)

            if values['choice'] == 'tianqi':
                if values['tiger'] == True:
                    tianqi.start(isPadding,0)
                if values['cat'] == True:
                    tianqi.start(isPadding,1)
            
            if values['choice'] == 'test':
                print("测试")
                test.start()
                

        if k == '2':
            #技能预设
            if values['input1'] or values['input2'] or values['input3']:
                print(values['input1'],values['input2'],values['input3'])
                jn_list = [values['input1'], values['input2'], values['input3']]
                io.w_skill(jn_list)
                str_val = ','.join(io.r_skill())
                jn_val = "技能预设为：" + str_val
                Dialog.alert(jn_val,'知道了')
                print("技能预设成功")

            # if values['input1'] or values['input2'] or values['input3']:
            #     jn_list = [values['input1'], values['input2'], values['input3']]
            #     io.w_skill(jn_list)
            #     tianqi.start(isPadding,values['input1'],values['input2'],values['input3'])


    w = WebWindow(R.ui('a.html'),tunnel)
    print("加载网页")
    w.mode(0)
    w.show()


start()

# path = R.res("/img/精灵集团.png")
# while True:
#     res = FindImages.find(path,rect = rc(931,253,1908,910),confidence=0.5)

#     if res:
#         print("中心坐标:",res["center_x"],res["center_y"])
#         print("相似度:",res["confidence"])
#         print("在屏幕中的范围:",res["rect"])
#         action.click(res["center_x"],res["center_y"])
#         break
