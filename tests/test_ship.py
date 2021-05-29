from battleship.ship import Ship


def test_ships_vertical():
    ship = Ship(1, 1, 3, "v")

    assert ship.positions == {(1, 1), (1, 2), (1, 3)}


def test_ships_horizontal():
    ship = Ship(1, 1, 3, "h")

    assert ship.positions == {(1, 1), (2, 1), (3, 1)}
