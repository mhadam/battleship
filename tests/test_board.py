import pytest

from battleship.board import Board, DamageRecord
from battleship.ship import Ship


def test_misses_ship():
    ships = {Ship(1, 1, 2, "v")}
    record = DamageRecord(ships)

    ship = record.hit(3, 3)

    assert ship is None


def test_hitting_ship():
    expected = Ship(1, 1, 2, "v")
    ships = {expected}
    record = DamageRecord(ships)

    ship = record.hit(1, 1)

    assert ship == expected


def test_hits_still_left():
    ships = {Ship(1, 1, 3, "v")}
    record = DamageRecord(ships)

    assert not record.is_all_hit()


def test_all_hit():
    ships = {Ship(1, 1, 2, "v")}
    record = DamageRecord(ships)

    record.hit(1, 1)
    record.hit(1, 2)

    assert record.is_all_hit()


def test_validate_exceeds_y_grid():
    dimensions = (1, 1)

    with pytest.raises(RuntimeError) as e_info:
        ships = {Ship(1, 1, 2, "v")}
        _ = Board(dimensions, ships)

    assert "exceeds size" == str(e_info.value)


def test_validate_exceeds_x_grid():
    dimensions = (1, 1)

    with pytest.raises(RuntimeError) as e_info:
        ships = {Ship(1, 1, 2, "h")}
        _ = Board(dimensions, ships)

    assert "exceeds size" == str(e_info.value)


def test_validate_negative_x_grid():
    dimensions = (1, 1)

    with pytest.raises(RuntimeError) as e_info:
        ships = {Ship(-5, 0, 2, "h")}
        _ = Board(dimensions, ships)

    assert "cannot be a negative coordinate" == str(e_info.value)


def test_validate_negative_y_grid():
    dimensions = (1, 1)

    with pytest.raises(RuntimeError) as e_info:
        ships = {Ship(0, -5, 2, "h")}
        _ = Board(dimensions, ships)

    assert "cannot be a negative coordinate" == str(e_info.value)


def test_overlapping_ships():
    dimensions = (10, 10)

    with pytest.raises(RuntimeError) as e_info:
        ships = {Ship(1, 1, 3, "h"), Ship(2, 0, 3, "v")}
        _ = Board(dimensions, ships)

    assert str(e_info.value).startswith("overlapping ships at (2, 1)")


def test_get_floating_positions():
    ship = Ship(1, 1, 2, "v")
    ships = {ship}
    record = DamageRecord(ships)

    positions = record.get_floating_positions(ship)

    assert positions == {(1, 1), (1, 2)}
