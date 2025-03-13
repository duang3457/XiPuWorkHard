

from ascript.android.system import R
from ascript.android import action
from ascript.android.screen import FindColors
from ascript.android.system import Device

import time
from time import sleep


battle = __import__(R.name+".main.function.basic.battle",fromlist=[''])


display = Device.display()
width = display.widthPixels
height = display.heightPixels


def start(**kwargs):
    padding = kwargs.get('padding', False)
    yise = kwargs.get('yise', False)
    print("异种开始")

    battle.battle(yise = yise,
                padding = padding,
                times = 99999,
                _list = ['异种'])


