import arcade
from random import randint, random
from random import shuffle, random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WIDTH = 50
HEIGHT = 40

MARGIN = 3;

class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.grid = Grid()
        arcade.set_background_color(arcade.color.WHITE)
        self.bg = arcade.Sprite('bg.jpg')
        self.bg.set_position(400,300)

    def animate(self, delta_time):
        self.grid.animate(delta_time)

    def on_draw(self):
        arcade.start_render()
        self.bg.draw()
        self.grid.on_draw()

    def on_key_press(self, key, modifiers):
        self.grid.on_key_press(key, modifiers)



class Grid:
    def __init__(self):
        self.grid = []
        self.SpacePress = False
        self.dataRow = [6,8,10]
        self.dataCol = [1,4,7,10,13]
        self.timeStart = 0.0
        self.temp = 0.0
        for row in range(14):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(20):
                self.grid[row].append(0)  # Append a cell

    def animate(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        if(self.SpacePress == True):
            if(self.timeStart < self.temp + 4):
                shuffle(self.dataCol)
                shuffle(self.dataRow)
                self.grid[self.dataRow[0]][self.dataCol[0]] = 1
                self.grid[self.dataRow[1]][self.dataCol[1]] = 0
            else :
                self.SpacePress = False
        self.timeStart += delta_time

    def on_key_press(self, key, modifiers):
        """
        Called whenever the mouse moves.
        """
        if key == arcade.key.SPACE:
            self.temp = self.timeStart
            self.SpacePress = True

    def checkPosition(self,row,column):
        check = 0
        if ( row == 6 and column == 1 ):
            check = 1
        if ( row == 10 and column == 1 ):
            check = 1
        if ( row == 10 and column == 13 ):
            check = 1
        if ( row == 6 and column == 13 ):
            check = 1
        if ( row == 10 and column == 7 ):
            check = 1
        if ( row == 6 and column == 7 ):
            check = 1
        if ( row == 8 and column == 4 ):
            check = 1
        if ( row == 8 and column == 10 ):
            check = 1
        return check

    def on_draw(self):
        for row in range(14):
            for column in range(20):
                if self.checkPosition(row,column):
                    #self.randomPosition()
                    if self.grid[row][column] == 1:
                        color = arcade.color.BLACK
                    else:
                        color = arcade.color.WHITE

                    # Do the math to figure out where the box is
                    x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                    y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                    # Draw the box
                    arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
