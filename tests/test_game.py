import pytest

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


def test_opponent_move_guessed():
    dims = (5, 5)
    s1 = {Ship(1, 1, 3, "v")}
    p1 = Player(Board(dims, s1))

    with pytest.raises(RuntimeError, match="already guessed"):
        p1.opponent_move(1, 1)
        p1.opponent_move(1, 1)


def test_player_is_defeated():
    dims = (5, 5)
    s1 = {Ship(1, 1, 3, "v")}
    p1 = Player(Board(dims, s1))

    for i in range(3):
        p1.opponent_move(1, 1 + i)

    assert p1.is_defeated
