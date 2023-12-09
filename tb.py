import pygame
from pygame.sprite import Sprite
from random import randint
from numpy import sin, pi
from os.path import join


class TB(Sprite):

	def __init__(self, settings, screen, initPos, A, initT, tIncr, omega):
		super().__init__()
		self.settings = settings
		self.screen = screen
		self.screenRect = self.screen.get_rect()
		self.screenSize = self.screenRect.size
		self.image = pygame.image.load(join("src", "tb.png"))
		self.rect = self.image.get_rect()
		self.rect.left = initPos[0]
		self.rect.top = initPos[1]
		self.size = self.rect.size
		self.initY = self.rect.top
		self.A = A
		self.t = initT
		self.tIncr = tIncr
		self.omega = omega
		self.energy = self.settings.energyConstant * (self.A * self.omega) ** 2 # E = (Aω)²C
		print(self.energy)

	def render(self):
		self.screen.blit(self.image, self.rect)

	def move(self):
		'''简谐运动'''
		self.rect.y = self.initY + self.A * sin(self.omega * self.t)
		self.t += self.tIncr