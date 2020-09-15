import os
import pygame
from pygame.sprite import Sprite, spritecollide




class Coin(Sprite):
	""" Class to manage the coins """

	def __init__(self, dr_game, yloc):
		""" Initalize a coin and set its position """

		super().__init__()

		self.dr_game = dr_game
		self.screen = dr_game.screen
		self.screen_rect = dr_game.screen.get_rect()
		self.settings = dr_game.settings


		# Set the starting frame
		self.frame = 0

		# Create a list of images for the coin animation
		self.images = []

		for i in range(1,16):
			img = pygame.transform.scale(pygame.image.load(os.path.join('img/coin/coin_' + str(i) + '.png')), (self.settings.coin_width, self.settings.coin_height))
			self.images.append(img)


		# Set the starting image
		self.image = self.images[self.frame]
		# Get the img rect
		self.rect = self.image.get_rect()

		# set a starting position
		self.rect.y = yloc


	def update(self):

		self.frame += 1
		if self.frame >= 15 * self.settings.ani:
			self.frame = 0
		self.image = self.images[self.frame // self.settings.ani]