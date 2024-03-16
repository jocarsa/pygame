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

balas_velocidad = 5
balas = []

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

    if tecla[pygame.K_SPACE]:
            balas.append(
                [
                    posnave[0] + sprite_nave.get_width() / 2,
                    posnave[1] + sprite_nave.get_height() / 2,
                    rotnave
                ]
            )
    for bala in balas:
        bala[0] += balas_velocidad * math.cos(math.radians(bala[2]))
        bala[1] -= balas_velocidad * math.sin(math.radians(bala[2]))
    balas = [bala for bala in balas if 0 <= bala[0] <= ventana.get_width() and 0 <= bala[1] <= ventana.get_height()]
    for bala in balas:
        pygame.draw.circle(ventana, (255, 0, 0), (int(bala[0]), int(bala[1])), 3)

    
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
