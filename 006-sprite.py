import pygame

pygame.init()

ventana = pygame.display.set_mode((1280,720))

sprite_nave = pygame.image.load('nave.png')
posnave = (0,0)

while True:
    ventana.blit(sprite_nave,(0,0))
    pygame.display.flip()

pygame.quit()
