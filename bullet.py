import pygame

class Bullet:
    def __init__(self,coordinate_x,coordinate_y,direction):
        #设置伤害
        self.damage = 1
        #设置移速和方向
        self.speed = 1
        self.direction = direction
        #设置位置
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y

        self.image = pygame.image.load("assets/BULLET.png")
        self.rect = self.image.get_rect()

    def update(self):
        pass