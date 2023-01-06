from time import sleep
import np as np
import pygame
from pygame.constants import QUIT

pygame.init()

screen = width, height = 800, 600
BLACK = 0, 0, 0
WHITE = 255, 255, 255
ball = pygame.Surface((20, 20))
ball.fill(WHITE)
ball_rect = ball.get_rect()
ball_speed = [1, 1]
main_surface = pygame.display.set_mode(screen)
is_working = True


def random_color():
    return ball.fill(list(np.random.choice(range(256), size=3)))


while is_working:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False
    ball_rect = ball_rect.move(ball_speed)
    sleep(0.001)

    if ball_rect.bottom >= height or ball_rect.top <= 0:
        ball_speed[1] = -ball_speed[1]
        random_color()

    if ball_rect.left <= 0 or ball_rect.right >= width:
        ball_speed[0] = -ball_speed[0]
        random_color()

    main_surface.fill(BLACK)
    main_surface.blit(ball, ball_rect)
    pygame.display.flip()




# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
