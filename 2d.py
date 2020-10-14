# Displays a white window with a blue circle in the middle
import arcade
import os

SPRITE_SCALING = 0.5
MOVEMENT_SPEED = 5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Welcome to Arcade Snails"
background = None
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
# arcade.set_background_color(arcade.color.ALIZARIN_CRIMSON)


arcade.start_render()


# added background
background = arcade.load_texture("menu4.jpg")
arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,background)
# ended background
box=int(600/10)
# Started making grid  
for y in range (100,701,box):
    # for horizontal line 
   
    arcade.draw_line(100,y,700,y,arcade.color.WHITE,5)
    # for verticle line
    arcade.draw_line(y,100,y,700,arcade.color.GRAY,5)

#making sprite to appear
background1=None    
backgroun1 = arcade.load_texture("n.jpg")

arcade.draw_lrwh_rectangle_textured(105,105,90,90,backgroun1)
arcade.finish_render()

arcade.run()