from PIL import Image

def remove_non_white(image_path, output_path, tolerance=200):
    # 打开图片
    img = Image.open(image_path).convert("RGBA")
    datas = img.getdata()

    new_data = []
    
    for item in datas:
        # 将白色和接近白色的颜色保留，其他的颜色变成透明
        if item[0] > tolerance and item[1] > tolerance and item[2] > tolerance:
            new_data.append(item)  # 保持原来的像素
        else:
            new_data.append((255, 255, 255, 0))  # 其他部分变成透明

    img.putdata(new_data)
    img.save(output_path, "PNG")
    print(f"处理后的图片已保存为: {output_path}")

# 示例用法
image_path = "input_image.png"  # 输入图片路径
output_path = "output_image.png"  # 输出图片路径
remove_non_white(image_path, output_path)
