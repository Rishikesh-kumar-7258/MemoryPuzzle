import pygame

from states.basestate import Base
from functions import *

class Start(Base):

    def __init__(self):
        self.screen = None

    def render(self) :
        Write(self.screen)

    def update(self) : pass

    def enter(self, params):
        self.screen = params[SCREEN]