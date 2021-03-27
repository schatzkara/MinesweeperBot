from Board import Board
import keyboard


class Game:
    def __init__(self, size, mine_locations):
        self.size = size
        self.board = Board(size, mine_locations)
        self.init_board(mine_locations)
        self.board.display()

    def init_board(self, mine_locations):     
        self.board.init_grid(mine_locations)

    def get_board(self):
        return self.board

    def click_tile(self, row, col):
        self.board.click_tile(row, col)
        # self.board.display()

    # def play(self):
    #     while not self.game_over():
    #         self.click_tile()

    def game_over(self):
        return self.board.dead()


if __name__ == "__main__":
    g = Game(4, 2)
    g.play()
    # while not g.get_board().dead():
    #     g.take_turn()
