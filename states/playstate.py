import pygame

from states.basestate import Base

from classes.fliper import Fliper

from functions import *

class Play(Base):

    def __init__(self):
        
        self.level = 1
        self.blockCount = 3
        self.flipers = []

        self.selected = None

    def render(self) :
        self.playspace = pygame.draw.rect(self.screen, (50, 0, 0), [190, 50, 600, 500])
        for fliper in self.flipers:
            fliper.render()

    def update(self, params) :

        for fliper in self.flipers:

            if fliper.clicked():
                print(self.selected)
                if self.selected == None:
                    self.selected = fliper
                    fliper.isflip = True
                else : 
                    if self.selected == fliper: fliper.isflip = True
                    else : self.selected.isflip = False
                    self.selected = None
                
        self.render()

    def enter(self, **params):
        self.GAME_STATE = params['gameState']
        self.screen = params['screen']
        self.WINDOW_WIDTH = params['windowWidth']
        self.WINDOW_HEIGHT = params['windowHeight']
        self.playspace = pygame.draw.rect(self.screen, (50, 0, 0), [190, 50, 600, 500])
        for i in range(self.blockCount):
            for j in range(4):
                fliper = Fliper(screen=self.screen, background=(255, 0, 0))
                fliper.width = 150 - 5
                fliper.height = 500 / self.blockCount - 5
                fliper.x = 190 + ((fliper.width + 5) * j)
                fliper.y = 50 + (fliper.height + 5) * i
                self.flipers.append(fliper)
        
        num = []
        for i in range(self.blockCount * 2) : 
            num.append(i+1)
            num.append(i+1)
        num = shuffle(num)

        i = 0
        for fliper in self.flipers:
            fliper.text = num[i]
            i += 1