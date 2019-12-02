# pong usando a biblioteca turtle

import turtle

janela = turtle.Screen()
janela.title("Ping Pong")
janela.bgcolor("black")
janela.setup(width= 800, height= 600)
janela.tracer(0)

# criação das raquetes e a bola da pong
# raquete a
raquete_a = turtle.Turtle()
raquete_a.speed(0)
raquete_a.shape("square")
raquete_a.color("white")
raquete_a.shapesize(stretch_len= 1, stretch_wid= 5)
raquete_a.penup()
raquete_a.goto(-350, 0)

# raquete b
raquete_b = turtle.Turtle()
raquete_b.speed(0)
raquete_b.shape("square")
raquete_b.color("white")
raquete_b.shapesize(stretch_len= 1, stretch_wid= 5)
raquete_b.penup()
raquete_b.goto(350, 0)

# bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 2
bola.dy = -2

# placar do jogo
placar = turtle.Turtle()
placar.speed(0)
placar.penup()
placar.color("white")
placar.goto(0, 260)



# placar
pontuacao_a = 0
pontuacao_b = 0

# movimentando as raquetes
# mover raquete a para cima
def mover_a_para_cima():
    y = raquete_a.ycor()
    if y > 250:
        y = 250
    else:
        y += 20
    raquete_a.sety(y)

# mover raquete a para baixo
def mover_a_para_baixo():
    y = raquete_a.ycor()
    y -= 20
    raquete_a.sety(y)


# mover raquete b para cima
def mover_b_para_cima():
    y = raquete_b.ycor()
    y += 20
    raquete_b.sety(y)

# mover raquete b para baixo
def mover_b_para_baixo():
    y = raquete_b.ycor()
    y -= 20
    raquete_b.sety(y)

# entrada do teclado
janela.listen()
janela.onkeypress(mover_a_para_cima,"w")
janela.onkeypress(mover_a_para_baixo,"s")
janela.onkeypress(mover_b_para_cima,"Up")
janela.onkeypress(mover_b_para_baixo,"Down")


#loop principal
# enquanto o jogo estiver rodando executa este loop
while True:
    janela.update()

    # movendo a bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # check das bordas do jogo
    # se a coordenada y alcançar a borda, seta novamente para coordenada e multiplica 
    # por -1 para inverter a direção
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1
    
    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    if bola.xcor() > 390:
        bola.goto(0,0)
        bola.dx *= -1
        pontuacao_a += 1
        placar.clear()
    
    if bola.xcor() < -390:
        bola.goto(0,0)
        bola.dx *= -1
        pontuacao_b += 1
        placar.clear()

    # colisão com a bola, checa se a raquete entrou em contato com a bola
    # verifica se a bola tocou a raquete 340, mas não passou por ela 350
    # e compara a altura da bola com a altura da raquete, neste caso dando um margem de 40px
    if (bola.xcor() > 340 and bola.xcor() < 350 ) and (bola.ycor() < raquete_b.ycor() + 40 and bola.ycor() > raquete_b.ycor() - 40):
        bola.setx(340)
        bola.dx *= -1

    # faz o mesmo check para a raquete a (da esquerda)
    if (bola.xcor() < -340 and bola.xcor() > -350 ) and (bola.ycor() < raquete_a.ycor() + 40 
    and bola.ycor() > raquete_a.ycor() - 40):
        bola.setx(-340)
        bola.dx *= -1

    # atualização de placar
    placar.write("Jogador 1: {} Jogador 2: {}".format(pontuacao_a, pontuacao_b), 
        align= "center", font=("Courier", 24, "normal") )