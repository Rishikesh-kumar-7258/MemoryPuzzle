import pygame

from functions import Write

class Fliper:

    def __init__(self, x=0, y=0, color=(255,255,255), background=(0,0,0), width=50, height=50, screen=None, text=1):
        self.x = x
        self.y = y
        self.color = color
        self.background = background
        self.width = width
        self.height = height
        self.screen = screen
        self.text = text

        self.isflip = False

        box = pygame.draw.rect(self.screen, self.background, [self.x, self.y, self.width, self.height])

    def render(self) : 
        box = pygame.draw.rect(self.screen, self.background, [self.x, self.y, self.width, self.height])
        l1 = pygame.draw.line(self.screen, self.color, (self.x,self.y), (self.x+self.width, self.y))
        l2 = pygame.draw.line(self.screen, self.color, (self.x,self.y), (self.x, self.y+self.height))
        l3 = pygame.draw.line(self.screen, self.color, (self.x+self.width,self.y + self.width), (self.x+self.width, self.y))
        l4 = pygame.draw.line(self.screen, self.color, (self.x+self.width,self.y + self.width), (self.x+self.width, self.y))
        if self.isflip : Write(self.screen, str(self.text), self.x + self.width // 2, self.y + self.height // 2, self.color, self.background, size=int(0.70*self.height), center=True)

    def update(self):

        if self.clicked() : self.flip()
        self.render()

    def clicked(self):
        x,y = pygame.mouse.get_pos()
        a, b, c = pygame.mouse.get_pressed()

        return a and x >= self.x and x <= self.x + self.width and y >= self.y and y <= self.y + self.height
    
    def flip(self):

        self.isflip = True