import pygame
import random
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT
from os import listdir

pygame.init()

FPS = pygame.time.Clock()
CREATE_ENEMY = pygame.USEREVENT + 1
CREATE_BONUS = pygame.USEREVENT + 2
CHANGE_IMG = pygame.USEREVENT + 3
IMG_PATH = 'images/animated/'
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
BALL_SIZE = (100, 50)
ENEMY_SIZE = (100, 50)
BONUS_SIZE = (100, 100)

is_working = True
img_index = 0
scores = 0
enemies = []
bonuses = []
screen = width, height = 800, 600
font = pygame.font.SysFont('Verdana', 20)
main_surface = pygame.display.set_mode(screen)
bg = pygame.transform.scale(pygame.image.load('images/background.png').convert(), screen)
bgX = 0
bgX2 = bg.get_width()
bg_speed = 3

ball_img = [pygame.image.load(IMG_PATH + '/' + file).convert_alpha() for file in listdir(IMG_PATH)]
ball = pygame.transform.scale(pygame.image.load('images/player.png').convert_alpha(), BALL_SIZE)
ball_rect = ball.get_rect()
ball_speed = 5

def create_enemy():
    enemy = pygame.transform.scale(pygame.image.load('images/enemy.png').convert_alpha(), ENEMY_SIZE)
    enemy_rect = pygame.Rect(width, random.randint(0, height), *enemy.get_size())
    enemy_speed = random.randint(2, 5)
    return [enemy, enemy_rect, enemy_speed]


def create_bonuses():
    bonus = pygame.transform.scale(pygame.image.load('images/bonus.png').convert_alpha(), BONUS_SIZE)
    bonus_rect = pygame.Rect(random.randint(0, width), 0, *bonus.get_size())
    bonus_speed = random.randint(2, 5)
    return [bonus, bonus_rect, bonus_speed]


pygame.time.set_timer(CREATE_ENEMY, 1500)
pygame.time.set_timer(CREATE_BONUS, 2000)
pygame.time.set_timer(CHANGE_IMG, 250)


while is_working:

    FPS.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonuses())
        if event.type == CHANGE_IMG:
            img_index += 1
            if img_index == len(ball_img):
                img_index = 0
            ball = ball_img[img_index]

    pressed_keys = pygame.key.get_pressed()

    bgX -= bg_speed
    bgX2 -= bg_speed

    if bgX < -bg.get_width():
        bgX = bg.get_width()

    if bgX2 < -bg.get_width():
        bgX2 = bg.get_width()

    main_surface.blit(bg, (bgX, 0))
    main_surface.blit(bg, (bgX2, 0))

    main_surface.blit(ball, ball_rect)
    main_surface.blit(font.render(str(scores), True, RED), (width - 30, 0))
    for enemy in enemies:
        enemy[1] = enemy[1].move(-enemy[2], 0)
        main_surface.blit(enemy[0], enemy[1])

        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))

        if ball_rect.colliderect(enemy[1]):
            is_working = False

    for bonus in bonuses:
        bonus[1] = bonus[1].move(0, bonus[2])
        main_surface.blit(bonus[0], bonus[1])

        if bonus[1].bottom > height:
            bonuses.pop(bonuses.index(bonus))

        if ball_rect.colliderect(bonus[1]):
            bonuses.pop(bonuses.index(bonus))
            scores += 1

    if pressed_keys[K_DOWN] and ball_rect.bottom < height:
        ball_rect = ball_rect.move((0, ball_speed))
    if pressed_keys[K_UP] and ball_rect.top > 0:
        ball_rect = ball_rect.move((0, -ball_speed))

    if pressed_keys[K_RIGHT] and ball_rect.right < width:
        ball_rect = ball_rect.move((ball_speed, 0))
    if pressed_keys[K_LEFT] and ball_rect.left > 0:
        ball_rect = ball_rect.move((-ball_speed, 0))

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
