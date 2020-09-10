import os
import pygame

class Settings:
	""" Class to define all settings for the game """

	def __init__(self):
		""" Initialize game settings """

		# Screen settings
		self.screen_width = 1920
		self.screen_height = 1080
		self.bg_color = (0, 0, 0)
		self.backdrop = pygame.transform.scale(pygame.image.load(os.path.join('img', 'backdrop.png')), (self.screen_width, self.screen_height) )
		self.fps = 40
		self.ani = 7  # Animation Cycles

		# Dino settings
		self.dino_steps = 10 # amount of pixels to move left or right
		self.dino_size = (184, 196)
		self.dino_gravity = 1 # amount of pixels to drop/move downwards
