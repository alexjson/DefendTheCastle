#Defend the castle
#File: hud.py
# Alexander Johansson
# himself@alexjson.se 
# Python 2.7.3
# Ubuntu 12.04 LTS
# PyGame 1.9.1
#
#
# File containing hud for mana, health and power
import pygame, sys, math ,pygame.gfxdraw

hpColor = (208,70,72)
hpColor2 = (210,170,153)
powerColor = (109,170,44)
powerColor2 = (218,212,94)
manaColor = (89,90,150)
manaColor2 = (109,194,202)

class hpBar():
	def __init__(self, obj):
		self.image2 = pygame.Surface([obj.hitpoints,5]) 
		self.image = pygame.Surface([obj.hitpoints,10])
		self.image2.fill(hpColor2)
		self.image.fill(hpColor)

	def update(self,obj):
		if obj.hitpoints>0:
	 		self.image = pygame.Surface([obj.hitpoints,10])
	 		self.image.fill(hpColor)
	 		self.image.blit(self.image2,(0,0))
 			return self.image
 		else:
 			return pygame.Surface([0,10])
 		

class powerBar():
	def __init__(self, obj):
		self.image2 = pygame.Surface([obj.hitpoints,5]) 
		self.image = pygame.Surface([int((float(obj.powerpoints)/obj.full_powerpoints)*100),10])
		self.image2.fill(powerColor2)
		self.image.fill(powerColor)

	def update(self,obj):
		if obj.powerpoints> 0:
	 		self.image = pygame.Surface([int((float(obj.powerpoints)/obj.full_powerpoints)*100),10])
	 		self.image.fill(powerColor)
	 		self.image.blit(self.image2,(0,0))
	 		return self.image
	 	else:
 			return pygame.Surface([0,10])
	 	

class manaBar():
	def __init__(self, obj):
		self.image2 = pygame.Surface([obj.manapoints,5]) 
		self.image = pygame.Surface([int((float(obj.manapoints)/obj.full_manapoints)*100),10])
		self.image2.fill(manaColor2)
		self.image.fill(manaColor)

	def update(self,obj):
		timer = 0
		if obj.manapoints > 0:
 			self.image = pygame.Surface([int((float(obj.manapoints)/obj.full_manapoints)*100),10])
 			self.image.fill(manaColor)
 			self.image.blit(self.image2,(0,0))
 			return self.image
 		else:
 			return pygame.Surface([0,10])

class superBar():
	def __init__(self, obj):
		self.surf = pygame.Surface([45,45],pygame.SRCALPHA, 32)
		self.rect = self.surf.get_rect()
		self.color = (50,255,50)
		self.image = pygame.image.load("gfx/fireball/F1.png")

	def update(self,obj):
		self.surf = pygame.Surface([44,44],pygame.SRCALPHA, 32)
		self.rect = self.surf.get_rect()
		timer = 0
		if obj.superpoints > 100:
			self.surf.blit(self.image,(10,14))
		if timer==20:
			obj.superpoints+=1
		elif timer<10:
			timer+=1
		
		return self.surf
		
 		
