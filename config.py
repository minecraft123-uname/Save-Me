import pygame
from numpy import pi

from tools import endGame

class Settings:
	'''静态配置数据'''

	def __init__(self):
		self.title = "救我救我"
		self.screenSize = (1120, 630) # 屏幕尺寸
		self.bgColor = (255, 255, 255) # 背景颜色
		self.waterDepth = 220 # 水深/像素
		self.waterColor = (0, 0, 255) # 水颜色
		self.waterYPos = self.screenSize[1] - self.waterDepth
		self.waterRect = ((0, self.waterYPos), self.screenSize)

		self.g = 0.03 # g
		self.arrowInitPos = (25, 150) # 箭头初始位置
		self.arrowRotateSpeed = 1 # 箭头旋转速度
		self.arrowAngleRange = (-60, 60) # 箭头旋转角度/度

		self.tbNum = 30 # tb数量
		self.tbInitTRange = (0, 0.5) # tb振动初始时间范围/秒
		self.tbARange = (20, 80) # tb振幅范围/像素
		self.tbTRange = (1.2, 2) # tb周期范围/秒
		self.tbOmegaRange = (2 * pi / self.tbTRange[1], 2 * pi / self.tbTRange[0])
		self.tbHeight = 68
		self.tbMaxFloatHeight = 30 # tb浮出水面最大高度/像素
		self.tbMaxBeneathHeight = 30 # tb沉入水底最大高度/像素
		self.tbTIncrRange = (0.006, 0.012) # tb每帧画面振动时间增加量/秒
		self.tbXRange = (int(self.screenSize[0] * 0.15), int(self.screenSize[0] * 0.9))
		self.tbYRange = (self.waterYPos - self.tbMaxFloatHeight + int(self.tbARange[1] / 2),
			self.screenSize[1] + self.tbMaxBeneathHeight - self.tbHeight - int(self.tbARange[1] / 2))

		self.initTime = 60 # 初始时间
		self.timeTLPos = (10, 10) # 时间上/左坐标
		self.timeFont = pygame.font.SysFont(None, 72) # 时间字体
		self.timeColor = (255, 117, 26) # 时间颜色

		self.initEnergy = 114 # 初始能量
		self.energyConstant = 0.00015 # 能量常数, 见tb.py:TB.__init__
		self.energyFont = pygame.font.SysFont(None, 72) # 能量字体
		self.energyTRPos = (10, self.screenSize[0] - 10) # 能量上/右坐标
		self.energyColor = (102, 68, 0) # 能量颜色

		self.powerTRPos = (80, self.screenSize[0] - 10) # 力量上/右坐标
		self.powerFont = pygame.font.SysFont(None, 72) # 力量字体
		self.powerColor = (0, 255, 0) # 力量颜色
		self.powerToEnergyConstant = 0.2 # 力量-能量常数, 见Stats.changePower
		self.powerToVelocityConstant = 0.1 # 力量-速率常数, 见tools.py:create_buoy

		self.maxBuoys = 5 # 最大救生圈数量
		self.shootEnergyConstant = 0.3 # 发射能量常数

		self.endgame_infos = ("\n\nYou ran out of all your energy without saving all the Tubos!\n\n",
			"\n\nDue to your untimely rescue, Tubo sank!\n\n",
			"\n\nCongyatulations! You successfully saved all the TBs!\n\n")


class Stats:
	'''运行时数据'''

	def __init__(self, settings):
		self.settings = settings
		self.energy = self.settings.initEnergy
		self.time = self.settings.initTime
		self.power = 0
		self.powerChange = 0
		self.powerChanging = False
		# self.clock = pygame.time.Clock()

	def changePower(self):
		'''仅当正在改变力量时改变力量，同时改变能量.
		当力量减少时，能量减少，且能量减少量=力量减少量*力量能量常数
		'''
		if 0 <= self.power + self.powerChange <= 100 and self.powerChanging:
			self.power += self.powerChange
			if self.powerChange > 0:
				self.energy = round(self.energy - self.settings.powerToEnergyConstant, 2)
			# self.clock.tick(15)
		if self.energy <= 0:
			endGame(self.settings, 0)