# Displays a white window with a blue circle in the middle
import arcade
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Welcome to Arcade Snails"
RADIUS = 150
background = None
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
# arcade.set_background_color(arcade.color.ALIZARIN_CRIMSON)

arcade.start_render()
# added background
background = arcade.load_texture("wow.jpg")
arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,background)
# ended background

# Started making grid  

for y in range (0,500,100):

    arcade.draw_line(0,y,500,y,arcade.color.WHITE,5)
    arcade.draw_line(y,0,y,500,arcade.color.GRAY,5)

arcade.finish_render()

arcade.run()