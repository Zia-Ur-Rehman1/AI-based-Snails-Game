"""
Move Sprite With Keyboard

Simple program to show moving a sprite with the keyboard.
The sprite_move_keyboard_better.py example is slightly better
in how it works, but also slightly more complex.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_keyboard
"""

import arcade
import os

SPRITE_SCALING = 0.95

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
SCREEN_TITLE = "2D Game By Khan Alone"

MOVEMENT_SPEED = 100
arcade.open_window(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)

        # This command has to happen before we start drawing
arcade.start_render()


background = arcade.load_texture("wow.jpg")
arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,background)
x=50
for y in range (100,700,100+x):
    # for horizontal line 
   
    arcade.draw_line(100,y,600-x,y,arcade.color.WHITE,5)
    # for verticle line
    arcade.draw_line(y,100,y,600-x,arcade.color.GRAY,5)
arcade.finish_render()
arcade.run()