from battleship.ship import Ship


def test_ships_vertical():
    ship = Ship(1, 1, 3, "v")

    result = ship.get_positions()

    assert result == {(1, 1), (1, 2), (1, 3)}


def test_ships_horizontal():
    ship = Ship(1, 1, 3, "h")

    result = ship.get_positions()

    assert result == {(1, 1), (2, 1), (3, 1)}
