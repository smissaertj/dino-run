import sys
import pygame

from settings import Settings
from dino import Dino
from ground import Ground
from platform import Platform


class DinoRun:
	""" Class to manage game assets and behaviour. """

	def __init__(self):
		""" Initialize the game and create game resouces. """

		pygame.init()
		self.settings = Settings()
		self.screen = self.settings.screen
		self.backdropbox = self.screen.get_rect()
		pygame.display.set_caption("Dino Run!")
		
		self.dino = Dino(self)
		self.grounds = pygame.sprite.Group()
		self.platforms = pygame.sprite.Group()


		# Create the ground and platform outside of the main loop
		# to prevent them from being recreated over and over again in _update_screen(), slowing down the application over time.
		self._create_ground()
		self._create_platform()


		# Get the pygame clock for handling FPS
		self.clock = pygame.time.Clock()


	def _check_events(self):
		""" Respond to input events """

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()


			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()
				if event.key == pygame.K_LEFT:
					self.dino.control(-self.settings.dino_steps, 0)
				if event.key == pygame.K_RIGHT:
					self.dino.control(self.settings.dino_steps, 0)

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					self.dino.control(self.settings.dino_steps, 0)
					self.dino.image = pygame.transform.flip(self.dino.image_idle, True, False)
					
				if event.key == pygame.K_RIGHT:
					self.dino.control(-self.settings.dino_steps, 0)
					self.dino.image = self.dino.image_idle



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


	def _create_platform(self):
		""" Create a platform  """

		platform = Platform(self)
		platform_width, platform_height = platform.rect.size
		available_space_x = self.settings.screen_width 
		number_of_tiles = 3

		for x in range(number_of_tiles):
			platform = Platform(self)
			platform.x = (platform_width * x) + (available_space_x // 3 + platform_width)
			platform.rect.x = platform.x
			self.platforms.add(platform)



	def _update_screen(self):
		""" Update images on the screen and flip to the new screen """

		self.screen.blit(self.settings.backdrop, self.backdropbox)
		self.grounds.draw(self.screen)
		self.platforms.draw(self.screen)

		self.dino.blitme()
		
		pygame.display.flip()



	def run_game(self):
		""" Start the game loop """

		while True:
			# Watch for input events:
		
			self._check_events()
			self.dino.gravity()
			self.dino.update()

			# Redraw the screen at each pass of the loop
			self._update_screen()

			self.clock.tick(self.settings.fps)
			
			

if __name__ == '__main__':
	# Make a game instance and run the game
	dr = DinoRun()
	dr.run_game()