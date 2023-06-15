import pygame.sprite
# import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, random_x, random_y, _direction):
        pygame.sprite.Sprite.__init__(self)

        # 设置怪物速度和方向
        self.speed = 1
        self.direction = _direction

        img = pygame.image.load("assets/ENEMY.png")
        self.image = pygame.transform.scale(img, (50, 50))
        self.rect = self.image.get_rect()

        # 设置怪物初始位置
        self.rect.x = random_x
        self.rect.y = random_y

    def update(self):
        if self.direction == "left":
            self.rect.x -= self.speed

        if self.direction == "right":
            self.rect.x += self.speed

        if self.direction == "up":
            self.rect.y += self.speed

        if self.direction == "down":
            self.rect.y -= self.speed

    # 怪物移动方向改变
    def change_direction(self, _direction):
        self.direction = _direction
