class Menu:
    '''
    The Menu should be initalized with a list of menu entries
    it then creates a menu accordingly and manages the different
    print Settings needed
    '''

    MENUCLICKEDEVENT = USEREVENT +1

    def __init__(self,menuEntries, menuCenter = None):
        '''
        The constructer uses a list of string for the menu entries,
        which need  to be created
        and a menu center if non is defined, the center of the screen is used
        '''
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.background = pygame.Surface(screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))
        self.active=False

        if pygame.font:
            fontSize = 36
            fontSpace= 4
            # loads the standard font with a size of 36 pixels
            # font = pygame.font.Font(None, fontSize)

            # calculate the height and startpoint of the menu
            # leave a space between each menu entry
            menuHeight = (fontSize+fontSpace)*len(menuEntries)
            startY = self.background.get_height()/2 - menuHeight/2  

            #listOfTextPositions=list()
            self.menuEntries = list()
            for menuEntry in menuEntries:
                centerX=self.background.get_width()/2
                centerY = startY+fontSize+fontSpace
                newEnty = MenuItem(menuEntry,(centerX,centerY))
                self.menuEntries.append(newEnty)
                self.background.blit(newEnty.get_surface(), newEnty.get_pos())
                startY=startY+fontSize+fontSpace

    def drawMenu(self):
        self.active=True            
        screen = pygame.display.get_surface()
        screen.blit(self.background, (0, 0))

    def isActive(self):
        return self.active
    def activate(self,):
        self.active = True
    def deactivate(self):
        self.active = False
    def handleEvent(self,event):
        if event.type == MOUSEBUTTONDOWN and isActive():
            # initiate with menu Item 0
            curItem = 0
            # get x and y of the current event 
            eventX = event.pos[0]
            eventY = event.pos[1]
            # for each text position 
            for menuItem in self.menuEntries:
                textPos = menuItem.get_pos()
                #check if current event is in the text area 
                if eventX &gt: textPos.left and eventX &lt; textPos.right \
                                 and eventY &gt; textPos.top and eventY