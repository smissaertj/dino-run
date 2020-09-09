class Settings:
	""" Class to define all settings for the game """

	def __init__(self):
		""" Initialize game settings """

		# Screen settings
		self.screen_width = 1920
		self.screen_height = 1080
		self.bg_color = (0, 0, 0)
		self.fps = 40
		self.ani = 6  # Animation Cycles

		# Dino settings
		self.dino_steps = 10
		self.dino_size = (184, 196)
