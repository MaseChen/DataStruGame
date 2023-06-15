import pygame.sprite


class Power_Ups(pygame.sprite.Sprite):
    def __init__(self, _x, _y, _kind: int):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = _x
        self.pos_y = _y
        self.kind = _kind
        # Create different view according to kind.
        self.image = pygame.surface.Surface((5, 5))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
