import pygame
from pygame.sprite import Sprite, spritecollide



class Ennemy(Sprite):
	""" Class to represent a single ennemy """

	def __init__(self, dr_game):
		""" Initialize the ennemy and set a starting position """

		super().__init__()

		self.screen = dr_game.screen
		self.settings = dr_game.settings


		# Set the ennemy image and its rect attribute
		self.image = self.settings.ennemy_img
		self.rect = self.image.get_rect()


		# Start the ennemy in the bottom right corner of the screen
		self.rect.x = self.settings.screen_width - self.rect.width
		self.rect.y = self.settings.screen_height - (1.75 * self.settings.ground_height)


		# Store the exact horizontal position
		self.x = float(self.rect.x)


	def update(self):
		""" Move the row of ennemies to the left """
		self.x += (self.settings.ennemy_speed * self.settings.ennemy_direction)
		self.rect.x = self.x




