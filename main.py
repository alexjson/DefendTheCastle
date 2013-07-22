#Defend the castle
#File: main.py
# Alexander Johansson
# himself@alexjson.se 
# Python 2.7.3
# Ubuntu 12.04 LTS
# PyGame 1.9.1
#
#
# The main program for the game

import sys, pygame, glob, pygame.mixer, math, random, wizard, enemy, projectile, button
from pygame import *
from wizard import Wizard
from enemy import Minotaur
from enemy import Goblin
from projectile import Projectile
from button import Button
from button import ImageButton


#Paints the scene of the games current state
def paintScene():
	if menuActive:
		screen.fill((0,0,0))
		screen.blit(background,(0,0))
		for x in xrange(0,8):
			screen.blit(ground1,(120*x,170))
		for x in xrange(0,16):
			for y in xrange(0,10):
				screen.blit(ground2,(60*x,233+60*y))
		screen.blit(castle,(0,200))
		for x in xrange(0,16):
			screen.blit(grass,(60*x,500))

		if infoVisible == False:
			screen.blit(menuHeader,(0,0))

			btn_mid = screen.get_width()/2 - startBtn.rect.width/2
			screen.blit(startBtn.getButton(),(btn_mid,240))
			startBtn.rect.x = btn_mid
			startBtn.rect.y = 240

			screen.blit(aboutBtn.getButton(),(btn_mid,290))
			aboutBtn.rect.x = btn_mid
			aboutBtn.rect.y = 290

			screen.blit(quitBtn.getButton(),(btn_mid,340))
			quitBtn.rect.x = btn_mid
			quitBtn.rect.y = 340

		if infoVisible == True:
			screen.blit(Info,(0,0))


	elif gameOver==False:
		screen.blit(background,(0,0))
		for x in xrange(0,8):
			screen.blit(ground1,(120*x,170))
		for x in xrange(0,16):
			for y in xrange(0,10):
				screen.blit(ground2,(60*x,233+60*y))
		screen.blit(castle,(0,200))
		all_sprites_list.draw(screen)

		wizard_.update()
		screen.blit(wizard_.img,(wizard_.x,wizard_.y))
		screen.blit(uiBars,(10,10))
		screen.blit(wizard_.hpBar.update(wizard_),(85,17))
		screen.blit(wizard_.powerBar.update(wizard_),(85,37))
		screen.blit(wizard_.manaBar.update(wizard_),(85,57))
		screen.blit(wizard_.superBar.update(wizard_),(21,20))

		for x in xrange(0,16):
			screen.blit(grass,(60*x,500))
	elif gameOver:
		screen.fill((0,0,0))
		text=font.render("Game Over", True, (255,0,0))
		text_rect = text.get_rect()
		text_x = screen.get_width()/2 - text_rect.width/2
		text_y = screen.get_height()/2 - text_rect.height/2
		screen.blit(text, [text_x, text_y])
		# scoreText = fontScore.render("Score " + str(SCORE), True, (240,240,240))	
		# screen.blit(scoreText,[text_x,text_y-50])

		screen.blit(restartBtn.getButton(),(370,300))
		restartBtn.rect.x = 350
		restartBtn.rect.y = 300

		screen.blit(quitBtn.getButton(),(500,300))
		quitBtn.rect.x = 500
		quitBtn.rect.y = 300
	if soundOn == True:
		screen.blit(soundOnBtn.getButton(),(900,20))
		soundOnBtn.rect.x = 900
		soundOnBtn.rect.y = 20
	elif soundOn == False:
		screen.blit(soundOffBtn.getButton(),(900,20))
		soundOffBtn.rect.x = 900
		soundOffBtn.rect.y = 20

	scoreText = fontScore.render("Score " + str(SCORE), True, (240,240,240))	
	screen.blit(scoreText,[220,20])
	

#Restarts the game at level 1 and reset variables
def restart():
	global LEVEL
	global wizard_
	global menuActive
	global NUMBER_OF_ENEMIES
	global gameOver
	global SCORE
	SCORE = 0
	NUMBER_OF_ENEMIES = 0
	LEVEL = 0
	gameOver = False
	menuActive = False
	wizard_.reset()
	paintScene()
	nextLevel()
#Generates the next level of the game, is called when the sprite list with enemies is empty
def nextLevel():
	global LEVEL
	global NUMBER_OF_ENEMIES
	global wizard_
	gameOver = False
	LEVEL += 1
	wizard_.levelUp(LEVEL)
	printLevel(LEVEL)
	NUMBER_OF_ENEMIES += 5
	all_sprites_list.empty()
	enemy_list.empty()
	generateEnemies(NUMBER_OF_ENEMIES,LEVEL)
	paintScene()

#Prints the text between levels 
def printLevel(level):
	text = "Level "+ str(level)
	image = pygame.Surface([200,50],pygame.SRCALPHA, 32)
	font = pygame.font.SysFont('8-bit Limit BRK', 36)
	fontText = font.render(text, True, (255,255,255))
	image.blit(fontText,(0,0))
	screen.blit(image,(400,200))
	pygame.display.update()
	pygame.time.wait(1000)



#Init pygame
pygame.init()
Soundtrack = pygame.mixer.Sound("sound/soundtrack.wav")
Soundtrack.set_volume(0.5)
SCREEN_HEIGHT=550
SCREEN_WIDTH=940
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Defend the castle - (c) Alexander Johansson 2013")
clock = pygame.time.Clock()
font = pygame.font.SysFont('8-bit Limit BRK', 36)
fontScore = pygame.font.SysFont('8-bit Limit BRK', 16)
menuActive = True
infoVisible = False
soundOn = True
#Load in gfx
background = pygame.image.load("gfx/bg.png")
ground1 = pygame.image.load("gfx/ground1.png")
ground2 = pygame.image.load("gfx/ground2.png")
grass = pygame.image.load("gfx/grass.png")
castle = pygame.image.load("gfx/castle.png")
uiBars = pygame.image.load("gfx/bars.png")
menuHeader = pygame.image.load("gfx/menuheader.png")
Info = pygame.image.load("gfx/info.png")
gameOverBG = pygame.image.load("gfx/menubg.png")
#Menu buttons
Menu = Button("Menu",100,40)
startBtn = Button("Start",100,40)
aboutBtn = Button("About",100,40)
quitBtn = Button("Quit", 100,40)
restartBtn = Button("Retry",100,40)

#Game buttons
soundOnBtn = ImageButton("gfx/soundOn.png")
soundOffBtn = ImageButton("gfx/soundOff.png")

#All sprites
all_sprites_list = pygame.sprite.Group()

#All enemies
enemy_list = pygame.sprite.Group()

#All projectiles
projectile_list = pygame.sprite.Group()


#Generates enemies for ceach level
def generateEnemies(numberOfEnemies,Level):

	for i in xrange(numberOfEnemies):
		enemy = Goblin()
		# Set a random location for the enemy
		enemy.rect.x = random.randint(SCREEN_WIDTH,SCREEN_WIDTH+500)
		enemy.rect.y = random.randint(200, 400)
		# Add the enemy to the list of objects
		enemy_list.add(enemy)
		all_sprites_list.add(enemy)

	for i in range(int(float(numberOfEnemies)/2)):   
	    enemy = Minotaur()
	 
	    # Set a random location for the enemy
	    enemy.rect.x = random.randint(SCREEN_WIDTH,SCREEN_WIDTH+500)
	    enemy.rect.y = random.randint(200, 400)
	     
	    # Add the enemy to the list of objects
	    enemy_list.add(enemy)
	    all_sprites_list.add(enemy)





# The main loop for the game
mouseX,mouseY = pygame.mouse.get_pos()
mouseX=0
mouseY=0
ypos=0
xpos=0
mousePos = [0,0]
wizard_ = Wizard()
atkSpeed=0
gameOver = False
levelDone = False
ENEMYSPEED = 1
NUMBER_OF_ENEMIES = 2
LEVEL = 1
SCORE = 0
generateEnemies(NUMBER_OF_ENEMIES,LEVEL)
Soundtrack.play(-1)

while 1:
	clock.tick(60)

	#Eventhandling
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
		 sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				if menuActive and infoVisible == False:
					menuActive = False
				elif menuActive and infoVisible:
					infoVisible = False
				else:
					menuActive = True
				
			if event.key == pygame.K_SPACE and wizard_.superpoints>100:
				wizard_.LoseSuper(100)
				for x in xrange(1,20):
					projectile_ = Projectile("Super")
					mouseX,mouseY = pygame.mouse.get_pos()
					projectile_.fire(mouseX,mouseY)
					all_sprites_list.add(projectile_)
					projectile_list.add(projectile_)

		elif event.type== MOUSEBUTTONDOWN:
			mouseX,mouseY = pygame.mouse.get_pos()
			mousePos = pygame.mouse.get_pos()
			if soundOn == True:
				if soundOnBtn.rect.collidepoint(mouseX, mouseY):
					Soundtrack.stop()
					soundOn = False
			elif soundOn==False:
				if soundOffBtn.rect.collidepoint(mouseX, mouseY):
					Soundtrack.play(-1)
					soundOn = True
			
			if menuActive:
				if startBtn.rect.collidepoint(mouseX,mouseY):
					restart()
				if aboutBtn.rect.collidepoint(mouseX,mouseY):
					infoVisible = True
				if quitBtn.rect.collidepoint(mouseX,mouseY):
					sys.exit()
			if gameOver:
				if restartBtn.rect.collidepoint(mouseX,mouseY):
					restart()
				if quitBtn.rect.collidepoint(mouseX,mouseY):
					sys.exit()
			if gameOver == False and menuActive== False:
				if wizard_.powerpoints >1 and pygame.mouse.get_pressed()[0]:
					wizard_.LosePower(1)
					projectile_ = Projectile("Stone")
					projectile_.fire(mouseX,mouseY)
					all_sprites_list.add(projectile_)
					projectile_list.add(projectile_)
					xpos = projectile_.x
				if wizard_.manapoints >3 and pygame.mouse.get_pressed()[2]:
					wizard_.LoseMana(3)
					projectile_ = Projectile("Fire")
					projectile_.fire(mouseX,mouseY-30)
					all_sprites_list.add(projectile_)
					projectile_list.add(projectile_)
					xpos = projectile_.x

	#Game logic
	if wizard_.hitpoints < 0:
		gameOver = True
	if menuActive==False and gameOver == False:
		wizard_.Gain()
		if len(enemy_list) == 0:
			nextLevel()
		for projectile_ in projectile_list:
			if projectile_.rect.x < SCREEN_WIDTH+50 or projectile_.rect.y < SCREEN_HEIGHT+50:
				#Move projectile
				projectile_.move(mouseX-10,mouseY-10,projectile_.projectile_type)

				#Check collision, removes enemies
				enemy_hit_list = pygame.sprite.spritecollide(projectile_,enemy_list,False, pygame.sprite.collide_circle)

				#Remove projectiles
				for enemy in enemy_hit_list:
					if enemy.hitpoints >0:
						enemy.LoseHealth(projectile_.dmg)
					else:
						SCORE += enemy.getScore()
						enemy.kill()
						enemy_list.remove(enemy)
						all_sprites_list.remove(enemy)
						wizard_.Gain()
					
					projectile_list.remove(projectile_)
					all_sprites_list.remove(projectile_)
					projectile_.reset()
			if projectile_.rect.x > SCREEN_WIDTH+50 or projectile_.rect.y > SCREEN_HEIGHT+50:
				projectile_list.remove(projectile_)
				all_sprites_list.remove(projectile_)
				projectile_.reset()

		for enemy in enemy_list:
			if enemy.rect.x > 40:
				enemy.rect.x -=ENEMYSPEED
				enemy.update()
			else:
				enemy.attack()
				if atkSpeed==30:
					wizard_.LoseHealth(enemy.dmg)
				elif atkSpeed>30:
						atkSpeed=0
					
				atkSpeed+=1			

	paintScene()
	pygame.display.update()

