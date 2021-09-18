import pygame

from states.basestate import Base

from classes.fliper import Fliper

from functions import *

class Play(Base):

    def __init__(self):
        
        # self.fliper = Fliper()    
        pass

    def render(self) :
        self.fliper.render()
    def update(self, params) :

        self.fliper.update()
        self.render()

    def enter(self, **params):
        self.GAME_STATE = params['gameState']
        self.screen = params['screen']
        self.WINDOW_WIDTH = params['windowWidth']
        self.WINDOW_HEIGHT = params['windowHeight']
        self.fliper = Fliper(screen=self.screen, background=(255, 0, 0))