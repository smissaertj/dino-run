import pygame
from pygame.sprite import Sprite


class Platform(Sprite):
	""" a class to manage platforms """

	def __init__(self, dr_game, yloc):

		super().__init__()

		self.screen = dr_game.screen
		self.settings = dr_game.settings

		self.image = self.settings.platform_img
		self.rect = self.image.get_rect()


		self.rect.y = yloc #self.settings.screen_height - (256 + 184)



