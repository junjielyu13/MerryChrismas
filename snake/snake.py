import turtle
import time
import random
from tkinter import *

posponer = 0.1

# Variables per els marcadors
score = 0
high_score = 0


# Generem finestra
wn = turtle.Screen()
wn.title("SNAKE")
wn.bgcolor("beige")
wn.setup(width=600, height=600)

# El tracer fa les animacions més suaus
wn.tracer(0)

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(random.randint(-280, 280), random.randint(-280, 280))

# Comida1
comida1 = turtle.Turtle()
comida1.speed(0)
comida1.shape("circle")
comida1.color("orange")
comida1.penup()
comida1.goto(random.randint(-280, 280), random.randint(-280, 280))

# Cos de la serp (segments)
segmentos = []
# Bloques
bloques = []

# TEXTO
texto = turtle.Turtle()
texto.speed(0)
texto.color("black")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Score: 0       High Score:  0",
            align="center", font=("Courier", 24, "normal"))

# PAS 4


def arriba():
    cabeza.direction = "up"


def abajo():
    cabeza.direction = "down"


def izquierda():
    cabeza.direction = "left"


def derecha():
    cabeza.direction = "right"


# TECLAT - Connectarem el moviment amb el nostre teclat
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

# PAS 3


def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y+20)
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y-20)
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x-20)
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x+20)


# Bucle principal (la finestra s'anirà actualitzant constantment)
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("LightSkyBlue")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "stop"


def GameExit(root):
    # root.destroy
    # time.sleep(0.5)
    # turtle.Screen().bye()
    pass


def gameOver(score):
    time.sleep(1)
    cabeza.goto(0, 0)
    cabeza.direction = "stop"

    for bloque in bloques:
        bloque.goto(1000, 1000)
        bloque.clear()
    bloques.clear()

    # Esconder los segmentos
    for segmento in segmentos:
        segmento.goto(1000, 1000)
        segmento.clear()
    segmentos.clear()

    #game = turtle.Screen()
    # game.title("GAMEOVER")
    # game.bgcolor("beige")
    #game.setup(width=600, height=600)
    # game.tracer(0)

    # Resetear marcador
    texto.clear()
    score = 0
    texto.write(f"Score: {score}       High Score:  {high_score}",
                align="center", font=("Courier", 24, "normal"))

    root = Tk()
    root.title("GAMEOVER")
    root.geometry("250x250")
    root.eval('tk::PlaceWindow . center')
    Label(root, text=f"Score: {score}").grid(row=2, column=0)
    Label(root, text=f"High Score: {high_score}").grid(row=2, column=2)
    Button(root, text=f"Continue", command=root.destroy).grid(row=4, column=1)
    return 0


while True:
    wn.update()

    # PAS 9: Colisiones bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        score = gameOver(score)

    for bloque in bloques:
        if cabeza.distance(bloque) < 20:
            score = gameOver(score)

        # Colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            score = gameOver(score)


# El quadrat fa 20 píxel x 20 píxels i el cercle igual de radi
    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        # Per anar eliminant un segmento a la llista cada vegada que hi hagi contacte
        if len(segmentos) > 0:
            lastone = segmentos[-1]
            segmentos.pop()
            lastone.goto(1000, 1000)
            lastone.clear()
        else:
            score = gameOver(score)

        # Augmentar marcador
        score -= 10
        if score > high_score:
            high_score = score

        texto.clear()
        texto.write("Score: {}       High Score:  {}".format(score, high_score), align="center",
                    font=("Courier", 24, "normal"))

    if cabeza.distance(comida1) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida1.goto(x, y)
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("LightSkyBlue1")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)
        score += 20
        if score > high_score:
            high_score = score
        texto.clear()
        texto.write("Score: {}       High Score:  {}".format(score, high_score), align="center",
                    font=("Courier", 24, "normal"))

        Bloque1 = turtle.Turtle()
        Bloque1.speed(0)
        Bloque1.shape("square")
        Bloque1.color("black")
        Bloque1.penup()
        Bloque1.goto(random.randint(-280, 280), random.randint(-280, 280))

        bloques.append(Bloque1)

    # Mover el cuerpo de la serpiente
    totalSeg = len(segmentos)
    for index in range(totalSeg-1, 0, -1):
        x = segmentos[index-1].xcor()
        y = segmentos[index-1].ycor()
        segmentos[index].goto(x, y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

    mov()

    time.sleep(posponer)
