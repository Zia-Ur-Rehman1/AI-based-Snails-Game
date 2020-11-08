import arcade
import os
import random
import math

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

SPRITE_SCALING = 0.10
board=[]

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Khan Alone"

MOVEMENT_SPEED = 60



       
            
   
class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        background = arcade.load_texture("menu4.jpg")
        arcade.start_render()
        
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
        background = arcade.load_texture("start.jpg")
        snail = arcade.load_texture("1.png",)
        snail = arcade.load_texture("2.png",flipped_horizontally=True)
        arcade.start_render()
        
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,background)
        arcade.draw_text("S N A I L S", SCREEN_WIDTH/2, SCREEN_HEIGHT-180,
                         arcade.color.SKY_BLUE, font_size=50, bold=True,anchor_x="center")
        
       
        arcade.draw_text("Click To Begin The Challenge", SCREEN_WIDTH/2, SCREEN_HEIGHT-400,
                         arcade.color.GRAY_ASPARAGUS, font_size=25,bold=True,font_name='calibri', anchor_x="center")
        arcade.draw_lrwh_rectangle_textured(50, 600,100,100,snail)
        arcade.draw_lrwh_rectangle_textured(SCREEN_WIDTH-150, 600,100,100,snail)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)

"""End Instructions View"""
"""                                         Game Start"""



class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.time_taken = 0
        self.score=0
        self.turn=0
        self.state="Game On"
        # Sprite lists
      
        # Set up the player
        
       
      

    def initialize_board(self,rows,cols):
        for i in range(cols): 
            col = [] 
            for j in range(rows): 
                col.append(0) 
            board.append(col) 
        board[9][0],board[0][9]=1,2
        for x in board:
            print(x)
    def on_show(self):
        # Don't show the mouse cursor
        self.window.set_mouse_visible(True)

    def on_draw(self):
        background = arcade.load_texture("menu4.jpg")
        s1=arcade.load_texture('s1.png')
        s2=arcade.load_texture('s2.png')
        p1=arcade.load_texture('1.png')
        p2=arcade.load_texture('2.png',flipped_horizontally=True)

        if(self.state=="Game On"):

            arcade.start_render()
        # Draw all the sprites.
            arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,background)
            

        # Put the text on the screen.
            output = f"Score: {self.score}"
            arcade.draw_text(output, 250, 750, arcade.color.WHITE, 14)
            output_total = f"Total Score: {self.window.total_score}"
            arcade.draw_text(output_total, 10, 10, arcade.color.WHITE, 14)
            turn=f"Turn Of Player: {self.turn+1}"
            # time_taken=f"Time Taken:{self.time_taken}"
            arcade.draw_text(turn, 350, 750, arcade.color.WHITE,20,italic=True)
            # arcade.draw_text(time_taken, 450, 700, arcade.color.WHITE,20,italic=True)
        
            """ Making Grid"""
            box=int(600/10)
        
# Started making grid  
            for y in range (100,701,box):
    # for horizontal line 
   
                arcade.draw_line(100,y,700,y,arcade.color.GRAY_BLUE,5)
    # for verticle line
                arcade.draw_line(y,100,y,700,arcade.color.GRAY_BLUE,5)
            for y in range(0,10):
                for x in range(0,10):
                    if(board[y][x]==11):
                        arcade.draw_lrwh_rectangle_textured(100+(x*60),630-(60*y)+10,50,50,s1)
                    elif(board[y][x]==22):
                        arcade.draw_lrwh_rectangle_textured(100+(x*60),630-(60*y)+10,50,50,s2)
                    elif(board[y][x]==1):
                        arcade.draw_lrwh_rectangle_textured(100+(x*60),630-(60*y)+10,50,50,p1)
                    elif(board[y][x]==2):
                        arcade.draw_lrwh_rectangle_textured(100+(x*60),630-(60*y)+10,50,50,p2)
            
        # Draw all the sprites.
            """ Ending Grid"""

    def on_update(self, delta_time):
        self.time_taken += delta_time
     
       
   
    def get_human_pos(self):
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == 1:
                    print (row, col)
                    return row , col
    def get_bot_pos(self):
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == 2:
                    return row , col
 
    
    

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if(self.state=="Game On"):
            if key == arcade.key.ESCAPE:
                exit(0)
                # pass self, the current view, to preserve this view's state
                # pause = PauseView(self)
                # self.window.show_view(pause)
            elif  self.turn==0:
                x,y=self.get_human_pos()
                if key == arcade.key.UP :
                    if(x==0 or board[x-1]==2 or board[x-1]==11 or board[x-1]==22):
                        pass
                    elif(board[x-1][y]==0):
                        board[x][y]=11
                        board[x-1][y]=1

                     
                    
                elif key == arcade.key.DOWN :
                    if(x==9 or board[x+1]==2 or board[x+1]==11 or board[x+1]==22):
                        pass
                    elif(board[x+1][y]==0):
                        board[x][y],board[x+1][y]=11,1

                        
                     
                elif key == arcade.key.LEFT :
                    if(y==0 or board[y-1]==2 or board[y-1]==11 or board[y-1]==22):
                        pass
                    elif(board[x][y-1]==0):
                        board[x][y]=11
                        board[x][y-1]=1

                     
                elif key == arcade.key.RIGHT :
                    if(y==9 or board[y+1]==2 or board[y+1]==11 or board[y+1]==22):
                        pass
                    elif(board[x][y+1]==0):
                        board[x][y]=11
                        board[x][y+1]=1
                  
                   
                
                self.turn+=1

            elif self.turn==1:    
                x,y=self.get_bot_pos()
                if key == arcade.key.UP :
                    if(x==0 or board[x-1]==1 or board[x-1]==11 or board[x-1]==22):
                        pass
                    elif(board[x-1][y]==0):
                        board[x][y]=22
                        board[x-1][y]=2

                        
                elif key == arcade.key.DOWN :
                    if(x==9 or board[x+1]==1 or board[x+1]==11 or board[x+1]==22):
                        pass
                    elif(board[x+1][y]==0):
                        board[x][y],board[x+1][y]=22,2

                    
                elif key == arcade.key.LEFT :
                    if(y==0 or board[y-1]==1 or board[y-1]==11 or board[y-1]==22):
                        pass
                    elif(board[x][y-1]==0):
                        board[x][y]=22
                        board[x][y-1]=2

                     
                      
                elif key == arcade.key.RIGHT :
                    if(y==9 or board[y+1]==1 or board[y+1]==11 or board[y+1]==22):
                        pass
                    elif(board[x][y+1]==0):
                        board[x][y]=22
                        board[x][y+1]=2
                    
                       
                self.turn-=1

  
        """
       End of Movement With Keyboard
        """
   

class PauseView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view

    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE)

    def on_draw(self):
        arcade.start_render()

        # Draw player, for effect, on pause screen.
        # The previous View (GameView) was passed in
        # and saved in self.game_view.
        player_sprite = self.game_view.player_sprite
        player_sprite.draw()

        # draw an orange filter over him
        arcade.draw_lrtb_rectangle_filled(left=player_sprite.left,
                                          right=player_sprite.right,
                                          top=player_sprite.top,
                                          bottom=player_sprite.bottom,
                                          color=arcade.color.ORANGE + (200,))

        arcade.draw_text("PAUSED", SCREEN_WIDTH/2, SCREEN_HEIGHT/2+50,
                         arcade.color.BLACK, font_size=50, anchor_x="center")

        # Show tip to return or reset
        arcade.draw_text("Press Esc. to return",
                         SCREEN_WIDTH/2,
                         SCREEN_HEIGHT/2,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Press Enter to reset",
                         SCREEN_WIDTH/2,
                         SCREEN_HEIGHT/2-30,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")
        

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:   # resume game
            self.window.show_view(self.game_view)
        elif key == arcade.key.ENTER:  # reset game
            game = GameView()
            self.window.show_view(game)

def main():
    
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE,resizable=True)
    window.total_score = 0
    menu_view = MenuView()
    window.center_window()
    window.show_view(menu_view)
    rows, cols = (10, 10)
    g=GameView()
    g.initialize_board(rows,cols)
    arcade.run()


if __name__ == "__main__":
    main()