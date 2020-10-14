import arcade
import os
import random


file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)


SPRITE_SCALING = 0.10

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Khan Alone"

MOVEMENT_SPEED = 60


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

class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        background = arcade.load_texture("menu4.jpg")
        
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,background)
        arcade.draw_text("Khan Alone", SCREEN_WIDTH/2, SCREEN_HEIGHT-270,
                         arcade.color.BLUEBERRY, font_size=90, anchor_x="center")
        arcade.draw_text("Click to Enter The Game", SCREEN_WIDTH/2, SCREEN_HEIGHT-320,
                         arcade.color.RED, font_size=40, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instructions_view = InstructionView()
        self.window.show_view(instructions_view)



"""Instructions View"""

class InstructionView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        arcade.start_render()
        background = arcade.load_texture("start.jpg")
        
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,background)
        arcade.draw_text("S N A I L S", SCREEN_WIDTH/2, SCREEN_HEIGHT-180,
                         arcade.color.SKY_BLUE, font_size=50, bold=True,anchor_x="center")
        
       
        arcade.draw_text("Click To Begin The Challenge", SCREEN_WIDTH/2, SCREEN_HEIGHT-400,
                         arcade.color.GRAY_ASPARAGUS, font_size=25,bold=True,font_name='calibri', anchor_x="center")
        snail = arcade.load_texture("1.png",)
        arcade.draw_lrwh_rectangle_textured(50, 600,100,100,snail)
        snail = arcade.load_texture("2.png",flipped_horizontally=True)
        arcade.draw_lrwh_rectangle_textured(SCREEN_WIDTH-150, 600,100,100,snail)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)

"""End Instructions View"""
"""Game Start"""



class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        self.time_taken = 0
        self.score=0
        # Sprite lists
        self.player_list = arcade.SpriteList()
        
        self.player_sprite = None
        # Set up the player
        self.player_sprite = Player("1.png", SPRITE_SCALING)
        self.player_sprite2 = Player("2.png", SPRITE_SCALING,flipped_horizontally=True)
        self.player_sprite.center_x = 130
        self.player_sprite.center_y = 120
        self.player_sprite2.center_x =  SCREEN_WIDTH- 130
        self.player_sprite2.center_y = SCREEN_HEIGHT- 134

        self.player_list.append(self.player_sprite)
        self.player_list.append(self.player_sprite2)
        
        
    # def on_show(self):
    #     arcade.set_background_color(arcade.color.AMAZON)

    #     # Don't show the mouse cursor
    #     self.window.set_mouse_visible(False)

    def on_draw(self):
        arcade.start_render()
        # Draw all the sprites.
        background = arcade.load_texture("menu4.jpg")
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,background)
        self.player_list.draw()
       
        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 30, arcade.color.WHITE, 14)
        output_total = f"Total Score: {self.window.total_score}"
        arcade.draw_text(output_total, 10, 10, arcade.color.WHITE, 14)
        turn=f"Turn Of Player 1"
        arcade.draw_text(turn, 350, 750, arcade.color.WHITE,20,italic=True)

        """ Making Grid"""
        box=int(600/10)
        
# Started making grid  
        for y in range (100,701,box):
    # for horizontal line 
   
            arcade.draw_line(100,y,700,y,arcade.color.GRAY_BLUE,5)
    # for verticle line
            arcade.draw_line(y,100,y,700,arcade.color.GRAY,5)

        # Draw all the sprites.
        """ Ending Grid"""
        

    def on_update(self, delta_time):
        self.time_taken += delta_time

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        
       # self.player_list.update()

        # Generate a list of all sprites that collided with the player.
       # hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the
        # score.
        
        # If we've collected all the games, then move to a "GAME_OVER"
        # state.
        """
        Call of Game Over
        """
        # if len(self.coin_list) == 0:
        #     game_over_view = GameOverView()
        #     game_over_view.time_taken = self.time_taken
        #     self.window.set_mouse_visible(True)
        #     self.window.show_view(game_over_view)
        """
        End Call of Game Over
        """
        """
        Movement With Keyboard
        """

        
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
        self.player_list.update()

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
        """
       End of Movement With Keyboard
        """
   


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.total_score = 0
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()