from PIL import Image, ImageDraw, ImageFont
import random

SQUARE_COLOR = "black"
DEFAULT_AREA_COLOR = "lightgray"


def draw_square_border(draw, position, size, border_width, number=None):
    x, y = position
    draw.rectangle(
        [(x, y), (x + size, y + size)],
        outline=SQUARE_COLOR,
        width=border_width
    )
    if number is not None:
        font_size = 48
        font = ImageFont.truetype("arial.ttf", font_size)

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


def generate_group_of_squares(image, square_size, border_width, area_position, area_size, words, area_color=DEFAULT_AREA_COLOR):
    draw = ImageDraw.Draw(image)
    draw.rectangle([area_position, (area_position[0] + area_size[0], area_position[1] + area_size[1])], fill=area_color)

    x_offset = 0
    y_offset = 0
    max_width = area_size[0]
    group_height = square_size

    existing_squares = []

    x_offset = random.randint(50, 150)  # 控制第一行第一组图片与右边界的随机距离
    y_offset = 0

    for word in words:
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

            draw_square_border(draw, square_position, square_size, border_width, number=ord(char.lower()) - ord('a') + 1)
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
    area_position = (500, 500)  # 右边 左上角 坐标
    area_size = (1900, 2900)  # 右边整个宽度和高度

    dom_image = generate_dom_image(paper, square_size=square_size, border_width=border_width,
                                   area_position=area_position,
                                   area_size=area_size, words=words)

    dom_image.save("output_image.png")

    dom_image.show()


def create_paper():
    # A4纸的标准尺寸
    a4_width, a4_height = 2480, 3508

    # 创建一个白色背景的A4图片
    background_color = (255, 255, 255)  # 白色
    image = Image.new("RGB", (a4_width, a4_height), background_color)

    return image, a4_width, a4_height


if __name__ == "__main__":


    image, a4_width, a4_height = create_paper()

    # 你的单词列表
    word_list = ["love", "peace", "joy", "python", "coding", "art", "music", "science", "nature", "happy", "friend",
                 "family", "travel", "beach", "dream", "smile", "laughter", "freedom", "inspire", "create", "hope",
                 "kindness", "success", "blessing", "harmony", "courage", "imagine", "serenity", "balance", "gratitude"]

    # 从单词列表中随机选择一些单词
    selected_words = random.sample(word_list, k=20)

    create_right_area(image, selected_words)