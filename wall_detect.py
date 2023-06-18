import game_launcher


class Wall_Detect():
    def __init__(self,x,y,direction,map):
        self.x_in = x
        self.y_in = y
        self.direction = direction
        self.map = map
        self.x_pane = 0
        self.y_pane = 0
        self.x_out_left = 0
        self.x_out_right = 0
        self.y_out_up = 0
        self.y_out_down = 0

    def pixel_pane(self,x,y):
        self.x_pane = x//game_launcher.SIZE_PANE
        self.y_pane = y//game_launcher.SIZE_PANE

    def pane_pixel_player(self,x,y):
        if self.direction == "left":
            self.x_out_left = (x + 1) * game_launcher.SIZE_PANE
        elif self.direction == "right":
            self.x_out_right = x * game_launcher.SIZE_PANE
        elif self.direction == "up":
            self.y_out_up = (y + 1) * game_launcher.SIZE_PANE
        elif self.direction == "down":
            self.y_out_down = y * game_launcher.SIZE_PANE

    def pane_pixel_enemy(self,x,y,direction):
        if direction == "left":
            self.x_out_left = (x + 1) * game_launcher.SIZE_PANE
        elif direction == "right":
            self.x_out_right = x * game_launcher.SIZE_PANE
        elif direction == "up":
            self.y_out_up = (y + 1) * game_launcher.SIZE_PANE
        elif direction == "down":
            self.y_out_down = y * game_launcher.SIZE_PANE

    def wall_player(self):
        self.pixel_pane(self.x_in + int(game_launcher.WIDTH_PLAYER / 2), self.y_in + int(game_launcher.HEIGHT_PLAYER / 2))
        if self.direction == "left":
            while self.map.getType(self.x_pane,self.y_pane) != "MAP_ENTRY_TYPE.MAP_BLOCK" and self.x_pane > 0:
                self.x_pane -= 1
            self.pane_pixel_player(self.x_pane,self.y_pane)
        elif self.direction == "right":
            while self.map.getType(self.x_pane,self.y_pane) != "MAP_ENTRY_TYPE.MAP_BLOCK" and self.x_pane < game_launcher.WIDTH_PANE:
                self.x_pane += 1
            self.pane_pixel_player(self.x_pane, self.y_pane)
        elif self.direction == "up":
            while self.map.getType(self.x_pane,self.y_pane) != "MAP_ENTRY_TYPE.MAP_BLOCK" and self.y_pane > 0:
                self.y_pane -= 1
            self.pane_pixel_player(self.x_pane, self.y_pane)
        elif self.direction == "down":
            while self.map.getType(self.x_pane,self.y_pane) != "MAP_ENTRY_TYPE.MAP_BLOCK" and self.y_pane < game_launcher.HEIGHT_PANE:
                self.y_pane += 1
            self.pane_pixel_player(self.x_pane, self.y_pane)

    def wall_enemy(self):
        self.pixel_pane(self.x_in, self.y_in)
        x = self.x_pane
        y = self.y_pane
        if self.direction == "left" or self.direction == "right":
            while self.map.getType(x,y) != "MAP_ENTRY_TYPE.MAP_BLOCK" and x > 0:
                x -= 1
            self.pane_pixel_enemy(x, y, "left")
            while self.map.getType(self.x_pane,self.y_pane) != "MAP_ENTRY_TYPE.MAP_BLOCK" and self.x_pane < game_launcher.WIDTH_PANE:
                self.x_pane += 1
            self.pane_pixel_enemy(self.x_pane, self.y_pane, "right")
        elif self.direction == "up" or self.direction == "down":
            while self.map.getType(x,y) != "MAP_ENTRY_TYPE.MAP_BLOCK" and y > 0:
                y -= 1
            self.pane_pixel_enemy(x, y, "up")
            while self.map.getType(self.x_pane,self.y_pane) != "MAP_ENTRY_TYPE.MAP_BLOCK" and self.y_pane < game_launcher.HEIGHT_PANE:
                self.y_pane += 1
            self.pane_pixel_enemy(self.x_pane, self.y_pane, "down")

