from PIL import Image, ImageDraw, ImageFont
import random

A4_WIDTH, A4_HEIGHT = 595, 842  # A4纸的大小
SQUARE_COLOR = "black"
AREA_COLOR = "lightgray"

def generate_blank_image(width, height, background_color="white"):
    """
    生成一个指定背景颜色的图片
    """
    image = Image.new("RGB", (width, height), background_color)
    return image

def draw_square_border(draw, position, size, border_width, number=None):
    """
    在图片上绘制一个正方形边框，可选择添加数字
    """
    x, y = position
    draw.rectangle(
        [(x, y), (x + size, y + size)],
        outline=SQUARE_COLOR,
        width=border_width
    )
    if number is not None:
        # 在正方形下方绘制数字
        font = ImageFont.load_default()  # 使用默认字体
        text_bbox = draw.textbbox((0, 0, 0, 0), str(number), font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_position = (x + (size - text_width) // 2, y + size)
        draw.text(text_position, str(number), fill=SQUARE_COLOR, font=font)

def generate_group_of_squares(image, square_size, border_width, area_position, area_size, word):
    """
    在指定区域内生成一组正方形边框，每个正方形下方添加相应的数字
    """
    draw = ImageDraw.Draw(image)

    # 在指定区域绘制背景颜色
    draw.rectangle([area_position, (area_position[0] + area_size[0], area_position[1] + area_size[1])], fill=AREA_COLOR)

    # 计算组内多个矩形边框组合排列到一起的长度以及高度
    total_width = (square_size - border_width) * len(word) + border_width * (len(word) - 1)
    group_height = square_size

    # 计算在指定区域内的随机位置
    x_position = random.randint(area_position[0], area_position[0] + area_size[0] - total_width)
    y_position = random.randint(area_position[1], area_position[1] + area_size[1] - group_height)

    # 绘制一组正方形边框
    for i, char in enumerate(word):
        if i > 0:
            x_position += border_width  # 为了保持边框之间的间隔
        square_position = (x_position + i * (square_size - border_width), y_position)
        draw_square_border(draw, square_position, square_size, border_width, number=ord(char.lower()) - ord('a') + 1)

    return image

if __name__ == "__main__":
    # 设置正方形边框的大小以及边框宽度
    square_size = 30
    border_width = 2

    # 生成A4大小的图片
    a4_image = generate_blank_image(A4_WIDTH, A4_HEIGHT)

    # 设置指定区域的位置和大小
    area_position = (50, 50)  # 从左上角开始
    area_size = (400, 600)    # 指定区域的宽度和高度

    # 指定单词
    word = "secret"

    # 生成正方形边框在指定区域内，每个正方形下方添加相应的数字
    generate_group_of_squares(a4_image, square_size, border_width, area_position, area_size, word)

    # 显示生成的图片
    a4_image.show()
