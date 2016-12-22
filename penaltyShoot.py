import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WIDTH = 50
HEIGHT = 40

MARGIN = 3;

class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.grid = []
        for row in range(14):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(20):
                self.grid[row].append(0)  # Append a cell


        arcade.set_background_color(arcade.color.BLACK)

        # self.ship = arcade.Sprite('ship.png', 5)
        # self.ship.set_position(100, 100)
        self.bg = arcade.Sprite('bg.png')
        self.bg.set_position(400,300)

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
        arcade.start_render()
        self.bg.draw()
        for row in range(14):
            for column in range(20):
                if self.checkPosition(row,column):
                    if self.grid[row][column] == 1:
                        color = arcade.color.GREEN
                    else:
                        color = arcade.color.WHITE

                    # Do the math to figure out where the box is
                    x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                    y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                    # Draw the box
                    arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)



    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """

        # Change the x/y screen coordinates to grid coordinates
        column = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        # Set that location to one
        self.grid[row][column] = 1
        print("Click coordinates: ({}, {}). Grid coordinates: ({}, {})"
              .format(x, y, row, column))



if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
