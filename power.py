import pygame


class Power:
	'''力量'''

	def __init__(self, screen, settings, stats, arrow):
		self.screen = screen
		self.settings = settings
		self.stats = stats
		self.arrow = arrow
		self.trPos = self.settings.powerTRPos

		self.render()

	def render(self):
		self.image = self.settings.powerFont.render(
			"Power: %6s" % self.stats.power + "%", True, 
			self.settings.powerColor, self.settings.bgColor)
		self.rect = self.image.get_rect()
		self.rect.top = self.trPos[0]
		self.rect.right = self.trPos[1]
		self.screen.blit(self.image, self.rect)