from PIL import ImageDraw, ImageFont
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
        font_size = 40
        font = ImageFont.truetype("arial.ttf", font_size)

        text_bbox = draw.textbbox((0, 0, 0, 0), str(number), font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_position = (x + (size - text_width) // 2, y + size)
        draw.text(text_position, str(number), fill=SQUARE_COLOR, font=font)


def generate_group_of_squares(image, square_size, border_width, area_position, area_size, word,
                              area_color=DEFAULT_AREA_COLOR):
    draw = ImageDraw.Draw(image)
    draw.rectangle([area_position, (area_position[0] + area_size[0], area_position[1] + area_size[1])], fill=area_color)

    total_width = (square_size - border_width) * len(word) + border_width * (len(word) - 1)
    group_height = square_size

    x_position = random.randint(area_position[0], area_position[0] + area_size[0] - total_width)
    y_position = random.randint(area_position[1], area_position[1] + area_size[1] - group_height)

    for i, char in enumerate(word):
        if i > 0:
            x_position += border_width
        square_position = (x_position + i * (square_size - border_width), y_position)
        draw_square_border(draw, square_position, square_size, border_width, number=ord(char.lower()) - ord('a') + 1)

    return image


def generate_dom_image(a4_image, square_size=30, border_width=2, area_position=(50, 50),
                       area_size=(400, 600), word="love", area_color=DEFAULT_AREA_COLOR):
    generate_group_of_squares(a4_image, square_size, border_width, area_position, area_size, word, area_color)
    return a4_image


def create_right_area(paper):
    square_size = 100  # 矩形的边长
    border_width = 5  # 矩形的border
    area_position = (500, 500)  # 右边 左上角 坐标
    area_size = (1900, 2900)  # 右边整个宽度和高度

    word = "love"  # 单词

    dom_image = generate_dom_image(paper, square_size=square_size, border_width=border_width,
                                   area_position=area_position,
                                   area_size=area_size, word=word)

    dom_image.save("output_image.png")

    dom_image.show()
