import pygame.sprite
import game_launcher

class Power_Ups(pygame.sprite.Sprite):
    def __init__(self, _x, _y, _kind: int):
        pygame.sprite.Sprite.__init__(self)

        self.kind = _kind
        # Create different view according to kind.
        self.image = pygame.surface.Surface((20, 20))
        if self.kind == 0:
            self.image.fill("red")
        elif self.kind == 1:
            self.image.fill("blue")
        elif self.kind == 2:
            self.image.fill("yellow")
        elif self.kind == 3:
            self.image.fill("green")
        self.rect = self.image.get_rect()
        self.rect.x = _x
        self.rect.y = _y
