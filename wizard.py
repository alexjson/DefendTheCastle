#Defend the castle
#File: wizard.py
# Alexander Johansson
# himself@alexjson.se 
# Python 2.7.3
# Ubuntu 12.04 LTS
# PyGame 1.9.1
#
#
# Wizard class
import sys, pygame, glob, hud
from hud import *
HITPOINTS = 100
class Wizard():
	def __init__(self):
		self.x = 3
		self.y = 250
		self.full_manapoints = 100
		self.full_powerpoints = 100
		self.full_superpoints = 100
		self.manapoints = 100
		self.powerpoints = 100
		self.superpoints = 50
		self.ani_speed_init=20
		self.ani_speed = self.ani_speed_init
		self.ani = glob.glob("gfx/wizard/S_*.png")
		self.ani.sort()
		self.ani_pos=0
		self.ani_max= len(self.ani)-1
		self.img = pygame.image.load(self.ani[0])
		self.hitpointsfull = HITPOINTS
		self.hitpoints = self.hitpointsfull
		self.hpBar = hpBar(self)
		self.powerBar = powerBar(self)
		self.manaBar = manaBar(self)
		self.superBar = superBar(self)
		self.attacking = False
		self.gain_timer_init = 20
		self.gain_timer = self.gain_timer_init

	def still(self):
		self.ani_speed-=1
		if self.ani_speed == 0:
			self.img = pygame.image.load(self.ani[self.ani_pos])
			self.ani_speed = self.ani_speed_init
			if self.ani_pos == self.ani_max:
				self.ani_pos = 0
			else:
				self.ani_pos+=1

	def update(self):
		self.still()
	def LoseHealth(self, amount):
		self.hitpoints-=amount

	def LoseMana(self, amount):
		self.manapoints-=amount

	def LosePower(self,amount):
		self.powerpoints-=amount

	def LoseSuper(self,amount):
		self.superpoints-=amount
		self.superBar.update(self)

	def Gain(self):
		self.gain_timer-=1
		if self.gain_timer == 0:
			if self.manapoints<self.full_manapoints:
				self.manapoints+=1
			if self.powerpoints<self.full_powerpoints:
				self.powerpoints+=1
			if self.superpoints<self.full_superpoints:
				self.superpoints+=1

			self.gain_timer=self.gain_timer_init

	def reset(self):
		self.hitpoints = self.hitpointsfull
		self.manapoints = 100
		self.powerpoints = 100
		self.superpoints = 0

	def levelUp(self,level):
		self.full_manapoints+=5
		self.full_powerpoints+=10
		self.full_superpoints+=30
		self.manapoints += 40*level
		self.powerpoints += 40*level
		if self.manapoints>self.full_manapoints:
			self.manapoints = self.full_manapoints
		if self.powerpoints>self.full_powerpoints:
			self.powerpoints = self.full_powerpoints
		

			
