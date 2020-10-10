"""
Better Move Sprite With Keyboard

Simple program to show moving a sprite with the keyboard.
This is slightly better than sprite_move_keyboard.py example
in how it works, but also slightly more complex.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_keyboard_better
"""

import arcade
import os
SPRITE_SCALING = 0.95

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Khan Alone"

MOVEMENT_SPEED = 100


class Player(arcade.Sprite):
    def update(self):
     
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 100:
            self.left = 100
        elif self.right > SCREEN_WIDTH - 100:
            self.right = SCREEN_WIDTH - 100

        if self.bottom < 100:
            self.bottom = 100
        elif self.top > SCREEN_HEIGHT - 100:
            self.top = SCREEN_HEIGHT - 100


class MyGame(arcade.Window):
    """
    Main application class.
    """
    def __init__(self, width, height, title):
        """
        Initializer
        """
        

        # Call the parent class initializer
        super().__init__(width, height, title)
        
        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Variables that will hold sprite lists
        self.player_list = None

        # Set up the player info
        self.player_sprite = None
        
        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.turn=0
        
        # Set up the player
        self.player_sprite = Player(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING)
        self.player_sprite1 = Player(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING)
        
        self.player_sprite.center_x = 150
        self.player_sprite.center_y = 165
        self.player_sprite1.center_x = 550
        self.player_sprite1.center_y = 565
        self.player_list.append(self.player_sprite)
        self.player_list.append(self.player_sprite1)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()


        background = arcade.load_texture("wow.jpg")
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,background)
        for y in range (100,700,100):
    # for horizontal line 
   
            arcade.draw_line(100,y,600,y,arcade.color.WHITE,5)
    # for verticle line
            arcade.draw_line(y,100,y,600,arcade.color.GRAY,5)
        # Draw all the sprites.

        # Draw all the sprites.
        self.player_list.draw()
    def on_update(self, delta_time):
        """ Movement and game logic """
        print(self.turn)
        if(self.turn==0):
            self.turn=self.turn+1
        # Calculate speed based on the keys pressed
            self.player_sprite.change_x = 0
            self.player_sprite.change_y = 0

            if self.up_pressed and not self.down_pressed:
                self.player_sprite.change_y = MOVEMENT_SPEED
            elif self.down_pressed and not self.up_pressed:
                self.player_sprite.change_y = -MOVEMENT_SPEED
            if self.left_pressed and not self.right_pressed:
                self.player_sprite.change_x = -MOVEMENT_SPEED
            elif self.right_pressed and not self.left_pressed:
                self.player_sprite.change_x = MOVEMENT_SPEED
            self.player_list.update()

        else:
            self.turn=self.turn-1
        # Calculate speed based on the keys pressed
            self.player_sprite1.change_x = 0
            self.player_sprite1.change_y = 0

            if self.up_pressed and not self.down_pressed:
                self.player_sprite1.change_y = MOVEMENT_SPEED
            elif self.down_pressed and not self.up_pressed:
                self.player_sprite1.change_y = -MOVEMENT_SPEED
            if self.left_pressed and not self.right_pressed:
                self.player_sprite1.change_x = -MOVEMENT_SPEED
            elif self.right_pressed and not self.left_pressed:
                self.player_sprite1.change_x = MOVEMENT_SPEED
            self.player_list.update()

        # Call update to move the sprite
        # If using a physics engine, call update on it instead of the sprite
        # list.
            
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()