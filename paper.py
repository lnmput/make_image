from PIL import Image


def create_paper():
    width = 595
    height = 842
    background_color = "white"

    image = Image.new("RGB", (width, height), background_color)
    return image
