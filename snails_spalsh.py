
import arcade
import os


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Khan Alone"
arcade.open_window(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
arcade.start_render()

background = arcade.load_texture("wow.jpg")
arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,background,alpha=240)
""" Placing Tick Cross Images"""
s1=arcade.load_texture("sn.png")
s1_s=arcade.load_texture("black.png")
jump=60
arcade.draw_lrwh_rectangle_textured(234,235,68,73,s1)
arcade.draw_lrwh_rectangle_textured(5,245,50, 50,s1_s)
arcade.draw_lrwh_rectangle_textured(65,245,50, 50,s1_s)
arcade.draw_lrwh_rectangle_textured(125,245,50, 50,s1_s)
arcade.draw_lrwh_rectangle_textured(185,245,50, 50,s1_s)
arcade.draw_lrwh_rectangle_textured(245,305,50, 50,s1_s)
arcade.draw_lrwh_rectangle_textured(245,185,50, 50,s1_s)
arcade.draw_lrwh_rectangle_textured(245,365,50, 50,s1_s)

arcade.draw_lrwh_rectangle_textured(245,425,50, 50,s1_s)

arcade.draw_lrwh_rectangle_textured(185,185,50, 50,s1_s)
arcade.draw_lrwh_rectangle_textured(125,125,50, 50,s1_s)
arcade.draw_lrwh_rectangle_textured(65,65,50, 50,s1_s)
arcade.draw_lrwh_rectangle_textured(5,5,50, 50,s1_s)
arcade.draw_lrwh_rectangle_textured(65,5,50, 50,s1_s)
arcade.draw_lrwh_rectangle_textured(125,5,50, 50,s1_s)
arcade.draw_lrwh_rectangle_textured(185,5,50, 50,s1_s)

s2=arcade.load_texture("s2.png",flipped_horizontally=True)
s2_s=arcade.load_texture("blue.png")

arcade.draw_lrwh_rectangle_textured(303,300,60, 60,s2)
arcade.draw_lrwh_rectangle_textured(365,305,50, 50,s2_s)
arcade.draw_lrwh_rectangle_textured(545,305,50, 50,s2_s)

arcade.draw_lrwh_rectangle_textured(365,365,50, 50,s2_s)

arcade.draw_lrwh_rectangle_textured(425,425,50, 50,s2_s)
arcade.draw_lrwh_rectangle_textured(485,485,50, 50,s2_s)
arcade.draw_lrwh_rectangle_textured(545,545,50, 50,s2_s)
arcade.draw_lrwh_rectangle_textured(545,485,50, 50,s2_s)
arcade.draw_lrwh_rectangle_textured(545,425,50, 50,s2_s)
arcade.draw_lrwh_rectangle_textured(545,365,50, 50,s2_s)
arcade.draw_lrwh_rectangle_textured(485,425,50, 50,s2_s)




box=int(SCREEN_WIDTH/10)
for x in range(0, SCREEN_WIDTH,box):
    """For X-AXIS """
    
    arcade.draw_line(0,x,SCREEN_HEIGHT,x,arcade.color.FALLOW,4)
  

    """For Y-AXIS """
    arcade.draw_line(x,0,x,SCREEN_WIDTH,arcade.color.FALLOW,4)

   

arcade.finish_render()
arcade.run()