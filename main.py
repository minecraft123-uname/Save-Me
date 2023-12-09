import pygame

from config import *
from tools import *
from tb import TB
from buoy import Buoy
from arrow import Arrow
from energy import Energy
from gametime import GameTime
from power import Power


def main():
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode(settings.screenSize)
	screenRect = screen.get_rect()
	pygame.display.set_caption(settings.title)

	arrow = Arrow(settings, screen)
	tbs = pygame.sprite.Group()
	buoys = pygame.sprite.Group()
	stats = Stats(settings)
	energy = Energy(screen, settings, stats, tbs)
	gametime = GameTime(screen, settings, stats, tbs)
	power = Power(screen, settings, stats, arrow)
	for i in range(settings.tbNum):
		tbs.add(create_tb(settings, screen))

	while True:
		for i in buoys:
			if not i.inScreen():
				buoys.remove(i)	# 删除屏幕外的救生圈
		check_collisions(settings, tbs, buoys, stats)
		check_events(settings, screen, tbs, buoys, arrow, stats)
		update_screen(settings, screen, tbs, buoys, arrow, stats, energy, gametime, power)

main()