import sys
from random import randint, uniform
from os import _exit

import pygame
from numpy import sin, cos, pi

from tb import TB
from buoy import Buoy


def update_screen(settings, screen, tbs, buoys, arrow, stats, energy, gametime, power):
	'''更新屏幕'''
	screen.fill(settings.bgColor)
	pygame.draw.line(screen, "black", (0, settings.waterYPos), (1120, settings.waterYPos), 5)
	pygame.draw.rect(screen, settings.waterColor, settings.waterRect)
	arrow.rotate()
	arrow.render()
	energy.render()
	gametime.render()
	stats.changePower()
	power.render()
	for tb in tbs:
		tb.move()
		tb.render()
	for buoy in buoys:
		buoy.move()
		buoy.render()
	pygame.display.flip()

def check_events(settings, screen, tbs, buoys, arrow, stats):
	'''检测键盘事件'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			stats.powerChanging = True # 若按下键，则开始改变力量
			if event.key == pygame.K_UP:
				arrow.direction = 1
			elif event.key == pygame.K_DOWN:
				arrow.direction = -1
			if event.key == pygame.K_w:
				stats.powerChange = 1 # 若按下w/s键，则力量增加/减少
			elif event.key == pygame.K_s:
				stats.powerChange = -1
			if event.key == pygame.K_SPACE:
				newBuoy = create_bouy(settings, screen, stats, arrow, buoys)
				stats.energy = round(stats.energy - stats.power * settings.shootEnergyConstant, 2)
				if stats.energy <= 0 and len(tbs) > 0:
					endGame(settings, 0)
				if newBuoy:
					buoys.add(newBuoy)
		elif event.type == pygame.KEYUP:
			# 若按键松开，则停止改变力量，同时将力量变化量清零
			arrow.direction = 0
			stats.powerChange = 0
			stats.powerChanging = False

def create_tb(settings, screen):
	'''创建tb，一切与运动状态有关的参数随机'''
	return TB(settings, screen,
		(randint(settings.tbXRange[0], settings.tbXRange[1]), 
			randint(settings.tbYRange[0], settings.tbYRange[1])), 
		randint(settings.tbARange[0], settings.tbARange[1]),
		uniform(settings.tbInitTRange[0], settings.tbInitTRange[1]),
		uniform(settings.tbTIncrRange[0], settings.tbTIncrRange[1]),
		uniform(settings.tbOmegaRange[0], settings.tbOmegaRange[1]))

def create_bouy(settings, screen, stats, arrow, buoys):
	'''当'''
	if len(buoys) >= settings.maxBuoys:
		return
	v0 = stats.power * settings.powerToVelocityConstant # 初速率 = 力量 * 力量速率常数
	radius = arrow.angle / 180 * pi
	buoy = Buoy(settings, screen, arrow.center, v0 * cos(radius), -v0 * sin(radius))
	return buoy

def check_collisions(settings, tbs, buoys, stats):
	'''检测碰撞'''
	collisions = pygame.sprite.groupcollide(buoys, tbs, True, True)
	if not collisions:
		return
	saved = []
	for i in collisions.values():
		for tb in i:
			saved.append(i) # 收集所有被碰撞的tb
	saved = tuple(set(i)) # 去重
	for i in saved:
		stats.energy = round(stats.energy + i.energy, 2)
	if len(tbs) == 0:
		endGame(settings, 2) # 当tb数量为0时，完成营救目标，结束游戏

def endGame(settings, arg):
	print(settings.endgame_infos[arg])
	_exit(0)