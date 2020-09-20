class GameStats():
	""" Track statistics and game state """

	def __init__(self, dr_game):

		self.settings = dr_game.settings
		self.reset_stats()

		# Set an inctive state for the game
		self.game_active = False


	def reset_stats(self):
		""" Initialize stats that change during gameplay """

		self.dinos_left = self.settings.dino_limit