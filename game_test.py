"""
Requirements:
SETUP:
    Show Map of specified width and height, default to 9x9.
    Show Player center of the Map.
    Place and show a treasure on the map in random position,
     that is not on the player's position.

PLAY:
    Ask user to if the they want to:
        A - Rotate-Left
        D - Rotate-Right
        W - Move-Straight
        S - Move-Backward
    Rotate or move player Move player in specified direction.
    Reject moves that would go off the game board.
    if player and treasure collide then:
        Add treasure's value to score.
        Remove treasure from map.
        Add a new one in an empty position.
"""
from game import Game

# Tests
assert Game() is not None
assert Game().board._width == 9
assert Game().board._height == 9
assert Game().player.position.x == 4
assert Game().player.position.y == 4
assert Game().player.direction == 0

g = Game()
g.turn_right()
assert g.player.direction == 1
g.turn_right()
g.turn_right()
g.turn_right()
assert g.player.direction == 0

map = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '^', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.']
]

result = g.get_map()
# print(result)
assert len(map) == len(result)
assert len(map[0]) == len(result[0])
