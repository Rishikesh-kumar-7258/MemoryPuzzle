import pygame
from functions import Write

class Changer:

    def __init__(self, actions=[], x=0, y=0, width=140, height=40, screen=None, color=(255, 0, 0), gameState=None) : 
        self.actions = actions
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.blockWidth = 0.2*self.width
        self.color = color
        self.current = 0

    def render(self) :

        Write(self.screen, str(self.actions[self.current]), x=self.x+self.width/2, y=self.y+self.height/2, size=int(3*self.height/4), center=True)
        leftArrow = pygame.draw.polygon(self.screen, self.color, [(self.x+self.blockWidth, self.y), (self.x+self.blockWidth, self.y+self.height), (self.x, self.y+self.height/2)])
        rightArrow = pygame.draw.polygon(self.screen, self.color, [(self.x-self.blockWidth + self.width, self.y), (self.x-self.blockWidth+self.width, self.y+self.height), (self.x+self.width, self.y+self.height/2)])

    def update(self, params) : 
        
        for event in params:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if (self.current > 0) : self.current -= 1
                if event.key == pygame.K_RIGHT: 
                    if (self.current < len(self.actions) - 1) : self.current += 1      
        self.render()

