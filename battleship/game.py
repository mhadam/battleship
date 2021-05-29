from typing import Optional, Tuple, Iterable, MutableMapping

from battleship.board import Board, DamageRecord


class Player:
    def __init__(self, board: Board):
        self.guesses = set()
        self.__board = board
        self.__damage_record = DamageRecord(board.ships)

    def opponent_move(self, x: int, y: int):
        if (x, y) in self.guesses:
            raise RuntimeError("already guessed")
        self.guesses.add((x, y))
        self.damage_record.hit(x, y)

    @property
    def is_defeated(self) -> bool:
        return self.damage_record.is_all_hit()

    @property
    def board(self) -> Board:
        return self.__board

    @property
    def damage_record(self) -> DamageRecord:
        return self.__damage_record


class Game:
    def __init__(self, p1: Player, p2: Player, dimensions: Tuple[int, int]):
        self.p1 = p1
        self.p2 = p2
        self.dimensions = dimensions

    def p1_move(self, x: int, y: int):
        self.p2.opponent_move(x, y)

    def p2_move(self, x: int, y: int):
        self.p1.opponent_move(x, y)

    def get_winner(self) -> Optional[int]:
        if self.p1.is_defeated and self.p2.is_defeated:
            return 0
        if self.p1.is_defeated:
            return 2
        if self.p2.is_defeated:
            return 1

    def print_game(self):
        grid: MutableMapping[Tuple[int, int], str] = {}
        for position, _ in self.p1.board.positions.items():
            grid[position] = "1"
        for position, _ in self.p2.board.positions.items():
            grid[position] = "2"
        for ship in self.p1.board.ships:
            floating = self.p1.damage_record.floating_positions_by_ship[ship]
            hit = ship.positions.difference(floating)
            for position in hit:
                grid[position] = "h"
        for ship in self.p2.board.ships:
            floating = self.p2.damage_record.floating_positions_by_ship[ship]
            hit = ship.positions.difference(floating)
            for position in hit:
                grid[position] = "h"
        x_dim, y_dim = self.dimensions
        for y in range(y_dim):
            for x in range(x_dim):
                try:
                    print(grid[x, y], end="")
                except KeyError:
                    print(".", end="")
            if y < y_dim - 1:
                print()
