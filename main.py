import pygame
import map

REC_SIZE = 20
REC_WIDTH = 60
REC_HEIGHT = 35
SCREEN_WIDTH = REC_WIDTH * REC_SIZE
SCREEN_HEIGHT = REC_HEIGHT * REC_SIZE


class Game_Launcher:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Test Run 2")

        self.map = map.Map(REC_WIDTH, REC_HEIGHT)
        self.map.generateMap()

    def launch(self):
        run = True
        while run:
            self.screen.fill(color=(23, 145, 87))
            self.draw_map()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.flip()
        pygame.quit()

    def draw_map(self):
        for y in range(self.map.height):
            for x in range(self.map.width):
                node_type = self.map.get_type(x, y)
                if node_type == 0:
                    color = (255, 255, 255)
                elif node_type == 1:
                    color = (0, 0, 0)
                elif node_type == 2:
                    color = (255, 0, 0)
                elif node_type == 3:
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


my_game = Game_Launcher()
my_game.launch()
