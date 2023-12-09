import pygame
from pygame.transform import rotate
from os.path import join
from numpy import pi


class Arrow:

	def __init__(self, settings, screen):
		self.settings = settings
		self.screen = screen
		self.screenRect = self.screen.get_rect()
		self.screenSize = self.screenRect.size
		self.image = pygame.image.load(join("src", "arrow.png"))
		self.rect = self.image.get_rect()
		self.size = self.rect.size
		self.rect.left = self.settings.arrowInitPos[0]
		self.rect.top = self.settings.arrowInitPos[1]
		self.center = self.rect.center
		self.Y = self.rect.centery
		self.newImage = self.image
		self.newRect = self.image.get_rect(center=self.center)

		self.direction = 0
		self.angle = 0
		self.minAngle = self.settings.arrowAngleRange[0]
		self.maxAngle = self.settings.arrowAngleRange[1]
		self.rotateSpeed = self.settings.arrowRotateSpeed

		self.buoyV0 = 0

	def render(self):
		self.screen.blit(self.newImage, self.newRect.topleft)

	def rotate(self):
		if self.direction == 1 and self.angle <= self.maxAngle:
			if self.angle + self.rotateSpeed < self.maxAngle:
				self.angle += self.rotateSpeed
			else:
				self.angle = self.maxAngle
		elif self.direction == -1 and self.angle >= self.minAngle:
			if self.angle - self.rotateSpeed > self.minAngle:
				self.angle -= self.rotateSpeed
			else:
				self.angle = self.minAngle
		else:
			return

		self.newImage = rotate(self.image, self.angle)
		self.newRect = self.newImage.get_rect(center=(self.center[0], self.Y))