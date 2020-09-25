import pygame

class Settings:
	""" Class to define all settings for the game """

	def __init__(self):
		""" Initialize game settings """

		# Screen settings
		self.screen_width, self.screen_height = 1920, 1080
		self.screen = pygame.display.set_mode((self.screen_width, self.screen_height)) 
		self.backdrop = pygame.image.load('img/backdrop.png').convert_alpha()
		self.fps = 50
		self.ani = 4  # Animation Cycles

		# Dino settings
		self.dino_steps = 15 # amount of pixels to move left or right
		self.dino_width, self.dino_height = 138, 147
		self.dino_img = pygame.transform.scale(pygame.image.load('img/dino_idle.png').convert_alpha(), (self.dino_width, self.dino_height))
		self.dino_gravity = 2 # amount of pixels to drop/move downwards
		self.dino_jump_height = 40 # How high to jump
		self.dino_limit = 3 # Amount of lives before game over.


		# Ennemy settings
		self.ennemy_img = pygame.image.load('img/mace.png').convert_alpha()
		self.ennemy_speed = 4.0
		self.ennemy_direction = -1 #  1 is right, -1 is left

		# Ground settings
		self.ground_img = pygame.image.load('img/grass.png').convert_alpha()
		self.ground_width, self.ground_height = 128, 128

		# Platform settings
		self.platform_tiles = 3
		self.platform_img = self.ground_img
		self.platform_l1_yloc = self.screen_height - (( 2 * self.ground_height) + self.dino_height)
		self.platform_l2_yloc = self.screen_height - (( 4 * self.ground_height) + self.dino_height)


		# Coin settings
		self.coin_width, self.coin_height = 64, 64
		self.coin_img = pygame.transform.scale(pygame.image.load('img/coin/coin_1.png').convert_alpha(), (self.coin_width, self.coin_height))
		self.coin_xloc = 32 # The coin is in the middle of the ground tile at tile.rect.x + 32px


		# Play Button
		self.play_button_width, self.play_button_height = 200, 50
		self.play_button_bg_color = (255, 51, 51) # Red
		self.play_button_txt_color = (255, 255, 255) # White

		# Scoring
		self.score_txt_color = (30, 30, 30) # Black
		

		