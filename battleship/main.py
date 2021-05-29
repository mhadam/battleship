from battleship.board import Board
from battleship.game import Game, Player
from battleship.ship import Ship

if __name__ == "__main__":
    dimensions = (10, 10)
    p1_board = Board(dimensions, {Ship(1, 1, 9, "h"), Ship(3, 5, 4, "v")})
    p1 = Player(p1_board)

    p2_board = Board(dimensions, {Ship(1, 2, 2, "v"), Ship(5, 6, 2, "h")})
    p2 = Player(p2_board)

    game = Game(p1, p2, dimensions)
    game.p1_move(3, 1)
    game.p1_move(3, 7)
    #
    game.p2_move(1, 1)
    # win
    game.p1_move(1, 2)
    game.p1_move(1, 3)
    game.p1_move(5, 6)
    game.p1_move(6, 6)
    print(f"winner: {game.get_winner()}")
    game.print_game()
