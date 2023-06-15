import pygame
from random import randint, choice
from enum import Enum
from sys import exit

REC_SIZE = 10
REC_WIDTH = 75  # must be odd number
REC_HEIGHT = 71  # must be odd number
SCREEN_WIDTH = REC_WIDTH * REC_SIZE
SCREEN_HEIGHT = REC_HEIGHT * REC_SIZE


# 创建地图格子种类枚举类
class MAP_ENTRY_TYPE(Enum):
    MAP_EMPTY = 0,
    MAP_BLOCK = 1,
    MAP_TARGET = 2,
    MAP_PATH = 3,
    MAP_DONE = 4


# 创建一个格子方法枚举类
class WALL_DIRECTION(Enum):
    WALL_LEFT = 0,
    WALL_UP = 1,
    WALL_RIGHT = 2,
    WALL_DOWN = 3,


# 用字典存储格子枚举类型
map_entry_types = {0: MAP_ENTRY_TYPE.MAP_EMPTY, 1: MAP_ENTRY_TYPE.MAP_BLOCK,
                   2: MAP_ENTRY_TYPE.MAP_TARGET, 3: MAP_ENTRY_TYPE.MAP_PATH, 4: MAP_ENTRY_TYPE.MAP_DONE}

"""基础MAP类生成并控制格子"""


class Map:
    # 初始化地图长宽

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [[0 for x in range(self.width)] for y in range(self.height)]

    # 创建一定数量的墙壁
    def createBlock(self, block_num):
        for i in range(block_num):
            x, y = (randint(0, self.width - 1), randint(0, self.height - 1))
            self.map[y][x] = 1

    # 在范围内随机选找到路径
    def generatePos(self, rangeX, rangeY):
        x, y = (randint(rangeX[0], rangeX[1]), randint(rangeY[0], rangeY[1]))
        while self.map[y][x] == 1:
            x, y = (randint(rangeX[0], rangeX[1]), randint(rangeY[0], rangeY[1]))
        return x, y

    # 将整个地图重置为指定类型
    def resetMap(self, value):
        for y in range(self.height):
            for x in range(self.width):
                self.setMap(x, y, value)

    # 将一个格子设置为指定类型
    def setMap(self, x, y, value):
        if value == MAP_ENTRY_TYPE.MAP_EMPTY:
            self.map[y][x] = 0
        elif value == MAP_ENTRY_TYPE.MAP_BLOCK:
            self.map[y][x] = 1
        elif value == MAP_ENTRY_TYPE.MAP_TARGET:
            self.map[y][x] = 2
        elif value == MAP_ENTRY_TYPE.MAP_PATH:
            self.map[y][x] = 3
        else:
            self.map[y][x] = 4

    # 判断一个格子是否可以访问
    def isVisited(self, x, y):
        return self.map[y][x] != 1

    # 判断一个格子是否可移动
    def isMovable(self, x, y):
        return self.map[y][x] != 1

    # 判断格子是否在地图内
    def isValid(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        return True

    # 返回格子类型
    def getType(self, x, y):
        return map_entry_types[self.map[y][x]]


"""迷宫生成算法"""


# 找到四个相位中没有被遍历过的格子
# 随机遍历一个，将其放入遍历过的方格列表
def setMap(self, x, y, value):
    directions = []
    if x > 0:
        if not map.isVisited(2 * (x - 1) + 1, 2 * y + 1):
            directions.append(WALL_DIRECTION.WALL_LEFT)

    if y > 0:
        if not map.isVisited(2 * x + 1, 2 * (y - 1) + 1):
            directions.append(WALL_DIRECTION.WALL_UP)

    if x < width - 1:
        if not map.isVisited(2 * (x + 1) + 1, 2 * y + 1):
            directions.append(WALL_DIRECTION.WALL_RIGHT)

    if y < height - 1:
        if not map.isVisited(2 * x + 1, 2 * (y + 1) + 1):
            directions.append(WALL_DIRECTION.WALL_DOWN)

    if len(directions):
        direction = choice(directions)
        # print("(%d, %d) => %s" % (x, y, str(direction)))
        if direction == WALL_DIRECTION.WALL_LEFT:
            map.setMap(2 * (x - 1) + 1, 2 * y + 1, MAP_ENTRY_TYPE.MAP_EMPTY)
            map.setMap(2 * x, 2 * y + 1, MAP_ENTRY_TYPE.MAP_EMPTY)
            checklist.append((x - 1, y))
        elif direction == WALL_DIRECTION.WALL_UP:
            map.setMap(2 * x + 1, 2 * (y - 1) + 1, MAP_ENTRY_TYPE.MAP_EMPTY)
            map.setMap(2 * x + 1, 2 * y, MAP_ENTRY_TYPE.MAP_EMPTY)
            checklist.append((x, y - 1))
        elif direction == WALL_DIRECTION.WALL_RIGHT:
            map.setMap(2 * (x + 1) + 1, 2 * y + 1, MAP_ENTRY_TYPE.MAP_EMPTY)
            map.setMap(2 * x + 2, 2 * y + 1, MAP_ENTRY_TYPE.MAP_EMPTY)
            checklist.append((x + 1, y))
        elif direction == WALL_DIRECTION.WALL_DOWN:
            map.setMap(2 * x + 1, 2 * (y + 1) + 1, MAP_ENTRY_TYPE.MAP_EMPTY)
            map.setMap(2 * x + 1, 2 * y + 2, MAP_ENTRY_TYPE.MAP_EMPTY)
            checklist.append((x, y + 1))
        return True
    else:
        # 如果没有找到相邻的未遍历方格
        return False


# 递归回溯实现
def recursiveBacktracker(map, width, height):
    startX, startY = (randint(0, width - 1), randint(0, height - 1))
    print("start(%d, %d)" % (startX, startY))
    map.setMap(2 * startX + 1, 2 * startY + 1, MAP_ENTRY_TYPE.MAP_EMPTY)

    checklist = []
    checklist.append((startX, startY))
    while len(checklist):
        # 将检查列表用作堆栈，从栈顶获取元素
        entry = checklist[-1]
        if not checkAdjacentPos(map, entry[0], entry[1], width, height, checklist):
            # 格子四周没有可以未遍历的路径，则将这个格子从栈顶删除
            checklist.remove(entry)


# 迷宫生成
def doRecursiveBacktracker(map):
    # 将所以有格子设为墙壁
    map.resetMap(MAP_ENTRY_TYPE.MAP_BLOCK)
    # 用算法产生迷宫
    recursiveBacktracker(map, (map.width - 1) // 2, (map.height - 1) // 2)


"""A*自动寻路"""


class SearchEntry:
    def __init__(self, x, y, g_cost, f_cost=0, pre_entry=None):
        self.x = x
        self.y = y
        # 从起始点到当前点的步数
        self.g_cost = g_cost
        self.f_cost = f_cost
        self.pre_entry = pre_entry

    def getPos(self):
        return self.x, self.y


def AStarSearch(map, source, dest):
    # 检查指定格子一个方向的另外一个格子是否不是墙壁，不是则输出坐标
    def getNewPosition(map, location, offset):
        x, y = (location.x + offset[0], location.y + offset[1])
        if not map.isValid(x, y) or not map.isMovable(x, y):
            return None
        return x, y

    # 返回所有不是墙壁的格子坐标列表
    def getPositions(map, location):
        # 用四相或者八相移动
        offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        # offsets = [(-1,0), (0, -1), (1, 0), (0, 1), (-1,-1), (1, -1), (-1, 1), (1, 1)]
        poslist = []
        for offset in offsets:
            pos = getNewPosition(map, location, offset)
            if pos is not None:
                poslist.append(pos)
        return poslist

    # 返回指定点到终点的曼哈顿距离
    def calHeuristic(pos, dest):
        return abs(dest.x - pos[0]) + abs(dest.y - pos[1])

    # 根据是否是斜向移动来计算消耗
    def getMoveCost(location, pos):
        if location.x != pos[0] and location.y != pos[1]:
            return 1.4
        else:
            return 1

    # 检查这个点是否在指定列表里
    def isInList(list, pos):
        if pos in list:
            return list[pos]
        return None

    # 添加可遍历点
    def addAdjacentPositions(map, location, dest, openlist, closedlist):
        poslist = getPositions(map, location)
        for pos in poslist:
            # 在colsedlist列表里，则不做操作
            if isInList(closedlist, pos) is None:
                findEntry = isInList(openlist, pos)
                h_cost = calHeuristic(pos, dest)
                g_cost = location.g_cost + getMoveCost(location, pos)
                if findEntry is None:
                    # 不在open列表里，添加进去
                    openlist[pos] = SearchEntry(pos[0], pos[1], g_cost, g_cost + h_cost, location)
                elif findEntry.g_cost > g_cost:
                    # 如果在open列表里，且代价比目前计算的大
                    # 就更新这个点的代价
                    findEntry.g_cost = g_cost
                    findEntry.f_cost = g_cost + h_cost
                    findEntry.pre_entry = location

    # 找到open列表里代价最小的点来遍历，open列表为空则返回None
    def getFastPosition(openlist):
        fast = None
        for entry in openlist.values():
            if fast is None:
                fast = entry
            elif fast.f_cost > entry.f_cost:
                fast = entry
        return fast

    openlist = {}
    closedlist = {}
    location = SearchEntry(source[0], source[1], 0.0)
    dest = SearchEntry(dest[0], dest[1], 0.0)
    openlist[source] = location
    while True:
        location = getFastPosition(openlist)
        if location is None:
            # 没找到路径
            print("can't find valid path")
            break

        if location.x == dest.x and location.y == dest.y:
            break

        closedlist[location.getPos()] = location
        openlist.pop(location.getPos())
        addAdjacentPositions(map, location, dest, openlist, closedlist)

    # 标记找到的路径
    # while location is not None:
    #     map.setMap(location.x, location.y, MAP_ENTRY_TYPE.MAP_PATH)
    #     location = location.pre_entry


"""GUI"""


class Game:

    def __init__(self):
        self.map = Map(REC_WIDTH, REC_HEIGHT)
        self.mode = 0
        self.source_x, self.source_y = self.map.generatePos((1, 1), (1, self.map.height - 2))

    def creat_maze(self):
        doRecursiveBacktracker(self.map)

        self.dest = self.map.generatePos((self.map.width - 2, self.map.width - 2), (1, self.map.height - 2))
        self.map.setMap(self.source_x, self.source_y, MAP_ENTRY_TYPE.MAP_TARGET)
        self.map.setMap(self.dest[0], self.dest[1], MAP_ENTRY_TYPE.MAP_TARGET)

    def creat_source(self):
        self.source_x, self.source_y = self.map.generatePos((1, 1), (1, self.map.height - 2))

    def path_find(self, origin):
        AStarSearch(self.map, origin, self.dest)
        self.map.setMap(origin[0], origin[1], MAP_ENTRY_TYPE.MAP_TARGET)
        self.map.setMap(self.dest[0], self.dest[1], MAP_ENTRY_TYPE.MAP_TARGET)

    def clear_maze(self):
        self.map.resetMap(MAP_ENTRY_TYPE.MAP_EMPTY)


# 键盘控制
def key_control(game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            exit()
            pass
        elif event.type == pygame.KEYDOWN:
            # 向上移动
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                if game.map.isVisited(game.source_x, game.source_y - 1):
                    if game.map.map[game.source_y - 1][game.source_x] == 4:
                        game.map.setMap(game.source_x, game.source_y, MAP_ENTRY_TYPE.MAP_EMPTY)
                        game.source_y -= 1
                        game.map.setMap(game.source_x, game.source_y, MAP_ENTRY_TYPE.MAP_TARGET)
                    else:
                        game.map.setMap(game.source_x, game.source_y, MAP_ENTRY_TYPE.MAP_DONE)
                        game.source_y -= 1
                        game.map.setMap(game.source_x, game.source_y, MAP_ENTRY_TYPE.MAP_TARGET)
            # 向下移动
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if game.map.isVisited(game.source_x, game.source_y + 1):
                    if game.map.map[game.source_y + 1][game.source_x] == 4:
                        game.map.setMap(game.source_x, game.source_y, MAP_ENTRY_TYPE.MAP_EMPTY)
                        game.source_y += 1
                        game.map.setMap(game.source_x, game.source_y, MAP_ENTRY_TYPE.MAP_TARGET)
                    else:
                        game.map.setMap(game.source_x, game.source_y, MAP_ENTRY_TYPE.MAP_DONE)
                        game.source_y += 1
                        game.map.setMap(game.source_x, game.source_y, MAP_ENTRY_TYPE.MAP_TARGET)
            # 向左移动
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if game.map.isVisited(game.source_x - 1, game.source_y):
                    if game.map.map[game.source_y][game.source_x - 1] == 4:
                        game.map.setMap(game.source_x, game.source_y, MAP_ENTRY_TYPE.MAP_EMPTY)
                        game.source_x -= 1
                        game.map.setMap(game.source_x, game.source_y, MAP_ENTRY_TYPE.MAP_TARGET)
                    else:
                        game.map.setMap(game.source_x, game.source_y, MAP_ENTRY_TYPE.MAP_DONE)
                        game.source_x -= 1
                        game.map.setMap(game.source_x, game.source_y, MAP_ENTRY_TYPE.MAP_TARGET)
            # 向右移动
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if game.map.isVisited(game.source_x + 1, game.source_y):
                    if game.map.map[game.source_y][game.source_x + 1] == 4:
                        game.map.setMap(game.source_x, game.source_y, MAP_ENTRY_TYPE.MAP_EMPTY)
                        game.source_x += 1
                        game.map.setMap(game.source_x, game.source_y, MAP_ENTRY_TYPE.MAP_TARGET)
                    else:
                        game.map.setMap(game.source_x, game.source_y, MAP_ENTRY_TYPE.MAP_DONE)
                        game.source_x += 1
                        game.map.setMap(game.source_x, game.source_y, MAP_ENTRY_TYPE.MAP_TARGET)

            elif event.key == pygame.K_SPACE:
                game.clear_maze()
                game.creat_source()
                game.creat_maze()
            elif event.key == pygame.K_ESCAPE:
                game.path_find((game.source_x, game.source_y))

#
# # 主游戏循环
# def main():
#     pygame.init()
#     game = Game()
#
#     screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
#     game.creat_maze()
#     while True:
#         pygame.time.Clock().tick(30)
#         pygame.display.update()
#         key_control(game)
#
#         for y in range(game.map.height):
#             for x in range(game.map.width):
#                 type = game.map.getType(x, y)
#                 if type == MAP_ENTRY_TYPE.MAP_EMPTY:
#                     color = (255, 255, 255)
#                 elif type == MAP_ENTRY_TYPE.MAP_BLOCK:
#                     color = (0, 0, 0)
#                 elif type == MAP_ENTRY_TYPE.MAP_TARGET:
#                     color = (255, 0, 0)
#                 elif type == MAP_ENTRY_TYPE.MAP_PATH:
#                     color = (0, 255, 0)
#                 else:
#                     color = (0, 0, 255)
#
#                 pygame.draw.rect(screen, color,
#                                  pygame.Rect(REC_SIZE * x, REC_SIZE * y, REC_SIZE, REC_SIZE))
#
#
# if __name__ == '__main__':  # 固定搭配
#     main()