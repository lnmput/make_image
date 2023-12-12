import random

from core.left import create_left_area
from core.paper import create_paper
from core.profile import add_profile_text
from core.right import create_right_area
from core.title import add_title_text

if __name__ == "__main__":
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
