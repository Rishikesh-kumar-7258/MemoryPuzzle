import pygame
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP

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
    
    def __eq__(self, o) -> bool:
        if isinstance(o, Fliper): return (int(o.text) == int(self.text))
        return False

    def render(self) : 
        box = pygame.draw.rect(self.screen, self.background, [self.x, self.y, self.width, self.height])
        if self.isflip : Write(self.screen, str(self.text), self.x + self.width // 2, self.y + self.height // 2, self.color, self.background, size=int(0.70*self.height), center=True)

    def update(self, params):
        # self.render()
        pass

    def clicked(self) -> bool:
        x,y = pygame.mouse.get_pos()
        a, b, c = pygame.mouse.get_pressed()

        return  (x >= self.x and x <= self.x + self.width and y >= self.y and y <= self.y + self.height and a)