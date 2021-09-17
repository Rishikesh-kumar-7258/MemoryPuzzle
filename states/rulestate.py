import pygame

from states.basestate import Base
from functions import *

class Rules(Base):

    def __init__(self): pass

    def render(self) : 
        Write(self.screen, text="some instructions")


    def update(self, params) :

        self.render()
    
    def enter(self, **params):
        self.screen = params['screen']