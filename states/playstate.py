import pygame

from states.basestate import Base

from classes.changer import Changer
from functions import *

class Play(Base):

    def __init__(self):
        
        self.changer = Changer()
        

    def render(self) :
        Write(self.screen, "Play", self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2, size=110, center=True)
        self.changer.render()

    def update(self, params) :

        self.changer.update(params)
        self.render()

    def enter(self, **params):
        self.GAME_STATE = params['gameState']
        self.screen = params['screen']
        self.WINDOW_WIDTH = params['windowWidth']
        self.WINDOW_HEIGHT = params['windowHeight']
        self.changer = Changer(x=self.WINDOW_WIDTH // 2, y=self.WINDOW_HEIGHT//2 + 200, screen=self.screen)
        self.changer.actions = ["play"]
        self.changer.gameState = self.GAME_STATE