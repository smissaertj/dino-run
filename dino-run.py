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


	def run_game(self):
		""" Start the game loop """


		while True:
			# Watch for input events:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						sys.exit()


			# Redraw the screen at each pass of the loop
			self.screen.fill(self.settings.bg_color)
			self.dino.blitme()
			pygame.display.flip()
			



if __name__ == '__main__':
	# Make a game instance and run the game
	dr = DinoRun()
	dr.run_game()