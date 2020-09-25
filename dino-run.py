import sys
import pygame
from time import sleep

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ground import Ground
from platform import Platform
from coin import Coin
from dino import Dino
from ennemy import Ennemy



class DinoRun:
	""" Class to manage game assets and behaviour. """

	def __init__(self):
		""" Initialize the game and create game resouces. """

		pygame.init()
		self.settings = Settings()
		self.screen = self.settings.screen
		self.backdropbox = self.screen.get_rect()
		pygame.display.set_caption("Dino Run!")

		# Initialize Sprite Group lists to hold images
		self.grounds = pygame.sprite.Group()
		self.platforms = pygame.sprite.Group()
		self.coins = pygame.sprite.Group()
		self.ennemies = pygame.sprite.Group()

		# Create the ground, platform and coins outside of the main loop
		# to prevent them from being recreated over and over again in _update_screen(), slowing down the application over time.
		self._create_ground()
		self._create_platforms()
		self._create_coins()
		self._create_ennemy_row()

		# Create an instance to store game statistics before the Dino is spawned
		self.stats = GameStats(self)
		self.sb = Scoreboard(self)

		# Create the player controllable Dino
		self.dino = Dino(self)

		# Make the Play button
		self.play_button = Button(self, "Play")

		# Get the pygame clock for handling FPS
		self.clock = pygame.time.Clock()


	def _check_events(self):
		""" Respond to input events """

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					self.dino.control(-self.settings.dino_steps, 0)
				if event.key == pygame.K_RIGHT:
					self.dino.control(self.settings.dino_steps, 0)
				if event.key == pygame.K_UP:
					self.dino.jump()
			
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					self.dino.control(self.settings.dino_steps, 0)
					self.dino.image = pygame.transform.flip(self.dino.image_idle, True, False)
					
				if event.key == pygame.K_RIGHT:
					self.dino.control(-self.settings.dino_steps, 0)
					self.dino.image = self.dino.image_idle

			# If the game state is not active, enable the Play Button
			if not self.stats.game_active:
				if event.type == pygame.MOUSEBUTTONDOWN:
					mouse_pos = pygame.mouse.get_pos()
					self._check_play_button(mouse_pos)


	def _check_play_button(self, mouse_pos):
		""" Set the game state to active when player clicks Play button """
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)

		if button_clicked and not self.stats.game_active:
			

			# reset coins and ennemies
			self.coins.empty()
			self.ennemies.empty()
			self._create_coins()
			self._create_ennemy_row()

			# reset the game statistics
			self.stats.reset_stats()

			# set Dino to start position
			self.dino._restart()

			# set the game state to active
			self.stats.game_active = True

			#self.stats.score = 0 # reset the score
			self.sb.prep_score()

			# hide the mouse cursor
			pygame.mouse.set_visible(False)
			

	def _create_ground(self):
		ground = Ground(self)

		""" Find the number of tiles in a row """
		ground_width, ground_height = ground.rect.size
		available_space_x = self.settings.screen_width 
		number_of_tiles = available_space_x // ground_width

		for tile_number in range(number_of_tiles):
			ground = Ground(self)
			ground.x = ground_width * tile_number
			ground.rect.x = ground.x
			self.grounds.add(ground)


	def _create_platforms(self):


		## Level 1 - MIDDLE
		# Set the Y location of the platform
		yloc = self.settings.platform_l1_yloc

		platform = Platform(self, yloc)
		platform_width, platform_height = platform.rect.size
		available_space_x = self.settings.screen_width 
		number_of_tiles = self.settings.platform_tiles

		for x in range(number_of_tiles):
			platform = Platform(self, yloc)

			# Set the X location of the tiles
			platform.x = (platform_width * x) + (available_space_x // number_of_tiles + platform_width)
			platform.rect.x = platform.x
			self.platforms.add(platform)
		## END ##


		## Level 2
		# Set the Y location of the platform
		yloc = self.settings.platform_l2_yloc
		
		platform = Platform(self, yloc)
		platform_width, platform_height = platform.rect.size
		available_space_x = self.settings.screen_width 
		number_of_tiles = self.settings.platform_tiles

		
		# Level 2 - LEFT
		for x in range(number_of_tiles):
			platform = Platform(self, yloc)

			# Set the X location of the tiles
			platform.x = platform_width + (platform_width * x)
			platform.rect.x = platform.x
			self.platforms.add(platform)

		# Level 2- RIGHT
		for x in range(number_of_tiles):
			platform = Platform(self, yloc)

			# Set the X location of the tiles
			platform.x = (platform_width * x) + (available_space_x // number_of_tiles) + (number_of_tiles + 6 * platform_width)
			platform.rect.x = platform.x
			self.platforms.add(platform)
		## END ##


	def _create_coins(self):


		# Set the X location for all coins
		xloc = self.settings.coin_xloc


		## Level 1 - Ground
		# Each  tile in our grounds list should have 1 coin. 
		for tile in self.grounds:
			# Set the Y location of the coin, on top of the Ground.
			yloc = tile.rect.top - (1.5 * self.settings.coin_height) # Float on top of Ground Tile
			coin = Coin(self, yloc)
			coin.x = tile.rect.x + xloc # The coin is in the middle of the ground tile at tile.rect.x + 32px
			coin.rect.x = coin.x
			self.coins.add(coin)


		## Level 2 - Platforms
		# Each tile on a platform should have 1 coin.
		
		for tile in self.platforms:
			yloc = tile.rect.top - (1.5 * self.settings.coin_height)
			coin = Coin(self, yloc)
			coin.x = tile.rect.x + xloc
			coin.rect.x = coin.x
			self.coins.add(coin)
	


	def _create_ennemy_row(self):
		""" Create a row of ennemies """

		ennemy = Ennemy(self)
		ennemy_width, ennemy_height = ennemy.rect.size

		number_of_ennemies = 4 

		for e in range(number_of_ennemies):
			self._create_ennemy(e)


	def _create_ennemy(self, ennemy_number):
		""" Spawn an ennemy """

		ennemy = Ennemy(self)
		ennemy_width, ennemy_height = ennemy.rect.size
		ennemy.x = self.settings.screen_width + ennemy_width + 4 * ennemy_width * ennemy_number # Set the ennemies 4 ground tiles apart
		ennemy.rect.x = ennemy.x
		self.ennemies.add(ennemy)


	def _update_ennemies(self):
		""" Provide a continuous flow of ennemies """
		
		# Remove ennemies from the Sprite Group when they move offscreen
		for e in self.ennemies.copy():
			if e.rect.right <= 0:
				self.ennemies.remove(e)

		# Spawn a new group of ennemies if the Sprite contains less than 4
		if len(self.ennemies) < 4:
			self._create_ennemy_row()


		if pygame.sprite.spritecollideany(self.dino, self.ennemies):
			self._dino_hit()


	def _dino_hit(self):
		""" Respond to the dino being hit by ennemy """

		if self.stats.dinos_left > 0:

			# Decrease dino_limit
			self.stats.dinos_left -= 1

			# Pause the game before setting the Dino back at the start position.
			sleep(0.5)
			self.dino._restart()
			self.sb.prep_score() # Update score / health display



		elif self.stats.dinos_left == 0: 
			# set the game to a non active state
			self.stats.game_active = False

			# Show the mouse cursor again
			pygame.mouse.set_visible(True)



	def _update_screen(self):
		""" Update images on the screen and flip to the new screen """

		self.screen.blit(self.settings.backdrop, self.backdropbox)
		self.grounds.draw(self.screen)
		self.platforms.draw(self.screen)
		self.coins.draw(self.screen)
		self.ennemies.draw(self.screen)
		self.dino.blitme()
		self.sb.show_score()


		# Draw the play button above all other elements when the game is in an inactive state
		if not self.stats.game_active:
			self.play_button.draw_button()

		
		pygame.display.flip()



	def run_game(self):
		""" Start the game loop """

		while True:
			# Watch for input events:
		
			self._check_events()

			# If the game is in an active state, create objects
			if self.stats.game_active:
				self.dino.gravity()
				self.dino.update()
				self.coins.update()
				self.ennemies.update()
				self._update_ennemies()

				
			
			# Redraw the screen at each pass of the loop
			self._update_screen()
			self.clock.tick(self.settings.fps)
			
			

if __name__ == '__main__':
	# Make a game instance and run the game
	dr = DinoRun()
	dr.run_game()