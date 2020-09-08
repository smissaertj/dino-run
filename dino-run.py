import sys
import pygame

from settings import Settings
from dino import Dino


class DinoRun:
	""" Class to manage game assets and behaviour. """

	def __init__(self):
		""" Initialize the game and create game resouces. """

		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Dino Run!")
		
		self.dino = Dino(self)


		# Get the pygame clock for handling FPS
		self.clock = pygame.time.Clock()


	def _check_events(self):
		""" Respond to input events """

		for event in pygame.event.get():
			keyhold = pygame.key.get_pressed()

			if event.type == pygame.QUIT:
				sys.exit()


			# Check for Key Presses
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()


			# Check for Key Hold
			if keyhold[pygame.K_RIGHT]:
				self.dino.moving_right = True
				
			else: 
				self.dino.moving_right = False



	def _update_screen(self):
		""" Update images on the screen and flip to the new screen """
		self.screen.fill(self.settings.bg_color)
		self.dino.blitme()
		pygame.display.flip()



	def run_game(self):
		""" Start the game loop """

		while True:
			# Watch for input events:
			self._check_events()
			self.dino.update()

			# Redraw the screen at each pass of the loop
			self._update_screen()

			self.clock.tick(self.settings.fps)
			
			

if __name__ == '__main__':
	# Make a game instance and run the game
	dr = DinoRun()
	dr.run_game()