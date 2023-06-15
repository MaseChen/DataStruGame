import pygame
import sys
import os
import bullet
import time
from pygame.locals import *

import game_launcher


class Player(pygame.sprite.Sprite):  # 继承Sprite精灵类
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # 设置血条
        self.blood = 3
        self.speed = 5
        self.shields = 0
        self.damage = 1
        self.time_damage = 0
        self.time_speed = 0
        self.time = 0
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
        self.time = time.time()
        if self.time - self.time_damage >= game_launcher.TIME_DAMAGE:
            self.damage_down()
        if self.time - self.time_speed >= game_launcher.TIME_SPEED:
            self.speed_down()

        if self.rect.x < game_launcher.WIDTH - game_launcher.WIDTH_PLAYER:
            if self.key_right_status:
                self.rect.x += self.speed
        if self.rect.x > 0:
            if self.key_left_status:
                self.rect.x -= self.speed
        if self.rect.y < game_launcher.HEIGHT - game_launcher.HEIGHT_PLAYER:
            if self.key_down_status:
                self.rect.y += self.speed
        if self.rect.y > 0:
            if self.key_up_status:
                self.rect.y -= self.speed

    def hurt(self, amount):
        if self.shields > 0:
            self.shields -= amount
        else:
            self.shields = 0
            self.blood -= amount
        if self.blood <= 0:
            sys.exit()

    def add_blood(self):
        self.blood += 1
        if self.blood > 3:
            self.blood = 3


    def Shields(self):
        self.shields = 1


    def damage_up(self):
        self.damage = 5
        self.time_damage = time.time()

    def damage_down(self):
        self.damage = 1

    def speed_up(self):
        self.speed = 10
        self.time_speed = time.time()

    def speed_down(self):
        self.speed = 5


    def fire(self):
        return bullet.Bullet(self.rect.x + game_launcher.WIDTH_PLAYER/2 - game_launcher.WIDTH_BULLET/2, self.rect.y + game_launcher.HEIGHT_PLAYER/2 - game_launcher.HEIGHT_BULLET/2, self.last_moving_status,self.damage)

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
