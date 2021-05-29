from typing import Set, Tuple, Iterable


class Ship:
    def __init__(self, x, y, length, orientation):
        self.x = x
        self.y = y
        self.length = length
        self.orientation = orientation
        self.__positions = set(self.calculate_positions())

    def get_position(self) -> Tuple[int, int]:
        return self.x, self.y

    @property
    def positions(self) -> Set[Tuple[int, int]]:
        return self.__positions

    def calculate_positions(self) -> Iterable[Tuple[int, int]]:
        if self.orientation == "v":
            return ((self.x, self.y + i) for i in range(self.length))
        if self.orientation == "h":
            return ((self.x + i, self.y) for i in range(self.length))
        raise RuntimeError(f"invalid orientation {self.orientation}")
