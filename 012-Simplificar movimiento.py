import pygame

pygame.init()

ventana = pygame.display.set_mode((1280,720))

sprite_nave = pygame.image.load('nave.png')
posnave = [0,0]

while True:
    ventana.fill((0,0,0))
    pygame.event.pump()
    tecla = pygame.key.get_pressed()
    posnave[1] -= tecla[pygame.K_UP]
    posnave[1] += tecla[pygame.K_DOWN]
    posnave[0] -= tecla[pygame.K_LEFT]
    posnave[0] += tecla[pygame.K_RIGHT]
    ventana.blit(sprite_nave,posnave)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
