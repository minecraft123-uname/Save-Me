import pygame
from pygame.sprite import Sprite
from os.path import join
from numpy import sin, pi


class Buoy(Sprite):

	def __init__(self, settings, screen, initCenter, v0x, v0y):
		super().__init__()
		self.settings = settings
		self.screen = screen
		self.screenRect = self.screen.get_rect()
		self.screenSize = self.screenRect.size
		self.image = pygame.image.load(join("src", "buoy.png"))
		self.rect = self.image.get_rect()
		self.size = self.rect.size
		self.rect.center = initCenter

		self.vx = v0x
		self.vy = v0y
		self.render()

	def render(self):
		self.screen.blit(self.image, self.rect)

	def inScreen(self):
		'''判断救生圈是否在屏幕里'''
		# return self.rect.left <= self.screenSize[0] and self.rect.top <= self.screenSize[1]
		return self.rect.top <= self.screenSize[1]

	def move(self):
		'''仅当救生圈在屏幕中时运动，且做斜抛运动'''
		if self.inScreen():
			self.rect.left += self.vx
			self.vy += self.settings.g
			self.rect.top += self.vy