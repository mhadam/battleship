import pytest

from battleship.board import Board
from battleship.game import Player, Game
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


def test_no_winner():
    dims = (5, 5)
    s1 = {Ship(1, 1, 3, "v")}
    p1 = Player(Board(dims, s1))
    s2 = {Ship(1, 1, 3, "v")}
    p2 = Player(Board(dims, s2))
    game = Game(p1, p2, dims)

    result = game.get_winner()

    assert result is None


def test_p1_winner():
    dims = (5, 5)
    s1 = {Ship(1, 1, 3, "v")}
    p1 = Player(Board(dims, s1))
    s2 = {Ship(1, 1, 3, "v")}
    p2 = Player(Board(dims, s2))
    game = Game(p1, p2, dims)

    game.p1_move(1, 1)
    game.p1_move(1, 2)
    game.p1_move(1, 3)
    result = game.get_winner()

    assert result == 1


def test_p2_winner():
    dims = (5, 5)
    s1 = {Ship(1, 1, 3, "v")}
    p1 = Player(Board(dims, s1))
    s2 = {Ship(1, 1, 3, "v")}
    p2 = Player(Board(dims, s2))
    game = Game(p1, p2, dims)

    game.p2_move(1, 1)
    game.p2_move(1, 2)
    game.p2_move(1, 3)
    result = game.get_winner()

    assert result == 2


def test_players_draw():
    dims = (5, 5)
    s1 = {Ship(1, 1, 3, "v")}
    p1 = Player(Board(dims, s1))
    s2 = {Ship(1, 1, 3, "v")}
    p2 = Player(Board(dims, s2))
    game = Game(p1, p2, dims)

    game.p2_move(1, 1)
    game.p2_move(1, 2)
    game.p2_move(1, 3)
    game.p1_move(1, 1)
    game.p1_move(1, 2)
    game.p1_move(1, 3)
    result = game.get_winner()

    assert result == 0


def test_game_text():
    dims = (3, 3)
    s1 = {Ship(0, 0, 3, "v")}
    p1 = Player(Board(dims, s1))
    s2 = {Ship(0, 0, 3, "v")}
    p2 = Player(Board(dims, s2))
    game = Game(p1, p2, dims)

    p1_lines = game.p1_lines()
    p2_lines = game.p2_lines()

    assert list(p1_lines) == [["s", ".", "."], ["s", ".", "."], ["s", ".", "."]]
    assert list(p2_lines) == [["s", ".", "."], ["s", ".", "."], ["s", ".", "."]]
