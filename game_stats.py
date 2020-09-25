class GameStats():
	""" Track statistics and game state """

	def __init__(self, dr_game):
		""" Initialize game statistics and state """

		self.settings = dr_game.settings
		self.reset_stats()

		# Set an inctive state for the game
		self.game_active = False

		# Initialize the score
		self.score = 0


	def reset_stats(self):
		""" Initialize stats that change during gameplay """

		self.dinos_left = self.settings.dino_limit
		self.score = 0