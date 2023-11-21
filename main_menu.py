# Logic of the main menu #

from game import Game


class MainMenu:

    def __init__(self):
        self.level_selected = None
        self.start_game = False
        self.sound = False

    def update_level(self, level):
        self.level_selected = level

    def launch_game(self, game):
        if self.start_game:
            game.cursor = self.level_selected
            game.stage = "Launched"
            game.load_interface()

    def launch_level_editor(self, game):
        game.stage = "Level Editor"
