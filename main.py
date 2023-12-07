from left import create_area_box
from paper import create_paper
from right import create_right_area

if __name__ == "__main__":

    image, a4_width, a4_height = create_paper()

    image = create_area_box(image, a4_width, a4_height)

    create_right_area(image)





