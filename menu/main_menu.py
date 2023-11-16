### Logic of the main menu ###

from game import Game


class Main_menu:

    def __init__(self, game):
        self.level_selected = None
        self.start_game = False
        self.levels = game.levels

        pass

    def update_level(self, level):
        self.level_selected = level

    def launch_game(self, game):
        if self.start_game:
            game.cursor = self.level_selected
            game.stage = "Launched"
