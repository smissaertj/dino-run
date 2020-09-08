import pygame
from pygame.sprite import Sprite


class Dino(Sprite):
	""" Class to manage the player controlled dinosaur. """

	def __init__(self, dr_game):
		""" Initialize the dino and set starting position """

		super(Dino, self).__init__()

		self.screen = dr_game.screen
		self.screen_rect = dr_game.screen.get_rect()
		self.image_idle = pygame.image.load('img/dino_idle.png')


		# Running animation
		self.images = []
		self.images.append(pygame.image.load('img/dino_run_1.png'))
		self.images.append(pygame.image.load('img/dino_run_2.png'))
		self.images.append(pygame.image.load('img/dino_run_3.png'))
		self.images.append(pygame.image.load('img/dino_run_4.png'))
		self.images.append(pygame.image.load('img/dino_run_5.png'))
		self.images.append(pygame.image.load('img/dino_run_6.png'))
		self.images.append(pygame.image.load('img/dino_run_7.png'))
		self.images.append(pygame.image.load('img/dino_run_8.png'))


		# Jump animation
		self.images_jump = []
		self.images_jump.append(pygame.image.load('img/dino_jump_1.png'))
		self.images_jump.append(pygame.image.load('img/dino_jump_2.png'))
		self.images_jump.append(pygame.image.load('img/dino_jump_3.png'))
		self.images_jump.append(pygame.image.load('img/dino_jump_4.png'))
		self.images_jump.append(pygame.image.load('img/dino_jump_5.png'))
		self.images_jump.append(pygame.image.load('img/dino_jump_6.png'))
		self.images_jump.append(pygame.image.load('img/dino_jump_7.png'))
		self.images_jump.append(pygame.image.load('img/dino_jump_8.png'))
		self.images_jump.append(pygame.image.load('img/dino_jump_9.png'))
		self.images_jump.append(pygame.image.load('img/dino_jump_10.png'))
		self.images_jump.append(pygame.image.load('img/dino_jump_11.png'))
		self.images_jump.append(pygame.image.load('img/dino_jump_12.png'))
		self.images_jump.append(pygame.image.load('img/dino_jump_13.png'))

		

		# Index value to get the image from the array
		# Initially it is 0 
		self.index = 0

		#now the image that we will display will be the index from the image array 
		self.image = self.image_idle #self.images[self.index]

		# Get the img rect
		self.rect = self.image.get_rect()

		# Position the dino at the bottom left of the screen
		self.rect.bottomleft = self.screen_rect.bottomleft


		# Movement flag
		self.moving_right = False
		self.moving_left = False
		self.jump = False


		# Set a decimal value for the dino position
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)


	def update(self):
		""" Update the dino based on the movement flag """
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.index += 1
			self.rect.x += 20

			if self.index >= len(self.images):
				self.index = 0
			self.image = self.images[self.index]

		elif self.moving_left and self.rect.left > 0:
			self.index += 1
			self.rect.x -= 20

			if self.index >= len(self.images):
				self.index = 0
			self.image = self.images[self.index]


		elif self.jump:
			self.index += 1
			self.rect.y -= 2

			if self.index >= len(self.images_jump):
				self.index = 0
				self.rect.y = 0
			self.image = self.images_jump[self.index]

			

		else:
			self.image = self.image_idle


	def blitme(self):
		""" Draw the dino at the current position """
		self.screen.blit(self.image, self.rect)



