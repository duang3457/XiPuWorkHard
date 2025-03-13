from ascript.android.system import R

import os

from . import rect

path = R.sd("xipuhugan")
hS_img_path = R.sd("xipuhugan/hS_img")
jn_path = R.sd("xipuhugan/jn")

# 创建xipuhugan文件夹
if not os.path.exists(path):
    os.mkdir(path)
    
# 创建xipuhugan/hS_img文件夹
if not os.path.exists(hS_img_path):
    os.mkdir(hS_img_path)


def record(content, times):
    txt_path = os.path.join(path, "hs_record.txt")
    with open(txt_path, mode='a') as file:
        content = f"{content} 在第{times}次\n"
        file.write(content)

# test用
def getScreen(count):
    
    screen.bitmap_to_file(R.sd(f"xipuhugan/hS_img/{count}.png"),bitmap=screen.capture(1085,263,1805,907), quality=80)


def w_skill(jn_list):
    if not os.path.exists(jn_path):
        os.mkdir(jn_path)
    jn_file_path = os.path.join(jn_path, "jn_record.txt")
    
    # 将列表元素通过换行符拼接成一个字符串
    jn_str = '\n'.join(jn_list)
    
    # 使用 'w' 模式打开文件，这会替换文件的内容
    with open(jn_file_path, mode='w') as file:
        file.write(jn_str)



def r_skill():
    jn_file_path = os.path.join(jn_path, "jn_record.txt")
    
    # 检查文件夹路径是否存在，如果不存在则创建
    if not os.path.exists(jn_path):
        os.mkdir(jn_path)
    
    # 检查文件是否存在，如果不存在则创建空文件
    if not os.path.exists(jn_file_path):
        with open(jn_file_path, mode='w') as file:
            pass  # 创建一个空文件
    
    # 打开文件并按行读取内容，返回一个列表
    with open(jn_file_path, mode='r') as file:
        content = file.readlines()
    
    # 移除每行末尾的换行符
    if content:
        content = [line.strip() for line in content]
    
    return content  # 返回按行读取的列表




