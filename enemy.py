#Defend the castle
#File: enemy.py
# Alexander Johansson
# himself@alexjson.se 
# Python 2.7.3
# Ubuntu 12.04 LTS
# PyGame 1.9.1
#
#
# File containing enemy classes

import pygame, glob, sys, random


class Minotaur(pygame.sprite.Sprite):
     
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ani = glob.glob("gfx/enemies/mino_W*.png")
        self.ani.sort()
        self.ani_max= len(self.ani)-1
        self.ani_pos=random.randint(0, self.ani_max)
        self.image = pygame.transform.flip(pygame.image.load(self.ani[0]),1,0)

        self.atk = glob.glob("gfx/enemies/mino_A*.png")
        self.atk.sort()
        self.atk_max= len(self.atk)-1
        self.atk_pos=0
        self.image = pygame.transform.flip(pygame.image.load(self.atk[0]),1,0)
        self.dmg = 4

        self.ani_speed_init=10
        self.ani_speed = self.ani_speed_init

        self.radius = 45
        self.rect = self.image.get_rect()
        self.hitpoints = 100

    def update(self):
		self.ani_speed-=1
		if self.ani_speed == 0:
			self.image = pygame.transform.flip(pygame.image.load(self.ani[self.ani_pos]),1,0)
			self.ani_speed = self.ani_speed_init
			if self.ani_pos == self.ani_max:
				self.ani_pos = 0
			else:
				self.ani_pos+=1
    def LoseHealth(self, amount):
        self.hitpoints-=amount

    def attack(self):
            self.ani_speed-=1
            if self.ani_speed == 0:
                self.image = pygame.transform.flip(pygame.image.load(self.atk[self.atk_pos]),1,0)
                self.ani_speed = self.ani_speed_init
                if self.atk_pos == self.atk_max:
                    self.atk_pos = 0
                else:
                    self.atk_pos+=1
    def getScore(self):
        return 5


class Goblin(pygame.sprite.Sprite):
     
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ani = glob.glob("gfx/enemies/rand_W*.png")
        self.ani.sort()
        self.ani_max= len(self.ani)-1
        self.ani_pos=random.randint(0, self.ani_max)
        self.image = pygame.transform.flip(pygame.image.load(self.ani[0]),1,0)

        self.atk = glob.glob("gfx/enemies/rand_A*.png")
        self.atk.sort()
        self.atk_max= len(self.atk)-1
        self.atk_pos=0
        self.image = pygame.transform.flip(pygame.image.load(self.atk[0]),1,0)
        self.dmg = 1

        self.ani_speed_init=7
        self.ani_speed = self.ani_speed_init

        self.radius = 15
        self.rect = self.image.get_rect()
        self.hitpoints = 10

    def update(self):
        self.ani_speed-=1
        if self.ani_speed == 0:
            self.image = pygame.transform.flip(pygame.image.load(self.ani[self.ani_pos]),1,0)
            self.ani_speed = self.ani_speed_init
            if self.ani_pos == self.ani_max:
                self.ani_pos = 0
            else:
                self.ani_pos+=1
    def LoseHealth(self, amount):
        self.hitpoints-=amount

    def attack(self):
            self.ani_speed-=1
            if self.ani_speed == 0:
                self.image = pygame.transform.flip(pygame.image.load(self.atk[self.atk_pos]),1,0)
                self.ani_speed = self.ani_speed_init
                if self.atk_pos == self.atk_max:
                    self.atk_pos = 0
                else:
                    self.atk_pos+=1
    def getScore(self):
        return 1

        