from PIL import Image, ImageDraw, ImageFont


def add_title_text(image, title):
    # 创建画布对象
    draw = ImageDraw.Draw(image)

    # 矩形的位置参数 (左上角x坐标, 左上角y坐标, 右下角x坐标, 右下角y坐标)
    rect_position = (500, 190, 2400, 400)  # 调整后的位置参数

    # 矩形的背景颜色（灰色）
    rect_color = (169, 169, 169)  # 灰色

    # 在指定位置绘制矩形
    draw.rectangle(rect_position, fill=rect_color)

    # 获取字体
    font_size = 80
    font = ImageFont.truetype("./fonts/arial.ttf", font_size)

    # 计算适应矩形大小的字体大小
    while True:
        # 获取文字的尺寸
        text_bbox = draw.textbbox((0, 0), title, font=font)
        text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

        # 检查文字是否超出矩形边框
        if text_width <= rect_position[2] - rect_position[0] and text_height <= rect_position[3] - rect_position[1]:
            break

        # 如果文字超出矩形边框，减小字体大小并重新计算
        font_size -= 1
        font = ImageFont.truetype("./fonts/arial.ttf", font_size)

    # 计算文字位置使其上下居中在矩形内
    text_x = (rect_position[2] + rect_position[0] - text_width) / 2
    text_y = (rect_position[3] + rect_position[1] - text_height) / 2 - text_bbox[1]  # 考虑文本基线位置

    # 在矩形内填充文字
    draw.text((text_x, text_y), title, fill=(0, 0, 0), font=font)

    return image