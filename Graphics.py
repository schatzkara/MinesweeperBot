import tkinter as tk
# from game import Game
# from bot import Bot
import gui_constants as c
import time


class Graphics(tk.Tk):
	def __init__(self, board, bot):
		super().__init__()
		self.title("Minesweeper")
		self.board = board
		self.board_size = self.board.size
		self.num_mines = self.board.num_mines
		self.bot = bot

		# labels
		self.header = tk.Frame(self, bg=c.BOARD_COLOR, width=c.WINDOW_WIDTH, height=c.WINDOW_HEIGHT)
		self.header.grid(column=0, row=0)

		label = tk.Label(self.header, text="Minesweeper", font=c.TITLE_FONT)
		label.grid(column=0, row=0)

		dummy = tk.Label(self.header, text="                 ", font=c.TITLE_FONT)
		dummy.grid(column=1, row=0)
		dummy.grid(column=2, row=0)

		num_mins_label = tk.Label(self.header, text="Num Mines:", font=c.TITLE_FONT)
		num_mins_label.grid(column=3, row=0)

		self.num_mines_value = tk.Label(self.header, text=str(self.num_mines).ljust(8), font=c.TITLE_FONT)
		self.num_mines_value.grid(column=4, row=0)

		# key binding
		self.bind("<s>", self.start)

		self.grid_tiles = []
		self.background = tk.Frame(self, bg=c.BOARD_COLOR, width=c.WINDOW_WIDTH, height=c.WINDOW_HEIGHT)

		self.init_board()

		# buttons
		self.start_button = tk.Button(self, text="Start Game", command=self.start)
		self.start_button.grid(column=0, row=1)

		self.game_over_frame = tk.Frame(self.background, bg=c.BOARD_COLOR, width=c.WINDOW_WIDTH, height=c.WINDOW_HEIGHT)

		self.game_over = tk.Label(self.game_over_frame, text='GAME OVER', bg=c.BOARD_COLOR, justify=tk.CENTER, 
								  font=c.TILE_FONT, width=6, height=4)

		self.background.grid(column=0, row=2)

		# start the window running
		self.mainloop()

	def init_board(self):
		for row in range(self.board_size):
			row_tiles = []
			for col in range(self.board_size):
				tile = tk.Frame(self.background, bg=c.tile_color_dict[0],
								width=c.WINDOW_WIDTH / self.board_size, height=c.WINDOW_HEIGHT / self.board_size)
				tile.grid(row=row, column=col, padx=c.TILE_PADX, pady=c.TILE_PADY)
				value = tk.Label(tile, text='', bg=c.tile_color_dict[0], justify=tk.CENTER,
								 font=c.TILE_FONT, width=c.TILE_WIDTH, height=c.TILE_HEIGHT)
				value.grid(column=col, row=row)
				row_tiles.append(value)
			self.grid_tiles.append(row_tiles)

	def start(self, *args):
		while not (self.board.dead() or self.board.win()):
			if self.bot is None:
				row = int(input())
				col = int(input())
			else:
				row, col = self.bot.get_action(self.board.grid)
			time.sleep(0.25)
			self.board.click_tile(row, col)
			number = self.board.grid[row][col].number
			self.bot.tell(row, col, number)
			self.display_board(True)

		self.end_game()

	def display_board(self, clicked=True):
		for row in range(self.board_size):
			for col in range(self.board_size):
				if self.board.grid[row][col] is not None:
					if not clicked or self.board.grid[row][col].clicked:
						if self.board.grid[row][col].clicked:
							value = self.board.grid[row][col].number
							self.grid_tiles[row][col].configure(text=str(value))
						else:
							value = self.board.grid[row][col].number
							self.grid_tiles[row][col].configure(text=str(value), bg='#333333')
				else:
					self.grid_tiles[row][col].configure(text='')
		self.update_idletasks()

	def end_game(self):
		# Check if we've won or lost the game (-1 for lose, 1 for win)
		win_or_lose = 0
		if self.board.dead():
			win_or_lose = -1

		if self.board.win():
			win_or_lose = 1    

		self.display_board(False)

		self.game_over_frame.place(relheight=1 / 4, relwidth=3 / 4, relx=0.5, rely=0.5, anchor=tk.CENTER)
		# self.game_over_frame.attributes('-alpha', 0.5)
		self.game_over_frame.lift()
		if win_or_lose == -1:
			self.game_over.configure(text='GAME OVER')

		if win_or_lose == 1:
			self.game_over.configure(text='YOU WON! :)')
		
		self.game_over.place(relheight=1, relwidth=1, relx=0.5, rely=0.5, anchor=tk.CENTER)

		self.bind("<s>", self.start)
		self.start_button["state"] = "normal"

		del self.board

	def button_click(self, row, col):
		# wraps the 2 functions so that clicking a button can
		# actually click the tile and update how the board looks
		# print('clicking')
		self.board.click_tile(row, col)
		self.display_board()
