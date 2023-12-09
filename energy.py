import pygame

from config import Settings
from tools import endGame


class Energy:
	'''能量'''

	def __init__(self, screen, settings, stats, tbs):
		self.settings = settings
		self.screen = screen
		self.energyNum = self.settings.initEnergy
		self.stats = stats
		self.trPos = self.settings.energyTRPos
		self.tbs = tbs

		self.render()

	def render(self):
		self.image = self.settings.energyFont.render(
			"Energy: %8s" % self.stats.energy, True, 
			self.settings.energyColor, self.settings.bgColor)
		self.rect = self.image.get_rect()
		self.rect.top = self.trPos[0]
		self.rect.right = self.trPos[1]
		self.screen.blit(self.image, self.rect)

	def reduceEnergy(self, energy):
		'''仅当更改后能量在[0, 100]范围内时修改能量'''
		self.energy -= energy
		if self.energy <= 0 and len(self.tbs) > 0:
			endGame(self.settings, 0) # 若能量耗尽且未营救成功，则结束游戏