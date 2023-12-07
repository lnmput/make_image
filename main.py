from PIL import Image, ImageDraw
import random

def generate_blank_a4_image():
    """
    生成一个白色背景的A4纸大小的图片
    """
    width, height = 595, 842  # A4纸的大小
    image = Image.new("RGB", (width, height), "white")
    return image

def draw_square_border(draw, position, size, border_width):
    """
    在图片上绘制一个正方形边框
    """
    x, y = position
    draw.rectangle(
        [(x, y), (x + size, y + size)],
        outline="black",
        width=border_width
    )

def generate_group_of_squares(image, square_size, border_width, area_position, area_size, area_color):
    """
    在指定区域内生成一组正方形边框
    """
    draw = ImageDraw.Draw(image)

    # 在指定区域绘制背景颜色
    x1, y1 = area_position
    x2, y2 = x1 + area_size[0], y1 + area_size[1]
    draw.rectangle([area_position, (x2, y2)], fill=area_color)

    # 计算组内5个矩形边框组合排列到一起的长度以及高度
    group_width = 5 * (square_size - border_width) + border_width
    group_height = square_size

    # 计算在指定区域内的随机位置
    x_position = random.randint(area_position[0], area_position[0] + area_size[0] - group_width)
    y_position = random.randint(area_position[1], area_position[1] + area_size[1] - group_height)

    # 绘制一组正方形边框
    for i in range(5):
        square_position = (x_position + i * (square_size - border_width), y_position)
        draw_square_border(draw, square_position, square_size, border_width)

    return image

if __name__ == "__main__":
    # 设置正方形边框的大小以及边框宽度
    square_size = 50
    border_width = 2

    # 生成A4大小的图片
    a4_image = generate_blank_a4_image()

    # 设置指定区域的位置、大小和背景颜色
    area_position = (50, 50)  # 从左上角开始
    area_size = (400, 600)    # 指定区域的宽度和高度
    area_color = "lightgray"  # 指定区域的背景颜色

    # 生成一组正方形边框在指定区域内随机放置
    image_with_squares = generate_group_of_squares(a4_image, square_size, border_width, area_position, area_size, area_color)

    # 显示生成的图片
    image_with_squares.show()
