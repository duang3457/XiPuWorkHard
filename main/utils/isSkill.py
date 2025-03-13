
from ascript.android.screen import FindColors
from ascript.android.system import R

rect = __import__(R.name+".main.utils.rect",fromlist=[''])
rc = rect.rc1920

def isSkill():
    # 普通系技能
    # 火焰系技能
    # 圣系技能
    # 风系技能
    # 水系技能
    # 暗系技能
    # 土系技能
    # 龙系技能
    # 电系技能
    # 草系技能
    # 爆裂系技能
    # 钢系技能
    # 冰系技能
    if (FindColors.find("811,990,#987F6C|748,947,#8E7765|930,949,#8D7564|734,995,#A58975|924,995,#9C826F",rect=rc(338,902,1584,1065),ori= 1)
    or FindColors.find("1423,991,#B8504D|1350,947,#AB4B48|1511,946,#AA4A47|1344,993,#C25451|1493,993,#BB514E",rect=rc(338,902,1584,1065),ori= 1)
    or FindColors.find("508,986,#B59E4F|446,949,#AC964B|607,944,#AA954A|439,995,#C1A854|572,993,#BBA351",rect=rc(338,893,1584,1068),ori= 1)
    or FindColors.find("807,989,#37B398|745,947,#34A98F|889,944,#33A78D|742,995,#3BBEA1|883,995,#39B99D",rect=rc(338,893,1584,1068),ori= 1)
    or FindColors.find("509,990,#3993B6|446,952,#368AAC|584,946,#3587A8|436,992,#3C9BC0|593,996,#3B98BC",rect=rc(344,902,1584,1065),ori= 1)
    or FindColors.find("508,986,#7952B5|448,947,#754FAD|598,947,#724DAA|443,998,#8359C3|598,998,#8157C0",rect=rc(344,902,1584,1065),ori= 1)
    or FindColors.find("501,987,#9A703B|442,947,#916A38|597,947,#906937|436,989,#9E743D|590,989,#9B713C",rect=rc(347,896,1575,1065),ori= 1)
    or FindColors.find("1109,987,#A23737|1049,949,#993434|1185,946,#983333|1044,994,#AC3A3A|1176,993,#A73838",rect=rc(347,896,1575,1065),ori= 1)
    or FindColors.find("508,992,#B9AE51|448,950,#ADA24C|578,947,#AAA04A|443,995,#C1B654|570,995,#BDB252",rect=rc(347,896,1575,1065),ori= 1)
    or FindColors.find("508,989,#70B749|446,950,#69AB44|587,947,#69AA44|443,995,#77C14D|581,995,#74BD4C",rect=rc(347,896,1575,1065),ori= 1)
    or FindColors.find("508,984,#B05C43|446,947,#A95840|587,944,#A85740|440,992,#BB6147|570,992,#B75F46|400,958,#FFFFB2",rect=rc(347,896,1575,1065),ori= 1)
    or FindColors.find("810,989,#6B838A|745,944,#637A80|906,944,#637A80|745,995,#718A91|903,995,#6F888E|708,964,#9FB6C1",rect=rc(347,896,1575,1065),ori= 1)
    or FindColors.find("505,989,#4981B6|446,944,#457AAC|587,944,#4479AA|437,992,#4D89C2|581,992,#4A84B9|400,961,#E0EEF7",rect=rc(347,896,1575,1065),ori= 1)
    ):
        return True
    else:
        return False