# Logic of the main menu #

from game import Game


class MainMenu:
    """
    The Main Menu manages the selection of the levels and launches the game.
    It is rended on the scren by the draw_main_menu object.
    """
    def __init__(self):
        """
        The __init__ method initiliases the variables that will be used to manage the choosing of the level
        """
        self.level_selected = None
        self.start_game = False
        self.sound = False
        self.level_cursor = 0

    def update_level(self, level):
        """
        This method is used to change the selected level

        Parameters :
        level (Level): the level you want to select
        """

        self.level_selected = level

    def launch_game(self, game):
        """
        This method is used to change the state of the game to Launched, which launches the selected level

        Parameters:
        game (Game): the current game
        """

        if self.start_game:
            game.cursor = self.level_selected
            game.stage = "Launched"
            game.load_interface()

    def increase_cursor(self, game):
        """
        This method is used to increase the view of levels selected

        Parameters: 
        game (Game): the current game
        """
        n = len(game.levels) // 10
        
        if self.level_cursor < n:
            self.level_cursor += 1
        else :
            self.level_cursor = 0

    def increase_cursor(self, game):
        """
        This method is used to increase the view of levels selected

        Parameters: 
        game (Game): the current game
        """
        n = len(game.levels) // 10

        if self.level_selected > 0:
            self.level_cursor -= 1
        else :
            self.level_cursor = n
