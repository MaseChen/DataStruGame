import pygame.sprite


class Enemy(pygame.sprite.Sprite):


    def __init__(self, _x, _y, _direction):
        """Create Enemy

        :param _x: initial x coordinate
        :param _y: initial y coordinate
        :return: nothing
        """
        pygame.sprite.Sprite.__init__(self)

        # 设置怪物速度和方向
        self.speed = 1
        self.direction = _direction

        img = pygame.image.load("assets/ENEMY.png")
        self.image = pygame.transform.scale(img, (50, 50))
        self.rect = self.image.get_rect()

        # 设置怪物初始位置
        self.rect.x = _x
        self.rect.y = _y

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
        """Change moving direction to something else

        :param _direction: the direction you want it to change to, can be left, right, up, or down"""
        self.direction = _direction

    def reverse_direction(self):
        if self.direction == "up":
            self.direction = "down"
        elif self.direction == "down":
            self.direction = "up"
        elif self.direction == "left":
            self.direction = "right"
        elif self.direction == "right":
            self.direction = "left"
        else:
            print("ERROR! Reverse direction error.")
