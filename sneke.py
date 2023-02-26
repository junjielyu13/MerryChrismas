import turtle
import time
import random
from tkinter import *

posponer = 0.1

# Variables per els marcadors
score = 0
high_score = 0
x = -1
y = -1


# Generem finestra
wn = turtle.Screen()
wn.title("SNAKE")
wn.bgcolor("beige")
wn.setup(width=600, height=600)

# El tracer fa les animacions més suaus
wn.tracer(0)


# Comida
red = turtle.Turtle()
red.speed(0)
red.shape("circle")
red.color("red")
red.penup()
red.goto(random.randint(-280/20, 280/20)*20,
         random.randint(-280/20, 280/20)*20)

# Comida1
orange = turtle.Turtle()
orange.speed(0)
orange.shape("circle")
orange.color("orange")
orange.penup()
orange.goto(random.randint(-280/20, 280/20)*20,
            random.randint(-280/20, 280/20)*20)

# Comida1
green = turtle.Turtle()
green.speed(0)
green.shape("circle")
green.color("green")
green.penup()
green.goto(random.randint(-280/20, 280/20)*20,
           random.randint(-280/20, 280/20)*20)

# Cos de la serp (segments)
segmentos = []
# Bloques
bloques = []

# position of elements
PosRed = set()
PosOrange = set()
PosGreen = set()
Posbloques = set()

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

    # Resetear marcador
    textoWrite(texto, score, high_score)

    root = Tk()
    root.title("GAMEOVER")
    root.geometry("250x250")
    root.eval('tk::PlaceWindow . center')

    Label(root,
          text=f"Score: {score}",
          font=("Inter", 14)
          ).grid(row=2, column=2, pady=25, padx=80)

    Label(root,
          text=f"High Score: {high_score}",
          font=("Inter", 14)
          ).grid(row=6, column=2, pady=25, padx=60)

    Button(root,
           text="Continue",
           command=root.destroy,
           font=("Inter", 14),
           fg='black'
           ).grid(row=10, column=2, pady=25, padx=80)

    return 0


def textoWrite(texto, score, high_score):
    texto.clear()
    texto.write("Score:{}      High Score:{}".format(score, high_score), align="center",
                font=("Courier", 24, "normal"))


while True:
    wn.update()

    if score == 0:
        textoWrite(texto, score, high_score)

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
    if cabeza.distance(red) < 20:

        PosRed.clear()
        while True:
            x = random.randint(-280/20, 280/20)*20
            y = random.randint(-280/20, 280/20)*20
            if (x, y) not in PosOrange and (x, y) not in Posbloques and (x, y) not in PosGreen:
                red.goto(x, y)
                PosRed.add((x, y))
                break

        PosOrange.clear()
        while True:
            x = random.randint(-280/20, 280/20)*20
            y = random.randint(-280/20, 280/20)*20
            if (x, y) not in PosOrange and (x, y) not in Posbloques and (x, y) not in PosGreen:
                orange.goto(x, y)
                PosOrange.add((x, y))
                break

        PosGreen.clear()
        while True:
            x = random.randint(-280/20, 280/20)*20
            y = random.randint(-280/20, 280/20)*20
            if (x, y) not in PosOrange and (x, y) not in Posbloques and (x, y) not in PosRed:
                green.goto(x, y)
                PosGreen.add((x, y))
                break

        # Per anar eliminant un segmento a la llista cada vegada que hi hagi contacte
        if len(segmentos) > 0:
            lastone = segmentos[-1]
            segmentos.pop()
            lastone.goto(1000, 1000)
            lastone.clear()
        else:
            score = 0
            score = gameOver(score)

        # Augmentar marcador
        score -= 10
        if score > high_score:
            high_score = score

        textoWrite(texto, score, high_score)

    if cabeza.distance(green) < 20:
        PosGreen.clear()
        while True:
            x = random.randint(-280/20, 280/20)*20
            y = random.randint(-280/20, 280/20)*20
            if (x, y) not in PosOrange and (x, y) not in Posbloques and (x, y) not in PosRed:
                green.goto(x, y)
                PosGreen.add((x, y))
                break

        # Bloques
        if len(bloques):
            bloque = bloques[random.randint(0, len(bloques)-1)]

            Posbloques.remove((bloque.position()[0], bloque.position()[1]))
            bloques.remove(bloque)
            bloque.goto(1000, 1000)
            bloque.clear()

        score -= 10
        if score > high_score:
            high_score = score

        textoWrite(texto, score, high_score)

    if cabeza.distance(orange) < 20:

        PosOrange.clear()
        while True:
            x = random.randint(-280/20, 280/20)*20
            y = random.randint(-280/20, 280/20)*20
            if (x, y) not in PosOrange and (x, y) not in Posbloques and (x, y) not in PosGreen:
                orange.goto(x, y)
                PosOrange.add((x, y))
                break

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("LightSkyBlue1")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        if score < 0:
            score = 20
        else:
            score += 20
        if score > high_score:
            high_score = score

        textoWrite(texto, score, high_score)

        Bloque1 = turtle.Turtle()
        Bloque1.speed(0)
        Bloque1.shape("square")
        Bloque1.color("black")
        Bloque1.penup()

        while True:
            x = random.randint(-280/20, 280/20)*20
            y = random.randint(-280/20, 280/20)*20
            if (x, y) not in PosRed and (x, y) not in PosOrange and (x, y) not in PosGreen:
                Bloque1.goto(x, y)
                Posbloques.add((x, y))
                break

        Bloque1.goto(x, y)
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
