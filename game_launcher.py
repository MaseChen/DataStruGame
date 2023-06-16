import pygame
import map
import sys
import player

REC_SIZE = 10
REC_WIDTH = 31  # must be odd number
REC_HEIGHT = 31  # must be odd number
SCREEN_WIDTH = REC_WIDTH * REC_SIZE
SCREEN_HEIGHT = REC_HEIGHT * REC_SIZE

WIDTH_BASIC = 10
HEIGHT_BASIC = 10

WIDTH_PLAYER = WIDTH_BASIC
HEIGHT_PLAYER = HEIGHT_BASIC

BLOOD_PLAYER = 3

TIME_DAMAGE = 5
TIME_SPEED = 5

POS_PLAYER_BLOOD_X = 90
POS_PLAYER_BLOOD_Y = SCREEN_HEIGHT - 60
WIDTH_PLAYER_BLOOD = 90
HEIGHT_PLAYER_BLOOD = 10

SHIELD_PLAYER = 1


class GameLauncher:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tomb Raider Game")
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

        self.maze = map.Maze(self.screen)
        self.maze.creat_maze()
        self.player = player.Player(self.screen)

        self.enemyGroup = pygame.sprite.Group()
        self.bulletGroup = pygame.sprite.Group()
        self.powerUpsGroup = pygame.sprite.Group()

        self.clock = pygame.time.Clock()

    def launch(self):
        while True:
            self.key_control(self.maze)

            for y in range(self.maze.map.height):
                for x in range(self.maze.map.width):
                    type = self.maze.map.getType(x, y)
                    if type == map.MAP_ENTRY_TYPE.MAP_EMPTY:
                        color = (255, 255, 255)
                    elif type == map.MAP_ENTRY_TYPE.MAP_BLOCK:
                        color = (0, 0, 0)
                    elif type == map.MAP_ENTRY_TYPE.MAP_TARGET:
                        color = (255, 0, 0)
                    elif type == map.MAP_ENTRY_TYPE.MAP_PATH:
                        color = (0, 255, 0)
                    else:
                        color = (0, 0, 255)

                    pygame.draw.rect(
                        self.screen,
                        color,
                        pygame.Rect(
                            REC_SIZE * x,
                            REC_SIZE * y,
                            REC_SIZE,
                            REC_SIZE,
                        ),
                    )

            # 生成随机数量的敌人
            # self.generate_enemy()
            # self.generate_power_ups()

            # 画子弹
            self.bulletGroup.draw(self.screen)

            # 画敌人
            self.enemyGroup.draw(self.screen)

            # 画道具
            self.powerUpsGroup.draw(self.screen)

            # 画玩家
            self.screen.blit(self.player.image, self.player.rect)

            # 检测互动

            # self.check_player_enemy()
            # self.check_player_power_ups()
            # self.check_bullet_enemy()

            # TODO 检测子弹和墙的碰撞

            # ----------------------------------------------------------------
            # 更新组件的状态
            self.bulletGroup.update()
            self.enemyGroup.update()
            self.powerUpsGroup.update()

            self.player.update()

            pygame.display.update()
            self.clock.tick(30)

    # 键盘控制
    def key_control(self, maze):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # 向上移动
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.player.go_up_begin()

                    # if maze.map.isVisited(maze.source_x, maze.source_y - 1):
                    #     if maze.map.map[maze.source_y - 1][maze.source_x] == 4:
                    #         maze.map.setMap(
                    #             maze.source_x,
                    #             maze.source_y,
                    #             map.MAP_ENTRY_TYPE.MAP_EMPTY,
                    #         )
                    #         maze.source_y -= 1
                    #         maze.map.setMap(
                    #             maze.source_x,
                    #             maze.source_y,
                    #             map.MAP_ENTRY_TYPE.MAP_TARGET,
                    #         )
                    #     else:
                    #         maze.map.setMap(
                    #             maze.source_x,
                    #             maze.source_y,
                    #             map.MAP_ENTRY_TYPE.MAP_DONE,
                    #         )
                    #         maze.source_y -= 1
                    #         maze.map.setMap(
                    #             maze.source_x,
                    #             maze.source_y,
                    #             map.MAP_ENTRY_TYPE.MAP_TARGET,
                    #         )
                # 向下移动
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.player.go_down_begin()

                    # if maze.map.isVisited(maze.source_x, maze.source_y + 1):
                    #     if maze.map.map[maze.source_y + 1][maze.source_x] == 4:
                    #         maze.map.setMap(
                    #             maze.source_x,
                    #             maze.source_y,
                    #             map.MAP_ENTRY_TYPE.MAP_EMPTY,
                    #         )
                    #         maze.source_y += 1
                    #         maze.map.setMap(
                    #             maze.source_x,
                    #             maze.source_y,
                    #             map.MAP_ENTRY_TYPE.MAP_TARGET,
                    #         )
                    #     else:
                    #         maze.map.setMap(
                    #             maze.source_x,
                    #             maze.source_y,
                    #             map.MAP_ENTRY_TYPE.MAP_DONE,
                    #         )
                    #         maze.source_y += 1
                    #         maze.map.setMap(
                    #             maze.source_x,
                    #             maze.source_y,
                    #             map.MAP_ENTRY_TYPE.MAP_TARGET,
                    #         )
                # 向左移动
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.player.go_left_begin()

                    # if maze.map.isVisited(maze.source_x - 1, maze.source_y):
                    #     if maze.map.map[maze.source_y][maze.source_x - 1] == 4:
                    #         maze.map.setMap(
                    #             maze.source_x,
                    #             maze.source_y,
                    #             map.MAP_ENTRY_TYPE.MAP_EMPTY,
                    #         )
                    #         maze.source_x -= 1
                    #         maze.map.setMap(
                    #             maze.source_x,
                    #             maze.source_y,
                    #             map.MAP_ENTRY_TYPE.MAP_TARGET,
                    #         )
                    #     else:
                    #         maze.map.setMap(
                    #             maze.source_x,
                    #             maze.source_y,
                    #             map.MAP_ENTRY_TYPE.MAP_DONE,
                    #         )
                    #         maze.source_x -= 1
                    #         maze.map.setMap(
                    #             maze.source_x,
                    #             maze.source_y,
                    #             map.MAP_ENTRY_TYPE.MAP_TARGET,
                    #         )
                # 向右移动
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.player.go_right_begin()

                    # if maze.map.isVisited(maze.source_x + 1, maze.source_y):
                    #     if maze.map.map[maze.source_y][maze.source_x + 1] == 4:
                    #         maze.map.setMap(
                    #             maze.source_x,
                    #             maze.source_y,
                    #             map.MAP_ENTRY_TYPE.MAP_EMPTY,
                    #         )
                    #         maze.source_x += 1
                    #         maze.map.setMap(
                    #             maze.source_x,
                    #             maze.source_y,
                    #             map.MAP_ENTRY_TYPE.MAP_TARGET,
                    #         )
                    #     else:
                    #         maze.map.setMap(
                    #             maze.source_x,
                    #             maze.source_y,
                    #             map.MAP_ENTRY_TYPE.MAP_DONE,
                    #         )
                    #         maze.source_x += 1
                    #         maze.map.setMap(
                    #             maze.source_x,
                    #             maze.source_y,
                    #             map.MAP_ENTRY_TYPE.MAP_TARGET,
                    #         )

                elif event.key == pygame.K_SPACE:
                    self.bulletGroup.add(self.player.fire())

                    # maze.clear_maze()
                    # maze.creat_source()
                    # maze.creat_maze()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYUP:
                # SPACE、W、方向上键
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.player.go_up_end()

                    # 松开S、方向下键
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.player.go_down_end()

                    # 按下A、方向左键
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.player.go_left_end()

                    # 按下D、方向右键
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.player.go_right_end()
