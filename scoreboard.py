import pygame.font

class Scoreboard:
	""" Report scoring information """

	def __init__(self, dr_game):
		""" Set attributes """

		self.screen = dr_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = dr_game.settings
		self.stats = dr_game.stats


		# Font settings
		self.text_color = self.settings.score_txt_color
		self.font = pygame.font.SysFont(None, 48)


		# Prepare the Score image
		self.prep_score()


	def prep_score(self):
		""" Turn the score into an image """
		score_str = str(f'Health: {self.stats.dinos_left}  |  Coins: {self.stats.score}')
		self.score_image = self.font.render(score_str, True, self.text_color)


		# Display the score in the top right corner of the screen
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20


	def show_score(self):
		""" Draw the score to the screen """
		self.screen.blit(self.score_image, self.score_rect)