from left import create_left_area
from paper import create_paper
from right import create_right_area
import random

from title import add_rectangle_text

if __name__ == "__main__":
    image, a4_width, a4_height = create_paper()

    add_rectangle_text(image)

    create_left_area(image, a4_width, a4_height)




    # 你的单词列表
    word_list = ["love", "peace", "joy", "python", "coding", "art", "music", "science", "nature", "happy", "friend",
                 "family", "travel", "beach", "dream", "smile", "laughter", "freedom", "inspire", "create", "hope",
                 "kindness", "success", "blessing", "harmony", "courage", "imagine", "serenity", "balance", "gratitude"]

    # 从单词列表中随机选择一些单词
    selected_words = random.sample(word_list, k=20)

    create_right_area(image, selected_words)
