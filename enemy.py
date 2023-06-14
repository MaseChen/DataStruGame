import pygame.sprite
import random



class Enemy(pygame.sprite.Sprite):
    def __init__(self,random_x,random_y,direction):
        pygame.sprite.Sprite.__init__(self)
        #设置怪物速度和方向
        self.speed = 4
        self.direction = direction
        #设置怪物初始位置
        self.rect.x = random_x
        self.rect.y = random_y

        self.image = pygame.image.load("assets/ENEMY.png")
        self.rect = self.image.get_rect()

    def update(self):
        if self.direction == "left":
            self.rect.x -= self.speed

        if self.direction == "right":
            self.rect.x += self.speed

        if self.direction == "up":
            self.rect_y += self.speed

        if self.direction == "down":
            self.rect_y -= self.speed

    #怪物移动方向改变
    def change_direction(self,direction):
        self.direction = direction
