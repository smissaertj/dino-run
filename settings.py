import os
import pygame

class Settings:
	""" Class to define all settings for the game """

	def __init__(self):
		""" Initialize game settings """

		# Screen settings
		self.screen_width = 1920
		self.screen_height = 1080
		self.screen = pygame.display.set_mode((self.screen_width, self.screen_height)) 
		self.backdrop = pygame.image.load(os.path.join('img', 'backdrop.png')).convert_alpha()
		self.fps = 40
		self.ani = 5  # Animation Cycles

		# Dino settings
		self.dino_steps = 10 # amount of pixels to move left or right
		self.dino_width = 184
		self.dino_height = 196
		self.dino_img = pygame.image.load(os.path.join('img', 'dino_idle.png')).convert_alpha()
		self.dino_gravity = 1 # amount of pixels to drop/move downwards

		# Ground settings
		self.ground_img = pygame.image.load(os.path.join('img', 'grass.png')).convert_alpha()
		self.ground_size = (128, 128)

		# Platform settings
		self.platform_img = self.ground_img