import pygame
import sys
import os
import bullet
import time

import game_launcher


class Player(pygame.sprite.Sprite):  # 继承Sprite精灵类
    def __init__(self, _surface):
        pygame.sprite.Sprite.__init__(self)

        # Main Screen
        self.main_screen = _surface
        # 设置血条
        self.blood = game_launcher.BLOOD_PLAYER
        self.speed = 5
        self.shields = 0
        self.damage = 1
        self.time_damage = 0
        self.time_speed = 0
        self.time = 0
        self.last_moving_status = "right"
        # self.towards_status = "right"
        self.images = []  # 用来存储玩家对象精灵图片的列表
        img = pygame.image.load(os.path.join('assets', 'right' + str(1) + '.png')).convert()
        img = pygame.transform.scale(img, (game_launcher.WIDTH_PLAYER, game_launcher.HEIGHT_PLAYER))  # Resize image
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        # ALPHA = (0, 255, 0)
        # img.convert_alpha()  # 优化 alpha
        # img.set_colorkey(ALPHA)  # 设置 alpha
        # self.x = 400
        # self.y = 300
        # self.rect = self.image.get_rect()
        self.rect.x = 60
        self.rect.y = 400
        # self.image = None
        self.key_right_status = False
        self.key_left_status = False
        self.key_down_status = False
        self.key_up_status = False



    def update(self):
        # Times-up stuff
        self.time = time.time()
        if self.time - self.time_damage >= game_launcher.TIME_DAMAGE:
            self.damage_down()
        else:
            self.draw_damage_up_time_remain()

        if self.time - self.time_speed >= game_launcher.TIME_SPEED:
            self.speed_down()
        else:
            self.draw_speed_up_time_remain()
        # Moving stuff
        if self.rect.x < game_launcher.WIDTH - game_launcher.WIDTH_PLAYER:
            if self.key_right_status:
                self.rect.x += self.speed
        if self.rect.x > 0:
            if self.key_left_status:
                self.rect.x -= self.speed
        if self.rect.y < game_launcher.HEIGHT - game_launcher.HEIGHT_PLAYER:
            if self.key_down_status:
                self.rect.y += self.speed
        if self.rect.y > 0:
            if self.key_up_status:
                self.rect.y -= self.speed

        # Draw Player Blood
        self.draw_player_blood()
        self.draw_shield()

    def fire(self):
        return bullet.Bullet(self.rect.x + game_launcher.WIDTH_PLAYER / 2 - game_launcher.WIDTH_BULLET / 2,
                             self.rect.y + game_launcher.HEIGHT_PLAYER / 2 - game_launcher.HEIGHT_BULLET / 2,
                             self.last_moving_status, self.damage)

    def draw_shield(self):
        pygame.draw.rect(self.main_screen, "grey",
                         (game_launcher.POS_PLAYER_BLOOD_X, game_launcher.POS_PLAYER_BLOOD_Y - 15,
                          game_launcher.WIDTH_PLAYER_BLOOD, game_launcher.HEIGHT_PLAYER_BLOOD))
        pygame.draw.rect(self.main_screen, "blue",
                         (game_launcher.POS_PLAYER_BLOOD_X, game_launcher.POS_PLAYER_BLOOD_Y - 15,
                          game_launcher.WIDTH_PLAYER_BLOOD *
                          (self.shields / game_launcher.SHIELD_PLAYER),
                          game_launcher.HEIGHT_PLAYER_BLOOD))

    def draw_player_blood(self):
        pygame.draw.rect(self.main_screen, "grey", (game_launcher.POS_PLAYER_BLOOD_X, game_launcher.POS_PLAYER_BLOOD_Y,
                                                    game_launcher.WIDTH_PLAYER_BLOOD,
                                                    game_launcher.HEIGHT_PLAYER_BLOOD))
        pygame.draw.rect(self.main_screen, "red", (game_launcher.POS_PLAYER_BLOOD_X, game_launcher.POS_PLAYER_BLOOD_Y,
                                                   game_launcher.WIDTH_PLAYER_BLOOD *
                                                   (self.blood / game_launcher.BLOOD_PLAYER),
                                                   game_launcher.HEIGHT_PLAYER_BLOOD))

    def draw_speed_up_time_remain(self):
        pygame.draw.rect(self.main_screen, "green",
                         (game_launcher.POS_PLAYER_BLOOD_X + 100, game_launcher.POS_PLAYER_BLOOD_Y,
                          game_launcher.WIDTH_PLAYER_BLOOD * (1 -
                                                              (self.time - self.time_speed)
                                                              / game_launcher.TIME_SPEED),
                          game_launcher.HEIGHT_PLAYER_BLOOD))

    def draw_damage_up_time_remain(self):
        pygame.draw.rect(self.main_screen, "yellow",(game_launcher.POS_PLAYER_BLOOD_X + 200,
                                                      game_launcher.POS_PLAYER_BLOOD_Y,
                                                      game_launcher.WIDTH_PLAYER_BLOOD
                                                      * (1 - (self.time - self.time_damage)
                                                         / game_launcher.TIME_DAMAGE),
                                                      game_launcher.HEIGHT_PLAYER_BLOOD))

    # Power-Ups Interaction
    # Blood
    def add_blood(self):
        self.blood += 1
        if self.blood > 3:
            self.blood = 3

    def hurt(self, amount):
        if self.shields > 0:
            self.shields -= amount
        else:
            self.shields = 0
            self.blood -= amount
        if self.blood <= 0:
            sys.exit()

    # Shield
    def add_shields(self):
        self.shields = game_launcher.SHIELD_PLAYER

    # Damage
    def damage_up(self):
        self.damage = 5
        self.time_damage = time.time()

    def damage_down(self):
        self.damage = 1

    # Speed
    def speed_up(self):
        self.speed = 10
        self.time_speed = time.time()

    def speed_down(self):
        self.speed = 5

    #
    # Player Move
    def go_up_begin(self):
        self.key_up_status = True
        self.last_moving_status = "up"
        self.images = []  # 用来存储玩家对象精灵图片的列表
        img = pygame.image.load(os.path.join('assets', 'up' + str(1) + '.png')).convert()
        img = pygame.transform.scale(img, (game_launcher.WIDTH_PLAYER, game_launcher.HEIGHT_PLAYER))  # Resize image
        self.images.append(img)
        self.image = self.images[0]


    def go_down_begin(self):
        self.key_down_status = True
        self.last_moving_status = "down"
        self.images = []  # 用来存储玩家对象精灵图片的列表
        img = pygame.image.load(os.path.join('assets', 'down' + str(1) + '.png')).convert()
        img = pygame.transform.scale(img, (game_launcher.WIDTH_PLAYER, game_launcher.HEIGHT_PLAYER))  # Resize image
        self.images.append(img)
        self.image = self.images[0]


    def go_left_begin(self):
        self.key_left_status = True
        self.last_moving_status = "left"
        self.images = []  # 用来存储玩家对象精灵图片的列表
        img = pygame.image.load(os.path.join('assets', 'left' + str(1) + '.png')).convert()
        img = pygame.transform.scale(img, (game_launcher.WIDTH_PLAYER, game_launcher.HEIGHT_PLAYER))  # Resize image
        self.images.append(img)
        self.image = self.images[0]

    def go_right_begin(self):
        self.key_right_status = True
        self.last_moving_status = "right"
        self.images = []  # 用来存储玩家对象精灵图片的列表
        img = pygame.image.load(os.path.join('assets', 'right' + str(1) + '.png')).convert()
        img = pygame.transform.scale(img, (game_launcher.WIDTH_PLAYER, game_launcher.HEIGHT_PLAYER))  # Resize image
        self.images.append(img)
        self.image = self.images[0]

    def go_up_end(self):
        self.key_up_status = False

    def go_down_end(self):
        self.key_down_status = False

    def go_left_end(self):
        self.key_left_status = False

    def go_right_end(self):
        self.key_right_status = False
