import random
import io
import base64

from core.left import create_left_area
from core.paper import create_paper
from core.profile import add_profile_text
from core.right import create_right_area
from core.title import add_title_text


def make_image():
    # 你的单词列表
    word_list = [
        "apple", "pear", "peach", "strawberry", "grape", "kiwi", "banana", "watermelon",
        "orange", "mango", "lemon", "cherry", "tomato", "hamimelon", "peanut",
    ]

    title = "我的石锅鱼"

    # 设置 k 的值
    k = 30

    # 如果 k 大于 word_list 的长度，将 k 设为 word_list 的长度
    if k > len(word_list):
        k = len(word_list)

    # 从单词列表中随机选择一些单词
    selected_words = random.sample(word_list, k)

    image, a4_width, a4_height = create_paper()

    add_profile_text(image)
    add_title_text(image, title)

    create_left_area(image, a4_width, a4_height)

    create_right_area(image, selected_words)

    # 将图像转换为字节流
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")

    # 获取base64编码的图像字符串
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return img_str



