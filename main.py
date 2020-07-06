"""
A Text interface not so much as a test but to prove the game is playable.
This must be executed from the terminal,
 or a debug configuration with the execution option,
  "Emulate terminal in output console" set to True
"""
import getch
import clear_screen
from game import Game


class TextInterface:
    def __init__(self, game):
        self.game = game
        self.commands = {'quit': self.stop}
        self.key_command_map = {}
        self.map(['q', 'Q', 'x', 'X'], 'quit')
        self.map(['w', 'W', '[A'], 'forward')
        self.map(['a', 'A', '[D'], 'left')
        self.map(['d', 'D', '[C'], 'right')
        self.map(['s', 'S', '[B'], 'backward')
        self.playing = True

    def map(self, key_list, command):
        for k in key_list:
            self.key_command_map[k] = command

    def draw(self):
        s = self.game.board.get_state()
        clear_screen.clear()
        for y in range(len(s)):
            print("  ".join(s[y]))
        print(self.game.player.score)

    def execute(self, command):
        self.commands[command]() if command in self.commands else self.game.execute(command)

    def user_input(self):
        k = getch.getch()
        if k == '[' or k == 27:
            k = k + getch.getch()
        if k in self.key_command_map:
            self.execute(self.key_command_map[k])

    def start(self):
        while self.playing:
            self.draw()
            self.user_input()
            self.game.check_collisions()

    def stop(self):
        self.playing = False


TextInterface(Game(9, 9)).start()
