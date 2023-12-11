from left import create_left_area
from paper import create_paper
from profile import add_profile_text
from right import create_right_area
import random

from title import add_title_text

if __name__ == "__main__":
    # 你的单词列表
    word_list = [
        "apple", "pear", "peach", "strawberry", "grape", "kiwi", "banana", "watermelon",
        "orange", "mango", "lemon", "cherry", "tomato", "hamimelon", "peanut",
    ]

    title = "我的石锅鱼"

    # 从单词列表中随机选择一些单词
    selected_words = random.sample(word_list, k=22)

    image, a4_width, a4_height = create_paper()

    add_profile_text(image)
    add_title_text(image, title)

    create_left_area(image, a4_width, a4_height)

    create_right_area(image, selected_words)
