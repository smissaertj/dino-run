import pygame
from pygame.sprite import Sprite

class Ground(Sprite):
	""" A class to manage platforms int the game the dino can travel to """

	def __init__(self, dr_game): 

		super().__init__()

		self.screen = dr_game.screen
		self.settings = dr_game.settings
	

		self.image = self.settings.ground_img
		self.rect = self.image.get_rect()

		# Start each tile at the bottom
		self.rect.x = self.settings.screen_width - self.rect.width
		self.rect.y = self.settings.screen_height- self.rect.height