import pygame
import math

pygame.init()

ventana = pygame.display.set_mode((1280,720))

sprite_nave = pygame.image.load('nave.png')
posnave = [0,0]
rotnave = 0

while True:
    ventana.fill((0,0,0))
    pygame.event.pump()
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP]:
        posnave[0] += math.cos(math.radians(rotnave))
        posnave[1] -= math.sin(math.radians(rotnave))
    rotnave += tecla[pygame.K_LEFT]
    rotnave -= tecla[pygame.K_RIGHT]
    rotado = pygame.transform.rotate(sprite_nave,rotnave)
    ventana.blit(rotado,posnave)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
