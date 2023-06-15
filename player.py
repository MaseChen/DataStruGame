import pygame
import sys
import os
import bullet
from pygame.locals import *

import game_launcher


class Player(pygame.sprite.Sprite):  # 继承Sprite精灵类
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # 设置血条
        self.blood = 3
        self.images = []  # 用来存储玩家对象精灵图片的列表
        for i in range(1, 5):
            img = pygame.image.load(os.path.join('assets', 'PLAYER' + '.png')).convert()
            img = pygame.transform.scale(img, (50, 50))  # Resize image
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
        # self.x = 400
        # self.y = 300
        # self.rect = self.image.get_rect()
        self.rect.x = 60
        self.rect.y = 400
        # self.image = None
        self.key_right_status = False
        self.key_left_status = False
        self.key_down_status = False
        self.key_up_status = False

        self.last_moving_status = "right"

    def update(self):
        if self.rect.x < game_launcher.WIDTH - game_launcher.WIDTH_PLAYER:
            if self.key_right_status:
                self.rect.x += 5
        if self.rect.x > 0:
            if self.key_left_status:
                self.rect.x -= 5
        if self.rect.y < game_launcher.HEIGHT - game_launcher.HEIGHT_PLAYER:
            if self.key_down_status:
                self.rect.y += 5
        if self.rect.y > 0:
            if self.key_up_status:
                self.rect.y -= 5

    def hurt(self, amount):
        self.blood -= amount
        if self.blood <= 0:
            sys.exit()

    def fire(self):
        return bullet.Bullet(self.rect.x + game_launcher.WIDTH_PLAYER/2 - game_launcher.WIDTH_BULLET/2, self.rect.y + game_launcher.HEIGHT_PLAYER/2 - game_launcher.HEIGHT_BULLET/2, self.last_moving_status)

    def go_up_begin(self):
        self.key_up_status = True
        self.last_moving_status = "up"

    def go_down_begin(self):
        self.key_down_status = True
        self.last_moving_status = "down"

    def go_left_begin(self):
        self.key_left_status = True
        self.last_moving_status = "left"

    def go_right_begin(self):
        self.key_right_status = True
        self.last_moving_status = "right"

    def go_up_end(self):
        self.key_up_status = False

    def go_down_end(self):
        self.key_down_status = False

    def go_left_end(self):
        self.key_left_status = False

    def go_right_end(self):
        self.key_right_status = False
