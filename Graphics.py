import tkinter as tk
# from game import Game
# from bot import Bot
import constants as c
import time


class Graphics(tk.Tk):
    def __init__(self, board):
        super().__init__()
        # window
        # self.window = tk.Tk()
        self.title("Minesweeper")
        # self.grid = grid
        self.board = board
        # self.bot = bot

        # labels
        self.header = tk.Frame(self, bg=c.BOARD_COLOR,
                                   width=c.WINDOW_WIDTH,
                                   height=c.WINDOW_HEIGHT)
        self.header.grid(column=0, row=0)

        label = tk.Label(self.header, text="Minesweeper", font=c.TITLE_FONT)
        label.grid(column=0, row=0)

        dummy = tk.Label(self.header, text="                 ", font=c.TITLE_FONT)
        dummy.grid(column=1, row=0)
        dummy.grid(column=2, row=0)

        num_mins_label = tk.Label(self.header, text="Num Mines:", font=c.TITLE_FONT)
        num_mins_label.grid(column=3, row=0)

        self.num_mines_value = tk.Label(self.header, text=str(c.NUM_MINES).ljust(8), font=c.TITLE_FONT)
        self.num_mines_value.grid(column=4, row=0)


        # key binding
        # self.bind("<Key>", self.take_turn)
        self.bind("<s>", self.start)

        self.grid_tiles = []
        self.background = tk.Frame(self, bg=c.BOARD_COLOR,
                                   width=c.WINDOW_WIDTH,
                                   height=c.WINDOW_HEIGHT)

        self.init_board()

        # buttons
        self.start_button = tk.Button(self, text="Start Game", command=self.start)
        self.start_button.grid(column=0, row=1)

        self.game_over_frame = tk.Frame(self.background, bg=c.BOARD_COLOR,
                                        width=c.WINDOW_WIDTH,
                                        height=c.WINDOW_HEIGHT)

        self.game_over = tk.Label(self.game_over_frame,
                                  text='GAME OVER',
                                  bg=c.BOARD_COLOR,
                                  justify=tk.CENTER,
                                  font=c.TILE_FONT,
                                  width=6,
                                  height=4)

        self.background.grid(column=0, row=2)

        # start the window running
        self.mainloop()

    def init_board(self):
        for row in range(c.BOARD_SIZE):
            row_tiles = []
            for col in range(c.BOARD_SIZE):
                tile = tk.Frame(self.background, bg=c.tile_color_dict[0],
                                width=c.WINDOW_WIDTH / c.BOARD_SIZE,
                                height=c.WINDOW_HEIGHT / c.BOARD_SIZE)
                tile.grid(row=row, column=col,
                          padx=c.TILE_PADX, pady=c.TILE_PADY)
                # value = tk.Button(tile, text="", command= lambda: self.button_click(row, col), width=c.TILE_WIDTH, height=c.TILE_HEIGHT)
                value = tk.Label(tile,
                                 text='',
                                 bg=c.tile_color_dict[0],
                                 justify=tk.CENTER,
                                 font=c.TILE_FONT,
                                 width=c.TILE_WIDTH,
                                 height=c.TILE_HEIGHT)
                value.grid(column=col, row=row)
                row_tiles.append(value)
            self.grid_tiles.append(row_tiles)

    def start(self, *args):
        while not self.board.dead() or self.board.win():
            row = int(input())
            col = int(input())
            self.board.click_tile(row, col)
            self.display_board()

        self.end_game()

    def display_board(self):
        # print(self.grid_tiles)
        # print(len(self.grid_tiles))
        # print(len(self.grid_tiles[0]))
        for row in range(len(self.grid_tiles)):
            for col in range(len(self.grid_tiles)):
                if self.board.grid[row][col] is not None and self.board.grid[row][col].clicked:
                    # print(row, col)
                    value = self.board.grid[row][col].number
                    self.grid_tiles[row][col].configure(text=str(value))
                else:
                    self.grid_tiles[row][col].configure(text='')
        self.update_idletasks()

    # def take_turn(self, event):
    #     direction = event.keysym.lower()
    #     # input("press enter to continue...")
    #     # time.sleep(1)
    #     try:
    #         self.game.take_turn(direction)
    #         self.display_board(self.game.get_board().get_grid())
    #         self.update_score(self.game.get_score())
    #         if self.game.game_over():
    #             self.end_game()
    #     except:
    #         print('game over')

    def end_game(self):
        print('here')
        #Check if we've won or lost the game (-1 for lose, 1 for win)
        win_or_lose = 0
        if self.board.dead():
            win_or_lose = -1

        if self.board.win():
            win_or_lose = 1    


        del self.board

        self.game_over_frame.place(relheight=1 / 4, relwidth=3 / 4,
                                   relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.game_over_frame.lift()
        # value.place(anchor=tk.CENTER)
        if win_or_lose == -1:
            self.game_over.configure(text='GAME OVER')

        if win_or_lose == 1:
            self.game_over.configure(text='YOU WON! :)')
        
        self.game_over.place(relheight=1, relwidth=1,
                             relx=0.5, rely=0.5, anchor=tk.CENTER)
        # value.grid()

        self.bind("<s>", self.start)
        self.start_button["state"] = "normal"

    def button_click(self, row, col):
        #wraps the 2 functions so that clicking a button can
        #actually click the tile and update how the board looks
        print('clicking')
        self.board.click_tile(row, col)
        self.display_board()


# if __name__ == "__main__":
#     Graphics(bot=True, heuristic=c.HIGHSCORE)
