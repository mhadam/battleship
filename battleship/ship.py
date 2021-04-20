from typing import Set, Tuple


class Ship:
    def __init__(self, x, y, length, orientation):
        self.x = x
        self.y = y
        self.length = length
        self.orientation = orientation

    def get_position(self) -> Tuple[int, int]:
        return self.x, self.y

    def get_positions(self) -> Set[Tuple[int, int]]:
        if self.orientation == "v":
            return {(self.x, self.y+i) for i in range(self.length)}
        if self.orientation == "h":
            return {(self.x+i, self.y) for i in range(self.length)}
        raise RuntimeError(f"invalid orientation {self.orientation}")
