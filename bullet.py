import pygame
import game_launcher


class Bullet(pygame.sprite.Sprite):

    #   @para
    #   coordinate_x the initial x coordinate of the bullet
    #   coordinate_y the initial y coordinate of the bullet
    #   direction   the moving direction of the bullet
    #
    def __init__(self, coordinate_x, coordinate_y, direction):
        pygame.sprite.Sprite.__init__(self)
        # 设置伤害
        self.damage = 1
        # 设置移速和方向
        self.speed = 10
        self.direction = direction

        img = pygame.image.load("assets/BULLET.png")
        self.image = pygame.transform.scale(img, (game_launcher.WIDTH_BULLET, game_launcher.HEIGHT_BULLET))
        self.rect = self.image.get_rect()

        # 设置位置
        self.rect.x = coordinate_x
        self.rect.y = coordinate_y

    def update(self):

        if self.direction == "left":
            self.rect.x -= self.speed

        if self.direction == "right":
            self.rect.x += self.speed

        if self.direction == "up":
            self.rect.y -= self.speed

        if self.direction == "down":
            self.rect.y += self.speed
