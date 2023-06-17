import game_launcher


class Wall_Detect():
    def __init__(self,x,y,direction,map):
        self.x_in = x
        self.y_in = y
        self.direction = direction
        self.map = map
        self.x_pane = 0
        self.y_pane = 0
        self.x_out = 0
        self.y_out = 0

    def pixel_pane(self,x,y):
        self.x_pane = x//game_launcher.SIZE_PANE
        self.y_pane = y//game_launcher.SIZE_PANE

    def pane_pixel(self,x,y):
        if self.direction == "left":
            self.x_out = (x + 1) * game_launcher.SIZE_PANE
        elif self.direction == "right":
            self.x_out = x * game_launcher.SIZE_PANE
        elif self.direction == "up":
            self.y_out = (y + 1) * game_launcher.SIZE_PANE
        elif self.direction == "down":
            self.y_out = y * game_launcher.SIZE_PANE

    def wall(self):
        self.pixel_pane(self.x_in,self.y_in)
        if self.direction == "left":
            self.x_pane -= 1
            if self.map[self.x_pane][self.y_pane].kind == 0:
                self.pane_pixel(self.x_pane,self.y_pane)
            else:
                self.wall()
        elif self.direction == "right":
            self.x_pane += 1
            if self.map[self.x_pane][self.y_pane].kind == 0:
                self.pane_pixel(self.x_pane, self.y_pane)
            else:
                self.wall()
        elif self.direction == "up":
            self.y_pane -= 1
            if self.map[self.x_pane][self.y_pane].kind == 0:
                self.pane_pixel(self.x_pane, self.y_pane)
            else:
                self.wall()
        elif self.direction == "down":
            self.y_pane += 1
            if self.map[self.x_pane][self.y_pane].kind == 0:
                self.pane_pixel(self.x_pane, self.y_pane)
            else:
                self.wall()