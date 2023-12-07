from PIL import Image, ImageDraw, ImageFont
import random

SQUARE_COLOR = "black"
DEFAULT_AREA_COLOR = "lightgray"

def generate_blank_image(width, height, background_color="white"):
    image = Image.new("RGB", (width, height), background_color)
    return image

def draw_square_border(draw, position, size, border_width, number=None):
    x, y = position
    draw.rectangle(
        [(x, y), (x + size, y + size)],
        outline=SQUARE_COLOR,
        width=border_width
    )
    if number is not None:
        font = ImageFont.load_default()
        text_bbox = draw.textbbox((0, 0, 0, 0), str(number), font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_position = (x + (size - text_width) // 2, y + size)
        draw.text(text_position, str(number), fill=SQUARE_COLOR, font=font)

def generate_group_of_squares(draw, square_size, border_width, area_position, word, area_color=DEFAULT_AREA_COLOR):
    total_width = (square_size - border_width) * len(word) + border_width * (len(word) - 1)
    group_height = square_size

    x_position = area_position[0]
    y_position = area_position[1]

    for i, char in enumerate(word):
        if i > 0:
            x_position += border_width
        square_position = (x_position + i * (square_size - border_width), y_position)
        draw_square_border(draw, square_position, square_size, border_width, number=ord(char.lower()) - ord('a') + 1)

    return x_position + total_width  # 返回单词的右边界，用于确定下一个单词的位置

def generate_dom_image(A4_WIDTH=595, A4_HEIGHT=842, square_size=30, border_width=2, area_position=(50, 50), area_size=(400, 600), words=["love", "father", "doctor"], area_color=DEFAULT_AREA_COLOR):
    a4_image = generate_blank_image(A4_WIDTH, A4_HEIGHT)

    draw = ImageDraw.Draw(a4_image)
    current_x = area_position[0]
    current_y = area_position[1]

    for word in words:
        total_width = generate_group_of_squares(draw, square_size, border_width, (current_x, current_y), word, area_color)
        current_x = total_width + 30  # 考虑两个单词之间的左边距

        # 如果超出 A4 纸的宽度，换行
        if current_x + total_width > A4_WIDTH:
            current_x = area_position[0]
            current_y += square_size + 20  # 考虑两行之间的垂直间距

    return a4_image

if __name__ == "__main__":
    square_size = 30
    border_width = 2
    area_position = (50, 50)
    area_size = (400, 600)
    words = ["love", "father", "doctor",'apple', 'banana', 'cat', 'dog', 'elephant', 'fish', 'grape', 'house', 'icecream', 'juice', 'kite', 'lion']

    dom_image = generate_dom_image(square_size=square_size, border_width=border_width, area_position=area_position, area_size=area_size, words=words)

    dom_image.show()
