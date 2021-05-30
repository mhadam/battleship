from dataclasses import dataclass, field
from typing import Set, Mapping, Tuple, Optional, Iterable

from battleship.ship import Ship


@dataclass
class Board:
    dimensions: Tuple[int, int]
    ships: Set[Ship]
    positions: Mapping[Tuple[int, int], Ship] = field(init=False)

    def __post_init__(self):
        self.positions = self.calculate_positions()

    def validate_position(self, x: int, y: int):
        if x >= self.dimensions[0] or y >= self.dimensions[1]:
            raise RuntimeError("exceeds size")
        if x < 0 or y < 0:
            raise RuntimeError("cannot be a negative coordinate")

    def calculate_positions(self) -> Mapping[Tuple[int, int], Ship]:
        positions = {}
        for ship in self.ships:
            for position in ship.positions:
                self.validate_position(*position)
                if position in positions:
                    raise RuntimeError(
                        f"overlapping ships at {position} between {ship} and {positions.get(position)}"
                    )
                positions[position] = ship
        return positions


class DamageRecord:
    def __init__(self, ships: Set[Ship]):
        self.ships = ships
        self.floating_positions_by_ship = {ship: set(ship.positions) for ship in ships}
        self.ship_by_floating_position = {
            position: ship for ship in ships for position in ship.positions
        }

    def hit(self, x: int, y: int) -> Optional[Ship]:
        try:
            position = (x, y)
            ship = self.ship_by_floating_position[position]
            self.floating_positions_by_ship[ship].remove(position)
            self.ship_by_floating_position.pop(position)
            return ship
        except KeyError:
            pass

    def get_floating_positions(self, ship: Ship) -> Iterable[Tuple[int, int]]:
        return self.floating_positions_by_ship.get(ship, [])

    def is_all_hit(self) -> bool:
        return len(self.ship_by_floating_position) == 0
