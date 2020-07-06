import random
from position import Position


class Board:
    def __init__(self, width=9, height=9):
        self._grid = []
        self._width = width
        self._height = height
        self._content = []
        for y in range(self._height):
            line = []
            for x in range(self._width):
                line.append('.')
            self._grid.append(line)

    def _set(self, position, symbol):
        self._grid[position.y][position.x] = symbol

    def redraw(self, item):
        self._set(item.position, item.get_symbol())

    def remove(self, item):
        self._content.remove(item)

    def move(self, item, target_position):
        self._grid[item.position.y][item.position.x] = '.'
        item.position = target_position
        self.redraw(item)

    def place(self, item):
        self.redraw(item)
        self._content.append(item)

    def place_center(self, item):
        item.position = Position(self._width // 2, self._height // 2)
        self.place(item)

    def random_position(self):
        return Position(random.randint(0, self._width - 1), random.randint(0, self._height - 1))

    def place_random(self, item, limit=999):
        tries = 0
        p = self.random_position()
        while self.is_occupied(p) and tries < limit:
            p = self.random_position()
            tries += 1
        item.position = p
        self.place(item)

    def is_occupied(self, position):
        return self._grid[position.y][position.x] != '.'

    def get_state(self):
        return self._grid

    def is_on_board(self, position):
        return position.x >= 0 and \
               position.y >= 0 and \
               position.x + 1 <= self._width and \
               position.y + 1 <= self._height
