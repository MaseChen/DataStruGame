import pygame.sprite


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.property1 = -1
        self.property2 = -1
        self.image = pygame.image.load("assets/ENEMY.png")
        self.rect = self.image.get_rect()
