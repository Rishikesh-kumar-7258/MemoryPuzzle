import pygame
from pygame.constants import KEYDOWN, SRCALPHA

from states.basestate import Base

from classes.fliper import Fliper

from functions import *

class Play(Base):

    def __init__(self):
        
        self.level = 1
        self.blockCount = 3
        self.flipers = []

        self.selected = 0
        self.current = None
        self.previous = None

    def render(self) :
        self.playspace = pygame.draw.rect(self.screen, (50, 0, 0), [190, 50, 600, 500])
        for fliper in self.flipers:
            fliper.render()
        
        selectbox = self.flipers[self.selected]
        tempbox = pygame.Surface((selectbox.width, selectbox.height), SRCALPHA)
        tempbox.set_colorkey(self.colors["black"])
        tempbox.set_alpha(120)
        pygame.draw.rect(tempbox, self.colors["green"], tempbox.get_rect(), 10)

        self.screen.blit(tempbox, (selectbox.x, selectbox.y))


    def update(self, params) :

        for event in params:
            if event.type == KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.selected = self.selected - 1 if (self.selected > 0) else self.selected
                if event.key == pygame.K_RIGHT:
                    self.selected = self.selected + 1 if self.selected < self.blockCount*4 - 1 else self.selected
                if event.key == pygame.K_UP:
                    self.selected = self.selected - 4 if self.selected > 3 else self.selected
                if event.key == pygame.K_DOWN:
                    self.selected = self.selected + 4 if self.selected < (self.blockCount-1)*4 else self.selected
                if event.key == pygame.K_SPACE:
                    self.current = self.flipers[self.selected]
                    self.current.isflip = True
                print(self.selected)
                
        self.render()

    def enter(self, **params):
        self.colors = params["colors"]
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