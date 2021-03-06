import pygame.font

class Button:

	def __init__(self, dr_game, msg):
		""" Set button attributes """

		self.screen = dr_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = dr_game.settings


		# Set definitions and properties
		self.width, self.height = self.settings.play_button_width, self.settings.play_button_height
		self.button_color = self.settings.play_button_bg_color
		self.text_color = self.settings.play_button_txt_color
		self.font = pygame.font.SysFont(None, 48)

		# Built the button rect and center it
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center


		# Prepare the msg for the button
		self._prep_msg(msg)


	def _prep_msg(self, msg):
		""" Turn string into image """
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center


	def draw_button(self):
		# Draw the blank button and then the message

		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
