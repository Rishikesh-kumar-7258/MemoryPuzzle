import pygame

def Write(screen, text="text", x=0, y=0, color=(255, 255, 255), background=(0, 0, 0), size=24, center=False):

    font = pygame.font.SysFont("Comic Sans MS", size)
    txt = font.render(text, True, color, background)
    textRect = txt.get_rect()
    if center: textRect.center = (x,y)
    else:
        textRect.x = x
        textRect.y = y
    screen.blit(txt, textRect)