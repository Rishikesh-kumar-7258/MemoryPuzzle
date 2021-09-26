import pygame
import random

def Write(screen, text="text", x=0, y=0, color=(255, 255, 255), background=(0, 0, 0), size=24, center=False):

    font = pygame.font.SysFont("Comic Sans MS", size)
    txt = font.render(text, True, color, background)
    textRect = txt.get_rect()
    if center: textRect.center = (x,y)
    else:
        textRect.x = x
        textRect.y = y
    screen.blit(txt, textRect)


def shuffle(arr) -> list():
    n = len(arr)
    for i in range(n-1):
        temp = random.randint(i+1, n-1)
        arr[i] = arr[i] ^ arr[temp]
        arr[temp] = arr[i] ^ arr[temp]
        arr[i] = arr[i] ^ arr[temp]
    
    return arr