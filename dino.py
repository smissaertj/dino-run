import os
import pygame
from pygame.sprite import Sprite




class Dino(Sprite):
	""" Class to manage the player controlled dinosaur. """

	def __init__(self, dr_game):
		""" Initialize the dino and set starting image and position """

		super(Dino, self).__init__()

		self.screen = dr_game.screen
		self.screen_rect = dr_game.screen.get_rect()
		self.settings = dr_game.settings

		self.movex = 0
		self.movey = 0
		self.frame = 0
		
		# Set the starting image.
		self.image_idle = pygame.transform.scale(pygame.image.load('img/dino_idle.png'), self.settings.dino_size)
		self.image = self.image_idle
		
		# Get the img rect
		self.rect = self.image.get_rect()

		# Set the starting postition in the bottom left of the screen
		self.rect.bottomleft = self.screen_rect.bottomleft

		# Create a list of images for the run animation
		self.images = [] 
		for i in range(1,8):
			img = pygame.transform.scale(pygame.image.load(os.path.join('img/dinorun', 'dino_run_' + str(i) + '.png')), self.settings.dino_size)
			self.images.append(img)
	

	def control(self, x, y):
		""" Control Dino movement """

		self.movex += x
		self.movey += y


	def update(self):
		""" Update Dino position """

		self.rect.x = self.rect.x + self.movex
		self.rect.y = self.rect.y + self.movey


		# Move left
		if self.movex < 0:
			self.frame += 1
			if self.frame > 3 * self.settings.ani:
				self.frame = 0
			self.image = pygame.transform.flip(self.images[self.frame // self.settings.ani], True, False)


		# Move right
		if self.movex > 0:
			self.frame += 1
			if self.frame > 3 * self.settings.ani:
				self.frame = 0
			self.image = self.images[self.frame // self.settings.ani]
		

	def blitme(self):
		""" Draw the dino at the current position """

		self.screen.blit(self.image, self.rect)



