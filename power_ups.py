import pygame.sprite

class Power_Ups(pygame.sprite.Sprite):
    def __init__(self, _x, _y, _kind: int):
        pygame.sprite.Sprite.__init__(self)

        self.kind = _kind
        # Create different view according to kind.
        self.image = pygame.surface.Surface((20, 20))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = _x
        self.rect.y = _y
