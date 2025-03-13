# 这里是升级模块（还未把战斗系统封装）
# levelUp:针对无Padding机型
# levelUpP:针对有Padding机型

from ascript.android.system import R
from ascript.android import action
from ascript.android.screen import FindColors
from ascript.android.system import Device

import time
from time import sleep

rect = __import__(R.name+".main.utils.rect",fromlist=[''])
battle = __import__(R.name+".main.function.basic.battle",fromlist=[''])
rc = rect.rc1920

c = action.click

display = Device.display()
width = display.widthPixels
height = display.heightPixels


def levelUp(padding):
    print("升级")
 
    battle.battle(padding = padding,
                    pokemon_index = 0,
                    _list = ['升级'])





