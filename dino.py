import os
import pygame
from pygame.sprite import Sprite, spritecollide
from time import sleep




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

		# Set the starting postition on the middle of the lvl 1 platform
		self.rect.x = 910
		self.rect.y = -self.settings.dino_height # Dino is not visible until Play button is clicked, falls from the sky.

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
		""" Update Dino position and detect collisions with other objects"""


		## Collisions
		# Ground
		ground_hit_list = spritecollide(self, self.dr_game.grounds, False)

		for g in ground_hit_list:
			self.movey = 0 # Stop moving Y on collision with ground
			self.rect.bottom = g.rect.top
			self.is_jumping = False # Stop jumping on collision with ground


		#  Platforms
		platform_hit_list = spritecollide(self, self.dr_game.platforms, False)
		for p in platform_hit_list:
			self.movey = 0
			self.is_jumping = False

			# Approach from below
			if self.rect.bottom <= p.rect.bottom:
				self.rect.bottom = p.rect.top
			else:
				self.is_jumping = True
				self.movey += self.settings.dino_gravity


		# Coins
		coin_hit_list = pygame.sprite.spritecollide(self, self.dr_game.coins, False)

		for c in coin_hit_list.copy():  # We use a copy of the list in order to be able to remove elements in the for loop
			self.dr_game.coins.remove(c)
			# Update the new scoring information.
			self.dr_game.stats.score += 1
			self.dr_game.sb.prep_score() 

			if len(self.dr_game.coins) == 0:
				self.dr_game._create_coins() # Spawn a new series of coins when the coin list is exhausted


		# Enemies
		enemy_hit_list = pygame.sprite.spritecollide(self, self.dr_game.enemies, False)

		for e in enemy_hit_list.copy():
			if self.dr_game.stats.dinos_left > 0:

				# Decrease dino_limit
				self.dr_game.stats.dinos_left -= 1

				# Pause the game before setting the Dino back at the start position.
				sleep(0.5)
				self._restart()
				self.dr_game.sb.prep_score() # Update score / health display

			elif self.dr_game.stats.dinos_left == 0:
				# set the game to a non active state
				self.dr_game.stats.game_active = False

				# Show the mouse cursor again
				pygame.mouse.set_visible(True)


		# Screen Edges
		if self.rect.right >= self.screen_rect.right:
			self.rect.x = self.screen_rect.left

		elif self.rect.left <= 0:
			self.rect.x = 0
		## END Collisions


		## Movement
		# Jump
		if self.is_jumping and self.is_falling is False:
			self.is_falling = True
			self.movey -= self.settings.dino_jump_height


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


		self.rect.x += self.movex
		self.rect.y += self.movey



	def _restart(self):
		""" Set the dino back to the starting position """
		self.rect.x = 910
		self.rect.y = -self.settings.dino_height



	def blitme(self):
		""" Draw the dino at the current position """
		self.screen.blit(self.image, self.rect)



