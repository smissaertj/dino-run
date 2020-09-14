import os
import pygame
from pygame.sprite import Sprite, spritecollide




class Dino(Sprite):
	""" Class to manage the player controlled dinosaur. """

	def __init__(self, dr_game):
		""" Initialize the dino and set starting image and position """

		super().__init__()

		self.dr_game = dr_game
		self.screen = dr_game.screen
		self.screen_rect = dr_game.screen.get_rect()
		self.settings = dr_game.settings

		self.movex = 0
		self.movey = 0
		self.frame = 0

		self.is_jumping = True # Turn gravity on
		self.is_falling = True
		
		# Set the starting image.
		self.image_idle = self.settings.dino_img
		self.image = self.image_idle
		
		# Get the img rect
		self.rect = self.image.get_rect()

		# Set the starting postition in the bottom left of the screen
		self.rect.x = self.screen_rect.left
		self.rect.y = self.screen_rect.bottom - self.settings.ground_height

		# Create a list of images for the run animation
		self.images = [] 
		for i in range(1,8):
			img = pygame.transform.scale(pygame.image.load(os.path.join('img/d_run', str(i) + '.png')), (self.settings.dino_width, self.settings.dino_height))
			self.images.append(img)





	def gravity(self):
		if self.is_jumping:
			self.movey += self.settings.dino_gravity


	def jump(self):
		if self.is_jumping is False:
			self.is_falling = False
			self.is_jumping = True


	def control(self, x, y):
		""" Control Dino movement """

		self.movex += x


	def update(self):
		""" Update Dino position """

		# Move left
		if self.movex < 0:
			self.is_jumping = True # Turn gravity on upon moving
			self.frame += 1
			if self.frame > 3 * self.settings.ani:
				self.frame = 0
			self.image = pygame.transform.flip(self.images[self.frame // self.settings.ani], True, False)


		# Move right
		if self.movex > 0:
			self.is_jumping = True # Turn gravity on upon moving
			self.frame += 1
			if self.frame > 3 * self.settings.ani:
				self.frame = 0
			self.image = self.images[self.frame // self.settings.ani]
		

		# Collisions
		ground_hit_list = spritecollide(self, self.dr_game.grounds, False)
		platform_hit_list = spritecollide(self, self.dr_game.platforms, False)
		#print(ground_hit_list)
		#print(platform_hit_list)

		for g in ground_hit_list:
			self.movey = 0 # Stop moving Y on collision with ground
			self.rect.bottom = g.rect.top
			self.is_jumping = False # Stop jumping on collision with ground

		# Jump
		if self.is_jumping and self.is_falling is False:
			self.is_falling = True
			self.movey -= self.settings.dino_jump_height


		self.rect.x += self.movex
		self.rect.y += self.movey


	def blitme(self):
		""" Draw the dino at the current position """

		self.screen.blit(self.image, self.rect)



