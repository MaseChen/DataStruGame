import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self,coordinate_x,coordinate_y,direction):
        pygame.sprite.Sprite.__init__(self)
        #设置伤害
        self.damage = 1
        #设置移速和方向
        self.speed = 5
        self.direction = direction
        #设置位置
        self.rect.x = coordinate_x
        self.rect_y = coordinate_y

        self.image = pygame.image.load("assets/BULLET.png")
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