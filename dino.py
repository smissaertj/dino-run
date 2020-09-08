import pygame


class Dino:
	""" Class to manage the player controlled dinosaur. """

	def __init__(self, dr_game):
		""" Initialize the dino and set starting position """
		
		self.screen = dr_game.screen
		self.screen_rect = dr_game.screen.get_rect()


		# Load the dino img and get its rect.
		self.image = pygame.image.load('img/dino_idle.png')
		self.rect = self.image.get_rect()

		# Position the dino at the bottom left of the screen
		self.rect.bottomleft = self.screen_rect.bottomleft



	def blitme(self):
		""" Draw the dino at the current position """
		self.screen.blit(self.image, self.rect)