"""
Show how to use GUI elements.

You can run this example with:
python -m arcade.examples.gui_elements_example

To style, see the style example or use a yaml file.
See:
https://github.com/pvcraven/arcade/blob/development/arcade/resources/style/default.yml
and the UIStyle.from_file() command.

"""
import arcade

import arcade.gui
from arcade.gui import UIManager



# class grid_choice(object):
#     """
#     docstring
#     """
#     def make_grid(grid_length):
#         SCREEN_WIDTH = 600
#         SCREEN_HEIGHT = 600
#         SCREEN_TITLE = "Welcome to Arcade"
#         RADIUS = 150
#         arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
#         #arcade.set_background_color(arcade.color.WHITE)
#         background = arcade.load_texture("images.jpeg")
#         arcade.start_render()
#         arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 
#                 SCREEN_WIDTH, SCREEN_HEIGHT, background)

#         #start rendering
#         grid=int(grid_length)
#         gap = SCREEN_HEIGHT / grid
#         for i in range(0,grid):
#             #x-axis
#             arcade.draw_line(gap*i, 0, gap*i, SCREEN_HEIGHT, arcade.color.BLACK, 3)
#             #y-axis
#             arcade.draw_line(0, gap*i, SCREEN_WIDTH, gap*i, arcade.color.BLACK, 3)

#         #end rendering 
#         arcade.finish_render()
#         arcade.run() 



class MyFlatButton(arcade.gui.UIFlatButton):
    """
    To capture a button click, subclass the button and override on_click.
    """
    def on_click(self):
        """ Called when user lets off button """
        print("My Flat Button")
class MyGhostFlatButton(arcade.gui.UIGhostFlatButton):
    """
    For this subclass, we create a custom init, that takes in another
    parameter, the UI text box. We use that parameter and print the contents
    of the text entry box when the ghost button is clicked.
    """

    def __init__(self, center_x, center_y, input_box):
        super().__init__(
            'Grid Size. OK',
            center_x=center_x,
            center_y=center_y,
            width=250,
            # height=20
        )
        self.input_box = input_box

    def on_click(self):
        """ Called when user lets off button """
        SCREEN_WIDTH = 600
        SCREEN_HEIGHT = 600
        SCREEN_TITLE = "Welcome to Arcade"
        RADIUS = 150
        arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        #arcade.set_background_color(arcade.color.WHITE)
        background = arcade.load_texture("images.jpeg")
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 
                SCREEN_WIDTH, SCREEN_HEIGHT, background)

        #start rendering
        grid=int(self.input_box.text)
        gap = SCREEN_HEIGHT / grid
        for i in range(0,grid):
            #x-axis
            arcade.draw_line(gap*i, 0, gap*i, SCREEN_HEIGHT, arcade.color.BLACK, 3)
            #y-axis
            arcade.draw_line(0, gap*i, SCREEN_WIDTH, gap*i, arcade.color.BLACK, 3)

        #end rendering 
        arcade.finish_render()
        arcade.run()


class MyView(arcade.View):
    """
    Main view. Really the only view in this example. """
    def __init__(self):
        super().__init__()

        self.ui_manager = UIManager()

    def on_draw(self):
        """ Draw this view. GUI elements are automatically drawn. """
        arcade.start_render()

    def on_show_view(self):
        """ Called once when view is activated. """
        self.setup()
        arcade.set_background_color(arcade.color.BLACK)

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def setup(self):
        """ Set up this view. """
        self.ui_manager.purge_ui_elements()

        y_slot = self.window.height // 4
        left_column_x = self.window.width // 4
        right_column_x = 3 * self.window.width // 4

        # left side elements
        self.ui_manager.add_ui_element(arcade.gui.UILabel(
            'Grid By ALi Khan & Zhyaaaaa',
            center_x=left_column_x * 2,
            center_y=y_slot * 3,
        ))

        ui_input_box = arcade.gui.UIInputBox(
            center_x=left_column_x,
            center_y=y_slot * 2,
            width=300
        )
        ui_input_box.text = ''
        ui_input_box.cursor_index = len(ui_input_box.text)
        self.ui_manager.add_ui_element(ui_input_box)
        #grid_choice.make_grid(ui_input_box.text)

        # right side elements

        button = MyGhostFlatButton(
            center_x=right_column_x,
            center_y=y_slot * 2,
            input_box=ui_input_box
        )
        self.ui_manager.add_ui_element(button)


if __name__ == '__main__':
    window = arcade.Window(title='ARCADE_GUI')
    view = MyView()
    window.show_view(view)
    arcade.run()