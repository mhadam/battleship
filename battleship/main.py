from typing import Set, Optional, Tuple, Mapping, Iterable

from battleship.ship import Ship


class Ships:
    def __init__(self, ships: Iterable[Ship], board_x: int, board_y: int):
        ships = set(ships)
        self.board_x = board_x
        self.board_y = board_y
        self.hits: Set[Ship] = set()
        self.okay: Set[Ship] = set(ships)
        self.ships: Set[Ship] = ships
        self.positions: Mapping[Tuple[int, int], Ship] = self.get_positions()

    def validate_position(self, x: int, y: int):
        if x >= self.board_x or y >= self.board_y:
            raise RuntimeError("exceeds size")

    def get_positions(self) -> Mapping[Tuple[int, int], Ship]:
        positions = {}
        for ship in self.ships:
            for position in ship.positions:
                if position in positions:
                    raise RuntimeError(f"overlapping ships between {ship} and {positions.get(position)}")
                self.validate_position(*position)
                positions[position] = ship
        return positions

    def hit(self, x: int, y: int) -> Optional[Ship]:
        try:
            ship = self.positions[(x, y)]
            if ship in self.okay:
                self.hits.add(ship)
                self.okay.remove(ship)
                return ship
            if ship in self.hits:
                raise RuntimeError("already hit")
        except KeyError:
            return

    def is_all_hit(self) -> bool:
        return len(self.okay) == 0


class Game:
    def __init__(self, p1_ships: Ships, p2_ships: Ships):
        self.p1_ships = p1_ships
        self.p2_ships = p2_ships
        self.p1_guesses: Set[Tuple[int, int]] = set()
        self.p2_guesses: Set[Tuple[int, int]] = set()

    def p1_play(self, x: int, y: int):
        if (x, y) in self.p1_guesses:
            raise RuntimeError("already guessed")
        self.p1_guesses.add((x, y))
        self.p2_ships.hit(x, y)

    def p2_play(self, x: int, y: int):
        if (x, y) in self.p2_guesses:
            raise RuntimeError("already guessed")
        self.p2_guesses.add((x, y))
        self.p1_ships.hit(x, y)

    def get_winner(self) -> Optional[int]:
        if self.p1_ships.is_all_hit():
            return 2
        if self.p2_ships.is_all_hit():
            return 1


if __name__ == '__main__':
    x, y = 10, 10
    p1_ships = Ships({Ship(1, 1, 9, 'h'), Ship(3, 5, 4, 'v')}, x, y)
    p2_ships = Ships({Ship(1, 2, 2, 'v'), Ship(5, 6, 2, 'h')}, x, y)
    game = Game(p1_ships, p2_ships)
    game.p1_play(3, 1)
    game.p1_play(3, 7)
    game.p2_play(1, 1)
    print(f"winner: {game.get_winner()}")
