import pygame
import sys
import os
import bullet
from pygame.locals import *


class Player(pygame.sprite.Sprite):  # 继承Sprite精灵类
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # 设置血条
        self.blood = 3
        self.images = []  # 用来存储玩家对象精灵图片的列表
        for i in range(1, 5):
            img = pygame.image.load(os.path.join('assets', 'PLAYER' + '.png')).convert()
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
        self.x = 400
        self.y = 300
        # self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50
        # self.image = None
        self.key_right_status = False
        self.key_left_status = False
        self.key_down_status = False
        self.key_up_status = False

    def update(self):
        if self.key_right_status:
            self.x += 5
        if self.key_left_status:
            self.x -= 5
        if self.key_down_status:
            self.y += 5
        if self.key_up_status:
            self.y -= 5

    def fire(self):
        myBullet = bullet.Bullet(0, 0, "left")
        myBullet.rect.bottom = self.rect.y + 10

    def key_control(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    self.key_left_status = True
                elif event.key == K_d or event.key == K_RIGHT:
                    self.key_right_status = True
                elif event.key == K_w or event.key == K_UP:
                    self.key_up_status = True
                elif event.key == K_s or event.key == K_DOWN:
                    self.key_down_status = True
                elif event.key == K_SPACE:
                    self.fire()
            elif event.type == KEYUP:
                if event.key == K_a or event.key == K_RIGHT:
                    self.key_right_status = False
                elif event.key == K_d or event.key == K_RIGHT:
                    self.key_right_status = False
                elif event.key == K_w or event.key == K_UP:
                    self.key_up_status = False
                elif event.key == K_s or event.key == K_DOWN:
                    self.key_down_status = False
