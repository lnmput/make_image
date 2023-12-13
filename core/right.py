from PIL import Image, ImageDraw, ImageFont
import random


SQUARE_COLOR = "black"
DEFAULT_AREA_COLOR = "lightgray"


def draw_square_border(draw, position, size, border_width, number=None):
    x, y = position
    draw.rectangle(
        [(x, y), (x + size, y + size)],
        outline=SQUARE_COLOR,
        width=2  # 边界宽度设置为 2
    )
    if number is not None:
        font_size = 48
        font = ImageFont.truetype("./fonts/arial.ttf", font_size)

        text_bbox = draw.textbbox((0, 0, 0, 0), str(number), font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_position = (x + (size - text_width) // 2, y + size)
        draw.text(text_position, str(number), fill=SQUARE_COLOR, font=font)


def is_overlap(square_position, square_size, existing_squares):
    """
    检查新的正方形是否与已有的正方形相交
    """
    x1, y1 = square_position
    x2, y2 = x1 + square_size, y1 + square_size

    for existing_square in existing_squares:
        ex1, ey1, ex2, ey2 = existing_square
        if not (x2 < ex1 or x1 > ex2 or y2 < ey1 or y1 > ey2):
            return True  # 相交

    return False  # 不相交


def generate_group_of_squares(image, square_size, border_width, area_position, area_size, words,
                              area_color=DEFAULT_AREA_COLOR):
    draw = ImageDraw.Draw(image)

    # 假设外边距为 margin
    margin = 20  # 可以根据需要调整外边距的大小

    # 调整 area_position 和 area_size 以添加外边距
    draw.rectangle(
        [
            (area_position[0] - margin, area_position[1] - margin),
            (
                area_position[0] + area_size[0] + margin,
                area_position[1] + area_size[1] + margin,
            ),
        ],
        fill=area_color
    )

    x_offset = 0
    y_offset = 0
    max_width = area_size[0]
    group_height = square_size

    existing_squares = []

    x_offset = random.randint(50, 150)  # 控制第一行第一组图片与右边界的随机距离
    y_offset = 0

    for word in words:
        word = word.lower()
        # 去掉空格
        word = word.replace(" ", "")
        total_width = (square_size - border_width) * len(word) + border_width * (len(word) - 1)

        if x_offset + total_width > max_width:
            x_offset = random.randint(50, 150)  # 控制下一行第一组图片与右边界的随机距离
            y_offset += group_height + random.randint(100, 200)  # 上下随机间距
            if y_offset + group_height > area_size[1]:
                break  # 如果超出右边界，停止生成

        for i, char in enumerate(word):
            if i > 0:
                x_offset += border_width
            square_position = (area_position[0] + x_offset, area_position[1] + y_offset)

            draw_square_border(draw, square_position, square_size, border_width,
                               number=ord(char.lower()) - ord('a') + 1)
            existing_squares.append((square_position[0], square_position[1], square_position[0] + square_size,
                                     square_position[1] + square_size))

            x_offset += square_size - border_width

        x_offset += random.randint(50, 100)  # 组与组之间的左右随机间距

    return image


def generate_dom_image(a4_image, square_size=30, border_width=2, area_position=(50, 50),
                       area_size=(400, 600), words=None, area_color=DEFAULT_AREA_COLOR):
    if words is None:
        words = ["love"]

    generate_group_of_squares(a4_image, square_size, border_width, area_position, area_size, words, area_color)
    return a4_image


def create_right_area(paper, words):
    square_size = 120  # 矩形的边长
    border_width = 5  # 矩形的border
    area_position = (520, 500)  # 右边 左上角 坐标
    area_size = (1860, 2880)  # 右边整个宽度和高度

    dom_image = generate_dom_image(paper, square_size=square_size, border_width=border_width,
                                   area_position=area_position,
                                   area_size=area_size, words=words)

    # dom_image.save("output_image.png")

    # return dom_image.show()


