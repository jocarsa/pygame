import pygame
import math

pygame.init()

ventana = pygame.display.set_mode((1280,720))

sprite_nave = pygame.image.load('nave.png')
posnave = [0,0]
rotnave = 0
velocidad= [0,0]
aceleracion = 0.1
friccion = 0.02

while True:
    ventana.fill((0,0,0))
    pygame.event.pump()
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP]:
        velocidad[0] += aceleracion*math.cos(math.radians(rotnave))
        velocidad[1] -= aceleracion*math.sin(math.radians(rotnave))
    else:
        velocidad[0] *= (1-friccion)
        velocidad[1] *= (1-friccion)
    posnave[0] += velocidad[0]
    posnave[1] += velocidad[1]
    
    rotnave += tecla[pygame.K_LEFT]
    rotnave -= tecla[pygame.K_RIGHT]
    rotado = pygame.transform.rotate(sprite_nave,rotnave)
    ventana.blit(rotado,posnave)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
