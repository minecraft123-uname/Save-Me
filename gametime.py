import pygame

from tools import endGame

class GameTime:
	'''游戏时间'''

	def __init__(self, screen, settings, stats, tbs):
		self.settings = settings
		self.stats = stats
		self.screen = screen
		self.clock = pygame.time.Clock()
		self.tlPos = self.settings.timeTLPos
		self.tbs = tbs
		self.ticks = pygame.time.get_ticks()

		self.render()

	def render(self):
		'''
		开始游戏时获取毫秒数.
		每次循环获取当前毫秒数，若经过时间达到1秒，
		则将剩余时间减少1秒.
		'''
		seconds = (pygame.time.get_ticks() - self.ticks) // 1000
		if seconds >= 1:
			self.stats.time -= seconds
			self.ticks += seconds * 1000
		if self.stats.time <= 0 and len(self.tbs) > 0:
			endGame(self.settings, 1) # 若时间耗尽且未营救成功，则结束游戏
		self.image = self.settings.energyFont.render(
			"Time: %6ss" % self.stats.time, True, 
			self.settings.timeColor, self.settings.bgColor)
		self.rect = self.image.get_rect()
		self.rect.top = self.tlPos[0]
		self.rect.left = self.tlPos[1]
		self.screen.blit(self.image, self.rect)