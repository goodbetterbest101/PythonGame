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
        super().__init__(width, height,title="Penalty Shooter!")
        self.grid = Grid()
        self.player = Player(self.grid)
        self.goalkeeper = Goalkeeper(self.grid,self.player)
        arcade.set_background_color(arcade.color.WHITE)

        self.bg = arcade.Sprite('bg.jpg')
        self.bg.set_position(400,300)

    def animate(self, delta_time):
        self.grid.animate(delta_time)

    def on_draw(self):
        arcade.start_render()
        self.bg.draw()
        self.grid.on_draw()
        self.goalkeeper.on_draw()
        arcade.draw_text("Q", 72, 448, arcade.color.WHITE, 16)
        arcade.draw_text("W", 72, 275, arcade.color.WHITE, 16)
        arcade.draw_text("R", 390, 448, arcade.color.WHITE, 16)
        arcade.draw_text("Y", 390, 275, arcade.color.WHITE, 16)
        arcade.draw_text("I", 710, 448, arcade.color.WHITE, 16)
        arcade.draw_text("O", 710, 275, arcade.color.WHITE, 16)
        arcade.draw_text("E", 230, 360, arcade.color.WHITE, 16)
        arcade.draw_text("U", 550, 360, arcade.color.WHITE, 16)

    def on_key_press(self, key, modifiers):
        self.grid.on_key_press(key, modifiers)
        self.player.on_key_press(key, modifiers)

class Goalkeeper:
    def __init__(self,oldGrid,oldPlayer):
        self.grid = oldGrid
        self.player = oldPlayer
        self.timeStart = 0.0
        self.de = arcade.Sprite('de.png')
        self.de2 = arcade.Sprite('de2.png')
        self.de3 = arcade.Sprite('de3.png')
        self.de22 = arcade.Sprite('de22.png')
        self.de33 = arcade.Sprite('de33.png')
        self.de4 = arcade.Sprite('de4.png')
        self.de5 = arcade.Sprite('de5.png')


    def animate(self, delta_time):
        self.grid.animate(delta_time)

    def on_draw(self):
        if self.player.shoot == False :
            self.de.set_position(400, 350)
            self.de.draw()
        if self.player.shoot == True and self.player.goal == 0 and self.player.posiCol < 7:
            self.de33.set_position(600, 400)
            self.de33.draw()
        if self.player.shoot == True and self.player.goal == 0 and self.player.posiCol == 7:
            self.de2.set_position(200, 400)
            self.de2.draw()
        if self.player.shoot == True and self.player.goal == 0 and self.player.posiCol > 7:
            self.de5.set_position(370, 300)
            self.de5.draw()
        if self.player.shoot == True and self.player.goal == 1 and self.player.posiRow == 10 and self.player.posiCol == 1:
            self.de2.set_position(170, 370)
            self.de2.draw()
        if self.player.shoot == True and self.player.goal == 1 and self.player.posiRow == 6 and self.player.posiCol == 1:
            self.de3.set_position(185, 330)
            self.de3.draw()
        if self.player.shoot == True and self.player.goal == 1 and self.player.posiRow == 10 and self.player.posiCol == 13:
            self.de22.set_position(630, 370)
            self.de22.draw()
        if self.player.shoot == True and self.player.goal == 1 and self.player.posiRow == 6 and self.player.posiCol == 13:
            self.de33.set_position(625, 330)
            self.de33.draw()
        if self.player.shoot == True and self.player.goal == 1 and self.player.posiRow == 10 and self.player.posiCol == 7:
            self.de4.set_position(400, 400)
            self.de4.draw()
        if self.player.shoot == True and self.player.goal == 1 and self.player.posiRow == 8 and self.player.posiCol == 4:
            self.de3.set_position(300, 360)
            self.de3.draw()
        if self.player.shoot == True and self.player.goal == 1 and self.player.posiRow == 8 and self.player.posiCol == 10:
            self.de33.set_position(500, 360)
            self.de33.draw()
        if self.player.shoot == True and self.player.goal == 1 and self.player.posiRow == 6 and self.player.posiCol == 7:
            self.de5.set_position(400, 300)
            self.de5.draw()




class Player:
    def __init__(self,oldGrid):
        self.grid = oldGrid
        self.timeStart = 0.0
        self.goal = 0
        self.posiRow = 0
        self.posiCol = 0
        self.shoot = False

    def on_key_press(self, key, modifiers):
        if key == arcade.key.Q:
            self.checkGoal(10,1)
        if key == arcade.key.W:
            self.checkGoal(6,1)
        if key == arcade.key.E:
            self.checkGoal(8,4)
        if key == arcade.key.R:
            self.checkGoal(10,7)
        if key == arcade.key.Y:
            self.checkGoal(6,7)
        if key == arcade.key.U:
            self.checkGoal(8,10)
        if key == arcade.key.I:
            self.checkGoal(10,13)
        if key == arcade.key.O:
            self.checkGoal(6,13)
        if self.grid.SpacePress == True :
            self.shoot = False

    def checkGoal(self,row,col):
        if self.grid.grid[row][col] == 0:
            self.shoot = True
            print ("Goal !!")
            self.goal = 0
            self.posiRow = row
            self.posiCol = col
        if self.grid.grid[row][col] == 1:
            self.shoot = True
            print ("Miss !!")
            self.goal = 1
            self.posiRow = row
            self.posiCol = col

    def animate(self, delta_time):
        self.timeStart += delta_time

class Grid:
    def __init__(self):
        # self.player = Player()
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
                # print("grid[{}][{}] = {}".format(self.dataRow[0],self.dataCol[0],self.grid[self.dataRow[0]][self.dataCol[0]]))
                # print("grid[{}][{}] = {}".format(self.dataRow[1],self.dataCol[1],self.grid[self.dataRow[1]][self.dataCol[1]]))
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
