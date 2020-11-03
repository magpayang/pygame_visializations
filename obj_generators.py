
from rectangles import GroundedRect
import my_maths


def _color_init(color, number_of_rects, color_offset):
    if color.lower()=="red":
        r_red_color = (255//(number_of_rects+color_offset))*(number_of_rects+color_offset)
        r_blue_color = 0
        r_green_color = 0
    elif color.lower()=="blue":
        r_red_color = 0
        r_blue_color = (255//(number_of_rects+color_offset))*(number_of_rects+color_offset)
        r_green_color = 0
    else:
        r_red_color = 0
        r_blue_color = 0
        r_green_color = (255//(number_of_rects+color_offset))*(number_of_rects+color_offset)

    return r_red_color, r_green_color, r_blue_color

def _color_update(color, r_red_color, r_green_color, r_blue_color, number_of_rects, color_offset):
    if color.lower() == "red":
        r_red_color -= 255 // (number_of_rects + color_offset)
    elif color.lower() == "blue":
        r_blue_color -= 255 // (number_of_rects + color_offset)
    else:
        r_green_color -= 255 // (number_of_rects + color_offset)

    return r_red_color, r_green_color, r_blue_color

def generate_ascending(screen, number_of_rectangles, xn_width, xn_height, initial_height, height_increment, y_offset = 0, xn_offset = 0, color="Red", color_offset = 5):
    """
    Generates grounded rects of ascending height
    :return:
    """
    number_of_rects = number_of_rectangles
    obj_holder_array = []
    r_y_pos = 0 + y_offset  # constant
    r_width = xn_width/number_of_rects
    r_height = initial_height
    r_red_color, r_green_color, r_blue_color = _color_init(color, number_of_rectangles, color_offset)
    r_color = (r_red_color, r_green_color, r_blue_color)
    r_show = True
    for i in range(number_of_rects):
        r_x_pos = (i*r_width)+xn_offset

        obj_holder_array.append(GroundedRect(screen, xn_width, xn_height, r_x_pos, r_y_pos, r_width, r_height, r_color, r_show))

        r_height += height_increment
        r_red_color, r_green_color, r_blue_color = _color_update(color, r_red_color, r_green_color, r_blue_color, number_of_rectangles, color_offset)
        r_color = (r_red_color, r_green_color, r_blue_color)

    return obj_holder_array


def generate_from_array(screen, input_array, xn_width, xn_height, minimum_height, height_increment, y_offset = 0, xn_offset = 0, color="Red", color_offset=5):
    obj_holder_array = []
    number_of_rectangles = len(input_array)
    r_width = xn_width / len(input_array)
    r_y_pos = 0 + y_offset  # constant
    # r_height = minimum_height
    r_red_color, r_green_color, r_blue_color = _color_init(color, number_of_rectangles, color_offset)
    r_color = (r_red_color, r_green_color, r_blue_color)

    max_entry = my_maths.max_arrays(input_array)
    # sum = my_maths.sum_arrays(input_array)
    for entry in input_array:
        r_x_pos = ((input_array.index(entry))*r_width)+xn_offset

        r_height = height_increment*(entry/max_entry)+minimum_height
        obj_holder_array.append(GroundedRect(screen, xn_width, xn_height, r_x_pos, r_y_pos, r_width, r_height, r_color, show=True))


        r_red_color, r_green_color, r_blue_color = _color_update(color, r_red_color, r_green_color, r_blue_color, number_of_rectangles, color_offset)
        r_color = (r_red_color, r_green_color, r_blue_color)

    return obj_holder_array