#Defend the castle
#File: projectile.py
# Alexander Johansson
# himself@alexjson.se 
# Python 2.7.3
# Ubuntu 12.04 LTS
# PyGame 1.9.1
#
#
# The projectile class

import pygame, glob, math, random, sys		

class Projectile(pygame.sprite.Sprite):


	def __init__(self, ProjectileType):
		pygame.sprite.Sprite.__init__(self)
		self.projectile_type = ProjectileType
		self.radius = 5
		self.mouseX = 0
		self.mouseY = 0

		if self.projectile_type == "Fire":
			self.speed = 15
			self.x_init = 5
			self.y_init = 275
			self.x = self.x_init
			self.y = self.y_init
			self.imageInit = pygame.image.load("gfx/Basic.png")
			self.imageInit = pygame.transform.rotate(self.imageInit, -90)
			self.image = self.imageInit
			self.rect = self.image.get_rect()
			self.gunSound = pygame.mixer.Sound("sound/shoot.wav")
			self.dmg = 40
		elif self.projectile_type == "Stone":
			self.speed = 10
			self.x_init = 5
			self.y_init = 275
			self.x = self.x_init
			self.y = self.y_init
			self.imageInit = pygame.image.load("gfx/rock.png")
			self.imageInit = pygame.transform.scale(self.imageInit,(8,8))
			self.image = self.imageInit
			self.rect = self.image.get_rect()
			self.gunSound = pygame.mixer.Sound("sound/shoot.wav")
			self.dmg = 10
		elif self.projectile_type == "Super":
			self.speed = 5
			self.x_init = 5
			self.y_init = 275
			self.x = self.x_init
			self.y = self.y_init
			self.ani = glob.glob("gfx/fireball/F*.png")
			self.ani.sort()
			self.ani_max= len(self.ani)-1
			self.ani_pos=random.randint(0, self.ani_max)
			self.imageInit = pygame.image.load(self.ani[0])
			self.image = self.imageInit
			self.rect = self.image.get_rect()
			self.ani_speed_init=10
			self.ani_speed = self.ani_speed_init
			self.gunSound = pygame.mixer.Sound("sound/shoot.wav")
			self.dmg = 100
		
		

	def fire(self,mouseX,mouseY):
		self.mouseX = mouseX
		self.mouseY = mouseY
		angle = getAngle(self.x,self.y,self.mouseX,self.mouseY)
		self.image = pygame.transform.rotate(self.imageInit,angle)
	def move(self,mouseX,mouseY,projectile_type):
		if projectile_type == "Super":
			self.ani_speed-=1
			if self.ani_speed == 0:
				self.image = pygame.image.load(self.ani[self.ani_pos])
				self.ani_speed = self.ani_speed_init
				if self.ani_pos == self.ani_max:
					self.ani_pos = 0
				else:
					self.ani_pos+=1

		self.x += self.speed
		self.y = self.y_init + (self.mouseY-self.y_init)*(float(self.x-self.x_init)/(self.mouseX-self.x_init))
		self.rect.y = self.y
		self.rect.x = self.x
	def reset(self):
		self.x = self.x_init
		self.y = self.y_init


def getAngle(x1, y1, x2, y2):
    # Return value is 0 for right, 90 for up, 180 for left, and 270 for down (and all values between 0 and 360)
    rise = y1 - y2
    run = x1 - x2
    angle = math.atan2(run, rise) # get the angle in radians
    angle = angle * (180 / math.pi) # convert to degrees
    angle = (angle + 90) % 360 # adjust for a right-facing sprite
    return angle
