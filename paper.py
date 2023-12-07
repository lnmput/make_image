from PIL import Image


def create_paper():
    # A4纸的标准尺寸
    a4_width, a4_height = 2480, 3508

    # 创建一个白色背景的A4图片
    background_color = (255, 255, 255)  # 白色
    image = Image.new("RGB", (a4_width, a4_height), background_color)

    return image, a4_width, a4_height
