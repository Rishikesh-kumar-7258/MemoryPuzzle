import pygame

from states.basestate import Base

from classes.fliper import Fliper

from functions import *

class Play(Base):

    def __init__(self):
        
        # self.fliper = Fliper()    
        self.level = 1
        self.blockCount = 2 + self.level
        self.flipers = []

    def render(self) :
        self.playspace = pygame.draw.rect(self.screen, (50, 0, 0), [190, 50, 600, 500])
        for fliper in self.flipers:
            fliper.render()

    def update(self, params) :
        for fliper in self.flipers:
            fliper.update()
        self.render()

    def enter(self, **params):
        self.GAME_STATE = params['gameState']
        self.screen = params['screen']
        self.WINDOW_WIDTH = params['windowWidth']
        self.WINDOW_HEIGHT = params['windowHeight']
        self.playspace = pygame.draw.rect(self.screen, (50, 0, 0), [190, 50, 600, 500])
        for i in range(self.blockCount):
            fliper = Fliper(screen=self.screen, background=(255, 0, 0))
            fliper.width = 600 / self.blockCount
            fliper.height = 500 / self.blockCount
            fliper.x = 190 + (fliper.width * i)
            fliper.y = 50
            self.flipers.append(fliper)