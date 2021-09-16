from functions import Write
import pygame

class Changer:

    def __init__(self, actions=[], x=0, y=0, width=140, height=50, screen=None, color=(255, 0, 0), gameState=None) : 
        self.actions = actions
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.color = color
        self.gameState = gameState
        self.current = 0
        self.active = True

        self.passed = None


    def render(self) :

        right = pygame.draw.rect(self.screen, self.color, [self.x, self.y, 20/100*self.width, self.height])
        left = pygame.draw.rect(self.screen, self.color, [self.x + 80/100*self.width, self.y, 20/100*self.width, self.height])

    def update(self, params) : 
        
        for event in params:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("this is working")
                if event.key == pygame.K_RIGHT: pass
                if event.key == pygame.K_SPACE:
                    if self.active : 
                        self.gameState.change(self.actions[self.current], self.passed)
                    print("This is working")                
        self.render()

