
class hpBar():
	def __init__(self, obj):
        self.image = pygame.Surface([10, obj.hitpoints])
        self.image.fill((0,180,0))

     def update(self,obj):
     	self.image = pygame.Surface([10, obj.hitpoints])
     	return self.image
