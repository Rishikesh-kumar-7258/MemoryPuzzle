import pygame

from gamestatemachine import GameStateMachine
from states.startstate import Start
from states.playstate import Play

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Memory Game")

COLORS = {
    "white" : (255, 255, 255),
    "black" : (0, 0, 0),
}

STATES = {
    "start" : Start(),
    "play" : Play(),
}

GAME_STATE = GameStateMachine(STATES)
GAME_STATE.change("start",
                    screen = SCREEN,
                    colors = COLORS,
                    windowWidth=WINDOW_WIDTH,
                    windowHeight=WINDOW_HEIGHT,
                    gameState=GAME_STATE)

GAME_OVER = False

clock = pygame.time.Clock()

while not GAME_OVER:

    events = pygame.event.get()
    for event in events:

        if event.type == pygame.QUIT:
            GAME_OVER = True
    
    SCREEN.fill(COLORS["black"])
    GAME_STATE.update(events)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
quit()