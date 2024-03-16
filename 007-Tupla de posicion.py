import pygame

pygame.init()

ventana = pygame.display.set_mode((1280,720))

sprite_nave = pygame.image.load('nave.png')
posnave = (0,0)

while True:
    tecla = pygame.key.get_pressed()
    
    ventana.blit(sprite_nave,posnave)
    pygame.display.flip()

pygame.quit()
