

# 通过GP任务,执行图片字库 获取识别结果
from ascript.android.screen.gp import GPStack
import cv2
from ascript.android.system import R
from ascript.android.screen.gp_tasks import CvFontLib
from ascript.android import action
import time


rect = __import__(R.name+".main.utils.rect",fromlist=[''])
rc = rect.rc1920

def start():
    def gp(cv_img=None):
        gp_stack = GPStack(cv_img)
        # 用R.rel获取图片相对路径
        # 哈尼熊 271,453,1033,840
        # 精灵集团 327,265,1437,704
        gp_stack.add(CvFontLib([R.rel(__file__,"../../res/img/精灵集团.png"),],['精灵集团',],rect = rc(327,265,1437,704), confidence= 0.5))
        gp_result = gp_stack.run()
        return gp_result
    # 如需运行,取消以下代码注释
    while True:
        while True:
            res = gp()
       
            if res.data:
                break
        #print(res.__dict__)
        print(res.data)
        print(res.data['words'][0][0]['result'])
        x,y = res.data['words'][0][0]['result']
        action.click(x-50,y-100,100)

        action.click(x-50,y-100,100)
        time.sleep(1)






     