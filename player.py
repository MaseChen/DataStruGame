import pygame.sprite


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.blood = 1000
        self.image = pygame.image.load("assets/PLAYER.png")
        self.rect = self.image.get_rect()

    def update(self):
        pass


def go_up_begin():
    return None


def go_down_begin():
    return None


def go_left_begin():
    return None


def go_right_begin():
    return None


def fire():
    return None


def go_up_end():
    return None


def go_down_end():
    return None


def go_left_end():
    return None


def go_right_end():
    return None

