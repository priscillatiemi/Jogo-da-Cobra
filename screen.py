import pygame
import random
import time

pygame.init()
dis_width = 800
dis_heigth = 600
dis = pygame.display.set_mode((dis_width,dis_heigth))
pygame.display.set_caption('Snake Game')

rosa = (255,182,193)
azul = (0,0,255)
branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)



blocos = 10



tempo = pygame.time.Clock()
velocidade = 20

font_style = pygame.font.SysFont(None, 30)

def mensagem(msg, cor):
    mensg = font_style.render(msg, True, cor)
    dis.blit(mensg, [dis_width/3, dis_heigth/3])

def game_loop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_heigth / 2

    x1_mover = 0
    y1_mover = 0

    comida_x = round(random.randrange(0, dis_width - blocos) / 10.0) * 10.
    comida_y  = round(random.randrange(0, dis_width - blocos) / 10.0) * 10.

    while not game_over:
        while game_close == True:
            dis.fill(branco)
            mensagem("Você perdeu! Aperte Q - Quit ou C - Jogar novamente", vermelho)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if evento.key == pygame.K_c:
                        game_loop()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_mover = -blocos
                    y1_mover = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_mover = blocos
                    y1_mover = 0
                elif evento.key == pygame.K_UP:
                    y1_mover = -blocos
                    x1_mover = 0
                elif evento.key == pygame.K_DOWN:
                    y1_mover = blocos
                    x1_mover = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_heigth or y1 < 0:
            game_close = True

        x1 += x1_mover
        y1 += y1_mover
        dis.fill(preto)
        pygame.draw.rect(dis, azul, [comida_x, comida_y, blocos, blocos])
        pygame.draw.rect(dis, rosa, [x1, y1, blocos, blocos])
        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            print("Que gostoso!")
        tempo.tick(velocidade)


    pygame.quit()
    quit()
game_loop()
