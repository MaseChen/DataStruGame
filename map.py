from random import randint
from enum import Enum
import game_launcher

class MAP_ENTRY_TYPE(Enum):
    """The type of the node in the map.

    MAP_EMPTY

    MAP_BLOCK

    MAP_TARGET

    MAP_PATH

    MAP_DONE"""
    MAP_EMPTY = (0,)
    MAP_BLOCK = (1,)
    MAP_TARGET = (2,)
    MAP_PATH = (3,)
    MAP_DONE = 4


class Map:
    width: int
    height: int
    map: [int]

    def __init__(self, width, height, default_type=1):
        self.width = width
        self.height = height
        self.map = [[default_type for _ in range(self.width)] for _ in range(self.height)]


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

    def resetMap(self, value):
        for y in range(self.height):
            for x in range(self.width):
                self.setMap(x, y, value)

    def get_type(self, x, y):
        return self.map[y][x]

    def is_valid(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        return True

    def is_edge(self, x, y):
        if x == 0 or y == 0 or x == self.width - 1 or y == self.height - 1:
            return True
        else:
            return False

    def is_block(self, x, y):
        if self.is_valid(x, y) and self.map[y][x] == 1:
            return True
        else:
            return False

    def generateMap(self):
        self.resetMap(MAP_ENTRY_TYPE.MAP_BLOCK)
        self.generate_map_with_all_blocks()

    def generate_map_with_all_blocks(self):
        startX, startY = (randint(2, self.width - 3), randint(2, self.height - 3))
        start_direction = randint(0, 3)

        drawing_man = DrawingMan(startX, startY, start_direction, self)
        drawing_man.paint()

        route_list = [(drawing_man.x, drawing_man.y, drawing_man.direction)]
        while len(route_list) > 0:
            while drawing_man.try_move(route_list):
                pass

            # Roll back configuration
            if len(route_list) > 5:
                for i in range(randint(2, 5)):
                    route_list.pop()
            elif len(route_list) > 1:
                for i in range(randint(2, len(route_list))):
                    route_list.pop()
            else:
                route_list.pop()

            if len(route_list):
                drawing_man.go_to(route_list[-1][0], route_list[-1][1], route_list[-1][2])

        print(self.map)  # can be deleted soon


class DrawingMan:
    def __init__(self, pos_x, pos_y, direction, map_where_the_drawing_man_is_in: Map):
        self.x = pos_x
        self.y = pos_y
        self.direction = direction

        self.map_parent = map_where_the_drawing_man_is_in
        self.force_forward = 0

    def forward(self):
        if self.direction == 0:
            self.y -= 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y += 1
        elif self.direction == 3:
            self.x -= 1

    def forward_by_steps(self, steps: int):
        if self.direction == 0:
            self.y -= steps
        elif self.direction == 1:
            self.x += steps
        elif self.direction == 2:
            self.y += steps
        elif self.direction == 3:
            self.x -= steps

    def backward(self):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 1:
            self.x -= 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 3:
            self.x += 1

    def backward_by_steps(self, steps: int):
        if self.direction == 0:
            self.y += steps
        elif self.direction == 1:
            self.x -= steps
        elif self.direction == 2:
            self.y -= steps
        elif self.direction == 3:
            self.x += steps

    def left(self):
        if self.direction == 0:
            self.x -= 1
        elif self.direction == 1:
            self.y -= 1
        elif self.direction == 2:
            self.x += 1
        elif self.direction == 3:
            self.y += 1

    def left_by_steps(self, steps: int):
        if self.direction == 0:
            self.x -= steps
        elif self.direction == 1:
            self.y -= steps
        elif self.direction == 2:
            self.x += steps
        elif self.direction == 3:
            self.y += steps

    def right(self):
        if self.direction == 0:
            self.x += 1
        elif self.direction == 1:
            self.y += 1
        elif self.direction == 2:
            self.x -= 1
        elif self.direction == 3:
            self.y -= 1

    def right_by_steps(self, steps: int):
        if self.direction == 0:
            self.x += steps
        elif self.direction == 1:
            self.y += steps
        elif self.direction == 2:
            self.x -= steps
        elif self.direction == 3:
            self.y -= steps

    def turn_left(self):
        if self.direction == 0:
            self.direction = 3
        elif self.direction == 1:
            self.direction = 0
        elif self.direction == 2:
            self.direction = 1
        elif self.direction == 3:
            self.direction = 2

    def turn_right(self):
        if self.direction == 0:
            self.direction = 1
        elif self.direction == 1:
            self.direction = 2
        elif self.direction == 2:
            self.direction = 3
        elif self.direction == 3:
            self.direction = 0

    def turn_around(self):
        if self.direction == 0:
            self.direction = 2
        elif self.direction == 1:
            self.direction = 3
        elif self.direction == 2:
            self.direction = 0
        elif self.direction == 3:
            self.direction = 1

    def move_by_relative_coordinate(self, relative_x: int, relative_y: int):
        if self.direction == 0:
            self.x += relative_x
            self.y += relative_y
        elif self.direction == 1:
            self.y += relative_x
            self.x -= relative_y
        elif self.direction == 2:
            self.x -= relative_x
            self.y -= relative_y
        elif self.direction == 3:
            self.x += relative_y
            self.y -= relative_x

    def go_to(self, cor_x: int, cor_y: int, direction: int) -> None:
        self.x = cor_x
        self.y = cor_y
        self.direction = direction

    def paint(self):
        self.map_parent.setMap(self.x, self.y, MAP_ENTRY_TYPE.MAP_EMPTY)
        self.backward()
        self.map_parent.setMap(self.x, self.y, MAP_ENTRY_TYPE.MAP_EMPTY)
        self.left()
        self.map_parent.setMap(self.x, self.y, MAP_ENTRY_TYPE.MAP_EMPTY)
        self.forward()
        self.map_parent.setMap(self.x, self.y, MAP_ENTRY_TYPE.MAP_EMPTY)
        self.forward()
        self.map_parent.setMap(self.x, self.y, MAP_ENTRY_TYPE.MAP_EMPTY)
        self.right()
        self.map_parent.setMap(self.x, self.y, MAP_ENTRY_TYPE.MAP_EMPTY)
        self.right()
        self.map_parent.setMap(self.x, self.y, MAP_ENTRY_TYPE.MAP_EMPTY)
        self.backward()
        self.map_parent.setMap(self.x, self.y, MAP_ENTRY_TYPE.MAP_EMPTY)
        self.backward()
        self.map_parent.setMap(self.x, self.y, MAP_ENTRY_TYPE.MAP_EMPTY)
        self.left()
        self.forward()

    def can_move_forward_and_paint(self) -> bool:
        original_x = self.x
        original_y = self.y
        return_bool = False

        self.left_by_steps(2)
        self.forward_by_steps(2)
        if self.map_parent.is_block(self.x, self.y):
            self.right_by_steps(4)
            if self.map_parent.is_block(self.x, self.y):
                self.left_by_steps(2)
                if not self.map_parent.is_edge(self.x, self.y):
                    return_bool = True

        self.go_to(original_x, original_y, self.direction)
        return return_bool

    def move_forward_and_paint(self):
        self.forward()
        self.paint()

    def can_turn_right_move_and_paint(self) -> bool:
        original_x = self.x
        original_y = self.y
        return_bool = False

        self.right_by_steps(2)
        self.forward_by_steps(2)
        if self.map_parent.is_block(self.x, self.y):
            self.backward_by_steps(4)
            if self.map_parent.is_block(self.x, self.y):
                self.forward_by_steps(2)
                if not self.map_parent.is_edge(self.x, self.y):
                    return_bool = True

        self.go_to(original_x, original_y, self.direction)
        return return_bool

    def turn_right_move_and_paint(self):
        self.turn_right()
        self.forward()
        self.paint()

        self.force_forward = 2

    def can_turn_left_move_and_paint(self) -> bool:
        original_x = self.x
        original_y = self.y
        return_bool = False

        self.left_by_steps(2)
        self.forward_by_steps(2)
        if self.map_parent.is_block(self.x, self.y):
            self.backward_by_steps(4)
            if self.map_parent.is_block(self.x, self.y):
                self.forward_by_steps(2)
                if not self.map_parent.is_edge(self.x, self.y):
                    return_bool = True

        self.go_to(original_x, original_y, self.direction)
        return return_bool

    def turn_left_move_and_paint(self):
        self.turn_left()
        self.forward()
        self.paint()

        self.force_forward = 2

    def can_turn_around_forward_and_paint(self):
        original_x = self.x
        original_y = self.y
        return_bool = False

        self.backward_by_steps(2)
        self.left_by_steps(2)
        if self.map_parent.is_block(self.x, self.y):
            self.right_by_steps(4)
            if self.map_parent.is_block(self.x, self.y):
                return_bool = True

        self.go_to(original_x, original_y, self.direction)
        return return_bool

    def turn_around_forward_and_paint(self):
        self.turn_around()
        self.forward()
        self.paint()

    def try_forward(self) -> bool:
        if self.can_move_forward_and_paint():
            self.move_forward_and_paint()
            return True
        else:
            return False

    def try_forward_by_steps(self, steps):
        can_we_move = False
        for i in range(steps):
            can_we_move = self.try_forward()
        return can_we_move

    def try_move(self, route_list: []) -> bool:
        can_we_move = False
        movable_direction = []
        if self.can_move_forward_and_paint():
            can_we_move = True
            for i in range(6):
                movable_direction.append(0)

        if self.can_turn_left_move_and_paint():
            can_we_move = True
            movable_direction.append(3)

        if self.can_turn_right_move_and_paint():
            can_we_move = True
            movable_direction.append(1)

        if not can_we_move:
            return False

        random_index = randint(0, len(movable_direction) - 1)

        if movable_direction[random_index] == 0:
            self.move_forward_and_paint()  # Can move several times
        elif movable_direction[random_index] == 1:
            self.turn_right_move_and_paint()
            self.try_forward_by_steps(3)
        elif movable_direction[random_index] == 3:
            self.turn_left_move_and_paint()
            self.try_forward_by_steps(3)

        route_list.append((self.x, self.y, self.direction))
        # print(self.map.map)
        return True




class Maze:
    def __init__(self):
        self.map = Map(game_launcher.REC_WIDTH, game_launcher.REC_HEIGHT)

    def creat_maze(self):
        self.map.generateMap()
