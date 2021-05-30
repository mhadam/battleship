import pytest

from battleship.ship import Ship


def test_ships_vertical():
    ship = Ship(1, 1, 3, "v")

    assert ship.positions == {(1, 1), (1, 2), (1, 3)}


def test_ships_horizontal():
    ship = Ship(1, 1, 3, "h")

    assert ship.positions == {(1, 1), (2, 1), (3, 1)}


def test_get_position():
    ship = Ship(1, 1, 3, "h")

    assert ship.get_position() == (1, 1)


def test_invalid_orientation():
    with pytest.raises(RuntimeError, match="invalid orientation x"):
        _ = Ship(1, 1, 3, "x")
