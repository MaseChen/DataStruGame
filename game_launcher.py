import pygame
import sys

import player
import map
import bullet
import enemy
import props


class GameLauncher:
    def __init__(self) -> None:
        # --------------------------------------------------------------------
        # 初始化窗口、载入素材
        pygame.init()
        pygame.display.set_caption("tomb_raider")
        self.screen = pygame.display.set_mode((800, 600))

        # TODO 载入素材

        # --------------------------------------------------------------------
        # 实例化精灵列表和组件（各个游戏元素）
        self.player = player.Player()
        self.map = map.Map()

        self.bulletGroup = pygame.sprite.Group()
        self.enemyGroup = pygame.sprite.Group()
        self.propsGroup = pygame.sprite.Group()

        # 游戏时钟
        self.clock = pygame.time.Clock()

    # 游戏运行函数
    def launch(self):
        while True:
            # ----------------------------------------------------------------
            # 事件监测

            for event in pygame.event.get():
                # 关闭窗口
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    # SPACE、W、方向上键
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        player.go_up_begin()

                    # 按下S、方向下键
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        player.go_down_begin()

                    # 按下A、方向左键
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        player.go_left_begin()

                    # 按下D、方向右键
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        player.go_right_begin()

                    if event.key == pygame.K_SPACE:
                        player.fire()

                if event.type == pygame.KEYUP:
                    # SPACE、W、方向上键
                    if (
                        event.key == pygame.K_SPACE
                        or event.key == pygame.K_w
                        or event.key == pygame.K_UP
                    ):
                        player.go_up_end()

                    # 松开S、方向下键
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        player.go_down_end()

                    # 按下A、方向左键
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        player.go_left_end()

                    # 按下D、方向右键
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        player.go_right_end()

            # ----------------------------------------------------------------
            # 画背景
            # assert self.dinosour.image is not None and self.dinosour.rect is not None

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
            self.generateEnemy()
            self.generateProps()

            # 画子弹
            self.bulletGroup.draw(self.screen)

            # 画敌人
            self.enemyGroup.draw(self.screen)

            # 画道具
            self.propsGroup.draw(self.screen)

            # 画玩家
            self.screen.blit(self.player.image, self.dinosour.rect)

            # 检测互动

            self.checkPlayer_Enemy()
            self.checkPlayer_Props()
            self.checkBullet_Enemy()

            # ----------------------------------------------------------------
            # 更新组件的状态
            self.bulletGroup.update()
            self.enemyGroup.update()
            self.propsGroup.update()

            self.player.update()

            # ----------------------------------------------------------------
            # 更新窗口、设置帧率
            pygame.display.update()
            self.clock.tick(60)

    # ------------------------------------------------------------------------
    # ------------------------------------------------------------------------
    # 功能函数

    def generateEnemy(self):
        pass

    def generateProps(self):
        pass

    def checkPlayer_Enemy():
        pass
    def checkPlayer_Props():
        pass
    def checkBullet_Enemy():
        pass

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
    #             self.dinosour, self.obstacleGroup, pygame.sprite.collide_mask
    #         )
    #         is not None
    #     ):  # type: ignore
    #         self.dinosour.life = False
