import pygame
import time
import random

from rectangles import *
import obj_generators
import sorting_algo

pygame.init()

# screen properties
# xn_width = 512
xn_width = 500
xn_height = xn_width
xn_size = xn_width, xn_height
screen = pygame.display.set_mode(xn_size)
xn_refresh_count = 9

# time properties
delay = 0.1

number_of_rectangles = 20
range_multiplier = 300
initial_height = xn_height//4
loop_count = 0
counter = 0
stop = False
while True:
    time.sleep(delay)
    if not stop:
        screen.fill((0,0,0))

    if loop_count==0:
        input_array = random.sample(range(number_of_rectangles*range_multiplier), number_of_rectangles)
    elif loop_count==number_of_rectangles-1:
        loop_count=0
        continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit()

    input_array = sorting_algo.sequential_sort_one_pass(input_array)  # sorted array one pass
    height_increment = initial_height
    obj_holder_array_2 = obj_generators.generate_from_array(screen, input_array, xn_width, xn_height,
                                                            initial_height - (initial_height / 4), height_increment,
                                                            color="Green")

    for entry in obj_holder_array_2:
        entry.draw()


    loop_count+=1
    pygame.display.flip()
