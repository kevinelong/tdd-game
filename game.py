from board import Board
from player import Player
from treasure import Treasure
from position import Position


class Game:
    def __init__(self, width=9, height=9):
        self.board = Board(width, height)
        self.player = Player()
        self.board.place_center(self.player)
        self.board.place_random(Treasure())
        self.commands = {
            "left": self.turn_left,
            "right": self.turn_right,
            "forward": self.forward,
            "backward": self.backward,
        }

    def execute(self, command):
        if command in self.commands:
            self.commands[command]()
        else:
            print("unknown command: " + command)

    def get_map(self):
        return self.board.get_state()

    def turn_right(self):
        self.player.direction = (self.player.direction + 1) % 4
        self.board.redraw(self.player)

    def turn_left(self):
        self.player.direction = (self.player.direction - 1) % 4
        self.board.redraw(self.player)

    def apply_position(self, p):
        if self.board.is_on_board(p):
            self.board.move(self.player, p)

    def forward(self):
        self.apply_position([
                                lambda c: Position(c.position.x, c.position.y - 1),
                                lambda c: Position(c.position.x + 1, c.position.y),
                                lambda c: Position(c.position.x, c.position.y + 1),
                                lambda c: Position(c.position.x - 1, c.position.y),
                            ][self.player.direction](self.player))

    def backward(self):
        self.apply_position([
                                lambda c: Position(c.position.x, c.position.y + 1),
                                lambda c: Position(c.position.x - 1, c.position.y),
                                lambda c: Position(c.position.x, c.position.y - 1),
                                lambda c: Position(c.position.x + 1, c.position.y),
                            ][self.player.direction](self.player))

    def check_collisions(self):
        for item in self.board._content:
            if item != self.player and \
                    item.position.x == self.player.position.x and \
                    item.position.y == self.player.position.y:
                self.player.score += item.value
                self.board.place_random(Treasure())
                self.board.remove(item)
                break
