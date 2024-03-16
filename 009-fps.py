import pygame

pygame.init()

ventana = pygame.display.set_mode((1280,720))

sprite_nave = pygame.image.load('nave.png')
posnave = (0,0)

bucle = True

while bucle:
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP]:
        posnave[1] -= 1
    if tecla[pygame.K_DOWN]:
        posnave[1] += 1
    if tecla[pygame.K_LEFT]:
        posnave[0] -= 1
    if tecla[pygame.K_RIGHT]:
        posnave[0] += 1
    ventana.blit(sprite_nave,posnave)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
