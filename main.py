import pygame

from gamestatemachine import GameStateMachine

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Memory Game")

COLORS = {
    "white" : (255, 255, 255),
    "black" : (0, 0, 0),
}

# STATES

GAME_STATE = GameStateMachine(states)

GAME_OVER = False

while not GAME_OVER:

    events = pygame.event.get()
    for event in events:

        if event.type == pygame.QUIT:
            GAME_OVER = True

pygame.quit()
quit()