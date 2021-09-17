import pygame

from states.basestate import Base

from classes.changer import Changer
from functions import *

class Start(Base):

    def __init__(self):
        
        self.changer = Changer()
        

    def render(self) :
        Write(self.screen, "Memory Game", self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2, size=110, center=True)
        self.changer.render()

    def update(self, params) :

        for event in params:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.GAME_STATE.change(self.changer.actions[self.changer.current],
                                            screen = self.screen,
                                            colors = self.colors,
                                            windowWidth=self.WINDOW_WIDTH,
                                            windowHeight=self.WINDOW_HEIGHT,
                                            gameState=self.GAME_STATE)

        self.changer.update(params)
        self.render()

    def enter(self, **params):
        self.colors = params['colors']
        self.GAME_STATE = params['gameState']
        self.screen = params['screen']
        self.WINDOW_WIDTH = params['windowWidth']
        self.WINDOW_HEIGHT = params['windowHeight']
        self.changer = Changer(x=self.WINDOW_WIDTH // 2 - self.changer.width//2, y=self.WINDOW_HEIGHT//2 + 200, screen=self.screen)
        self.changer.passed = params
        self.changer.color = self.colors['green']
        self.changer.actions = ["play", "rules"]
        self.changer.gameState = self.GAME_STATE