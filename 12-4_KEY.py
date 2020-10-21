import pygame

pygame.init()
screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption("游戏")
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print(event.key)
