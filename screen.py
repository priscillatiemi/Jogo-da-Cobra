import pygame

pygame.init()
dis = pygame.display.set_mode((800,600))
pygame.display.set_caption('Snake Game')

rosa = (255,182,193)
azul = (0,0,255)
branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)


game_over = False

x1 = 300
y1 = 300

x1_mover = 0
y1_mover = 0

tempo = pygame.time.Clock()


while not game_over:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game_over = True
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                x1_mover = -10
                y1_mover = 0
            elif evento.key == pygame.K_RIGHT:
                x1_mover = 10
                y1_mover =  0
            elif evento.key == pygame.K_UP:
                y1_mover = -10
                x1_mover = 0
            elif evento.key == pygame.K_DOWN:
                y1_mover = 10
                x1_mover = 0

    x1 += x1_mover
    y1 += y1_mover
    dis.fill(preto)

    pygame.draw.rect(dis,rosa,[x1,y1,10,10])
    pygame.display.update()
    tempo.tick(30)
pygame.quit()
quit()

