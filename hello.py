# Displays a white window with a blue circle in the middle
import arcade
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Welcome to Arcade"
RADIUS = 150
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

arcade.draw_line(0,300,600,300,arcade.color.AQUA,5)

arcade.finish_render()
arcade.run()