import pygame
from dino import Dino


class Score():

	def __init__(self, dr_game):
		""" Class to manage the Dino score """

		self.screen = dr_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = dr_game.settings



		# Define Text Color
		self.white = (255, 255, 255)

		# Create font object
		self.font = pygame.font.Font('freesansbold.ttf', 16)

		# Create text surface object
		self.text = self.font.render('TEST', True, self.white)


		
		self.rect = self.text.get_rect()

		self.rect.x = 0
		self.rect.y = 0


	def update(self):
		""" Draw the text to the screen """

		self.screen.blit(self.text, self.rect)


