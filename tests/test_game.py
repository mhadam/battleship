from battleship.board import Board
from battleship.game import Player
from battleship.ship import Ship


def test_player():
    dims = (5, 5)
    s1 = {Ship(1, 1, 3, "v")}
    p1 = Player(Board(dims, s1))

    for i in range(3):
        p1.opponent_move(1, 1 + i)

    assert list(p1.text) == [
        [".", ".", ".", ".", "."],
        [".", "h", ".", ".", "."],
        [".", "h", ".", ".", "."],
        [".", "h", ".", ".", "."],
        [".", ".", ".", ".", "."],
    ]
