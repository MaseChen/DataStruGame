# import sys

import pygame

import enemy
import map
import player
import power_ups

WIDTH = 800
HEIGHT = 600


class GameLauncher:
    def __init__(self) -> None:
        # --------------------------------------------------------------------
        # 初始化窗口、载入素材
        pygame.init()
        pygame.display.set_caption("Tomb_Raider")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        # TODO 载入素材

        # --------------------------------------------------------------------
        # 实例化精灵列表和组件（各个游戏元素）
        self.player = player.Player()
        self.map = map.Map(WIDTH, HEIGHT)

        self.enemyGroup = pygame.sprite.Group()
        self.bulletGroup = pygame.sprite.Group()
        self.powerUpsGroup = pygame.sprite.Group()

        # 游戏时钟
        self.clock = pygame.time.Clock()

    # 游戏运行函数
    def launch(self):
        while True:
            # ----------------------------------------------------------------
            # 事件监测
            self.player.key_control()

            # ----------------------------------------------------------------
            # 画背景
            # assert self.dinosaur.image is not None and self.dinosaur.rect is not None

            # 背景颜色
            self.screen.fill("black")

            # TODO 画地图

            # 背景图片
            # self.screen.blit(self.background.track1.image, self.background.track1.rect)
            # self.screen.blit(self.background.track2.image, self.background.track2.rect)

            # ----------------------------------------------------------------
            # 游戏的核心内容

            # 画东西

            # 生成随机数量的敌人
            self.generate_enemy()
            self.generate_power_ups()

            # 画子弹
            self.bulletGroup.draw(self.screen)

            # 画敌人
            self.enemyGroup.draw(self.screen)

            # 画道具
            self.powerUpsGroup.draw(self.screen)

            # 画玩家
            self.screen.blit(self.player.image, self.player.rect)

            # 检测互动

            self.check_player_enemy()
            self.check_player_power_ups()
            self.check_bullet_enemy()

            # TODO 检测子弹和墙的碰撞

            # ----------------------------------------------------------------
            # 更新组件的状态
            self.bulletGroup.update()
            self.enemyGroup.update()
            self.powerUpsGroup.update()

            self.player.update()

            # ----------------------------------------------------------------
            # 更新窗口、设置帧率
            pygame.display.update()
            self.clock.tick(60)

    # ------------------------------------------------------------------------
    # ------------------------------------------------------------------------
    # 功能函数

    # 敌人人数不足5个时生成敌人
    def generate_enemy(self):
        if len(self.enemyGroup.sprites()) < 5:
            self.enemyGroup.add(enemy.Enemy(60, 80, "right"))

    # 道具数量不足3个时生成道具
    def generate_power_ups(self):
        if len(self.powerUpsGroup.sprites()) < 3:
            self.powerUpsGroup.add(power_ups.Power_Ups(100, 200, 0))

    # 玩家碰撞敌人时扣血
    def check_player_enemy(self):
        if (
                pygame.sprite.spritecollideany(
                    self.player, self.enemyGroup, collided=pygame.sprite.collide_rect
                )
                is not None
        ):
            self.player.blood = self.player.blood - 1

    # 玩家碰撞道具时道具生效
    def check_player_power_ups(self):
        gets_hit = pygame.sprite.spritecollideany(
            self.player, self.powerUpsGroup, collided=pygame.sprite.collide_rect
        )
        if gets_hit is not None:
            player.status = gets_hit.status
            self.powerUpsGroup.remove(gets_hit)
            # TODO 道具的实现需要更多信息

    # 子弹碰撞敌人时敌人扣血
    def check_bullet_enemy(self):
        bullet_list = self.bulletGroup.sprites()
        list_size = len(bullet_list)
        enemy_list = self.enemyGroup.sprites()
        for i in range(list_size):
            hit_list = pygame.sprite.spritecollide(
                bullet_list[i],
                self.enemyGroup,
                dokill=False,
                collided=pygame.sprite.collide_rect,
            )


            # for gets_hit in hit_list:
            #     if gets_hit in self.bulletGroup:
            #         self.bulletGroup.remove()
            #
            #     elif gets_hit in self.enemyGroup:
            #         gets_hit.blood -= 1

    # 通过规则随机确定下一个障碍物的种类并实例化此障碍物
    # def randObstacleKind(self):
    #     temp = random.random()

    #     if temp < para.Para.PROBABILITY_OF_BIRD:
    #         self.obstacleGroup.add(obstacle.Bird(self.speed))
    #     elif temp < 1 - ((1 - para.Para.PROBABILITY_OF_BIRD) / 2):
    #         self.obstacleGroup.add(obstacle.LargeCactus(self.speed))
    #     else:
    #         self.obstacleGroup.add(obstacle.SmallCactus(self.speed))

    # 删除已超出屏幕外的障碍物
    # def deleteObstacle(self):
    #     for item in self.obstacleGroup.sprites():
    #         assert item.image is not None and item.rect is not None

    #         if -item.rect.x > item.rect.width:
    #             self.obstacleGroup.remove(item)

    # 若检测到恐龙与障碍物碰撞，则判定恐龙死亡
    # def checkCollision(self):
    #     if (
    #         pygame.sprite.spritecollideany(
    #             self.dinosaur, self.obstacleGroup, pygame.sprite.collide_mask
    #         )
    #         is not None
    #     ):  # type: ignore
    #         self.dinosaur.life = False
