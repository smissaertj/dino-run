import pygame

class Settings:
	""" Class to define all settings for the game """

	def __init__(self):
		""" Initialize game settings """

		# Screen settings
		self.screen_width, self.screen_height = 1920, 1080
		self.screen = pygame.display.set_mode((self.screen_width, self.screen_height)) 
		self.backdrop = pygame.image.load('img/backdrop.png').convert_alpha()
		self.fps = 40
		self.ani = 5  # Animation Cycles

		# Dino settings
		self.dino_steps = 10 # amount of pixels to move left or right
		self.dino_width, self.dino_height = 184, 196
		self.dino_img = pygame.image.load('img/dino_idle.png').convert_alpha()
		self.dino_gravity = 2 # amount of pixels to drop/move downwards
		self.dino_jump_height = 40 # How high to jump

		# Ground settings
		self.ground_img = pygame.image.load('img/grass.png').convert_alpha()
		self.ground_width, self.ground_height = 128, 128

		# Platform settings
		self.platform_tiles = 3
		self.platform_img = self.ground_img
		self.platform_l1_yloc = self.screen_height - (( 2 * self.ground_height) + self.dino_height)
		self.platform_l2_yloc = self.screen_height - (( 4 * self.ground_height) + self.dino_height)