import turtle
import time
import random
from tkinter import *

posponer = 0.1

# Variables per els marcadors
score = 0
high_score = 0

# Variables per les posicions
x = -1
y = -1


# Generem finestra
wn = turtle.Screen()
wn.title("SNAKE")
wn.bgcolor("beige")
wn.setup(width=620, height=620)

# El tracer fa les animacions més suaus
wn.tracer(0)


# Descripció de tutorial
texto1 = turtle.Turtle()
texto1.speed(0)
texto1.color("black")
texto1.penup()
texto1.hideturtle()
texto1.goto(0, 200)
texto1.write("Premeu qualsevol tecla per començar el joc",
             align="center", font=("Helvetica", 20, "bold"))

# TEXTO
texto2 = turtle.Turtle()
texto2.speed(0)
texto2.color("black")
texto2.penup()
texto2.hideturtle()
texto2.goto(0, 100)
texto2.write("Premeu < cap a ESQUERRA",
             align="center", font=("Helvetica", 30, "bold"))


# TEXTO
texto3 = turtle.Turtle()
texto3.speed(0)
texto3.color("black")
texto3.penup()
texto3.hideturtle()
texto3.goto(0, 0)
texto3.write("Premeu > cap a DRETA",
             align="center", font=("Helvetica", 30, "bold"))


# TEXTO
texto4 = turtle.Turtle()
texto4.speed(0)
texto4.color("black")
texto4.penup()
texto4.hideturtle()
texto4.goto(0, -100)
texto4.write("Premeu ^ cap a DALT",
             align="center", font=("Helvetica", 30, "bold"))


# TEXTO
texto5 = turtle.Turtle()
texto5.speed(0)
texto5.color("black")
texto5.penup()
texto5.hideturtle()
texto5.goto(0, -200)
texto5.write("Premeu v cap a BAIX",
             align="center", font=("Helvetica", 30, "bold"))


# Cos de la serp (segments)
segmentos = []
# Bloques
bloques = []
# Fronteres
borderList = []

# posició dels elements
PosRed = set()
PosOrange = set()
PosGreen = set()
Posbloques = set()


# PAS 4
def arriba():
    cabeza.direction = "up"


def abajo():
    cabeza.direction = "down"


def izquierda():
    cabeza.direction = "left"


def derecha():
    cabeza.direction = "right"


def cualquiera():
    cabeza.direction = "up"


# TECLAT - Connectarem el moviment amb el nostre teclat
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")
wn.onkeypress(cualquiera)


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


def gameOver(score):
    # fi del joc

    # time.sleep(1)

    # La serp torna al punt de partida
    cabeza.goto(0, 0)
    cabeza.direction = "stop"

    # Esborra tots els blocs
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

    # finestra nova per la continuació del joc
    root = Tk()
    root.title("GAMEOVER")
    root.geometry("250x250")
    root.eval('tk::PlaceWindow . center')

    Label(root,
          text=f"Score: {score}",
          font=("Helvetica", 14, "bold")
          ).grid(row=2, column=2, pady=25, padx=80)

    Label(root,
          text=f"High Score: {high_score}",
          font=("Helvetica", 14, "bold")
          ).grid(row=6, column=2, pady=25, padx=60)

    Button(root,
           text="Continue",
           command=root.destroy,
           font=("Helvetica", 14, "bold"),
           fg='black'
           ).grid(row=10, column=2, pady=25, padx=80)

    score = 0
    return score


def textoWrite(texto, score, high_score):
    texto.clear()
    texto.write(" Score:{}     High Score:{}".format(score, high_score), align="center",
                font=("Courier", 24, "normal"))


cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("LightSkyBlue")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "stop"

# esperant que comenci el joc
while cabeza.direction == "stop":
    wn.update()
    mov()

# Amaga el tutorial
for text in [texto1, texto2, texto3, texto4, texto5]:
    text.clear()

# dibuixa la frontera
for i in range(int(-280/20), int(300/20)):
    borderTop = turtle.Turtle()
    borderTop.speed(0)
    borderTop.shape("square")
    borderTop.color("black")
    borderTop.penup()
    borderTop.goto(i*20, 280)
    borderList.append(borderTop)

    borderBottom = turtle.Turtle()
    borderBottom.speed(0)
    borderBottom.shape("square")
    borderBottom.color("black")
    borderBottom.penup()
    borderBottom.goto(i*20, -280)
    borderList.append(borderBottom)

    borderLeft = turtle.Turtle()
    borderLeft.speed(0)
    borderLeft.shape("square")
    borderLeft.color("black")
    borderLeft.penup()
    borderLeft.goto(-280, i*20)
    borderList.append(borderLeft)

    borderRight = turtle.Turtle()
    borderRight.speed(0)
    borderRight.shape("square")
    borderRight.color("black")
    borderRight.penup()
    borderRight.goto(280, i*20)
    borderList.append(borderRight)


# ComidaRed
red = turtle.Turtle()
red.speed(0)
red.shape("circle")
red.color("red")
red.penup()
red.goto(random.randint(-260/20, 260/20)*20,
         random.randint(-260/20, 260/20)*20)

# ComidaOrange
orange = turtle.Turtle()
orange.speed(0)
orange.shape("circle")
orange.color("orange")
orange.penup()
orange.goto(random.randint(-260/20, 260/20)*20,
            random.randint(-260/20, 260/20)*20)

# ComidaGreen
green = turtle.Turtle()
green.speed(0)
green.shape("circle")
green.color("green")
green.penup()
green.goto(random.randint(-260/20, 260/20)*20,
           random.randint(-260/20, 260/20)*20)

# TEXTO
texto = turtle.Turtle()
texto.speed(0)
texto.color("black")
texto.penup()
texto.hideturtle()
texto.goto(0, 235)
texto.write("Score: 0       High Score:  0",
            align="center", font=("Courier", 24, "normal"))

# Bucle principal (la finestra s'anirà actualitzant constantment)
while True:
    wn.update()

    # PAS 9: Colisiones bordes
    if cabeza.xcor() > 260 or cabeza.xcor() < -260 or cabeza.ycor() > 260 or cabeza.ycor() < -260:
        score = gameOver(score)

    # Colisiones con el bloques
    for bloque in bloques:
        if cabeza.distance(bloque) < 20:
            score = gameOver(score)

    # Colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            score = gameOver(score)

    # El nou joc actualitza la puntuació del joc anterior
    if score == 0:
        textoWrite(texto, score, high_score)

    # El quadrat fa 20 píxel x 20 píxels i el cercle igual de radi
    # Si toca  amb vermell
    if cabeza.distance(red) < 20:

        # Canvia les posicions per vermell
        PosRed.clear()
        while True:
            x = random.randint(-260/20, 260/20)*20
            y = random.randint(-260/20, 260/20)*20
            # Assegurem-nos que no estigui al mateix lloc amb altres colors i bloques
            if (x, y) not in PosOrange and (x, y) not in Posbloques and (x, y) not in PosGreen:
                red.goto(x, y)
                PosRed.add((x, y))
                break

        # Canvia les posicions per taronja
        PosOrange.clear()
        while True:
            x = random.randint(-260/20, 260/20)*20
            y = random.randint(-260/20, 260/20)*20
            # Assegurem-nos que no estigui al mateix lloc amb altres colors i bloques
            if (x, y) not in PosOrange and (x, y) not in Posbloques and (x, y) not in PosGreen:
                orange.goto(x, y)
                PosOrange.add((x, y))
                break

        # Canvia les posicions per verd
        PosGreen.clear()
        while True:
            x = random.randint(-260/20, 260/20)*20
            y = random.randint(-260/20, 260/20)*20
            # Assegurem-nos que no estigui al mateix lloc amb altres colors i bloques
            if (x, y) not in PosOrange and (x, y) not in Posbloques and (x, y) not in PosRed:
                green.goto(x, y)
                PosGreen.add((x, y))
                break

        # Actualitzar marcador
        score -= 10
        if score > high_score:
            high_score = score

        # Per anar eliminant un segmento a la llista cada vegada que hi hagi contacte
        if len(segmentos) > 0:
            # Selecciona l'última segment del cos i suprimix
            lastone = segmentos[-1]
            segmentos.pop()
            lastone.goto(1000, 1000)
            lastone.clear()
        else:
            score = gameOver(score)

        # Resetear marcador
        textoWrite(texto, score, high_score)

    # Si toca  amb verd
    if cabeza.distance(green) < 20:

        # Canvia les posicions per verd
        PosGreen.clear()
        while True:
            x = random.randint(-260/20, 260/20)*20
            y = random.randint(-260/20, 260/20)*20
            # Assegurem-nos que no estigui al mateix lloc amb altres colors i bloques
            if (x, y) not in PosOrange and (x, y) not in Posbloques and (x, y) not in PosRed:
                green.goto(x, y)
                PosGreen.add((x, y))
                break

        # Si el bloc existeix, almenys un
        if len(bloques):
            # Selecciona un bloc aleatòriament
            bloque = bloques[random.randint(0, len(bloques)-1)]

            # Elimina des de posbloques
            Posbloques.remove((bloque.position()[0], bloque.position()[1]))
            bloques.remove(bloque)

            # I eliminar-lo
            bloque.goto(1000, 1000)
            bloque.clear()

        # Actualitzar marcador
        score -= 10
        if score > high_score:
            high_score = score

        # Resetear marcador
        textoWrite(texto, score, high_score)

    # Si toca  amb taronge
    if cabeza.distance(orange) < 20:

        # Canvia les posicions per taronge
        PosOrange.clear()
        while True:
            x = random.randint(-260/20, 260/20)*20
            y = random.randint(-260/20, 260/20)*20
            # Assegurem-nos que no estigui al mateix lloc amb altres colors i bloques
            if (x, y) not in PosOrange and (x, y) not in Posbloques and (x, y) not in PosGreen:
                orange.goto(x, y)
                PosOrange.add((x, y))
                break

        # crear un nou cos
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("LightSkyBlue1")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        score += 20
        if score > high_score:
            high_score = score

        # Resetear marcador
        textoWrite(texto, score, high_score)

        Bloque1 = turtle.Turtle()
        Bloque1.speed(0)
        Bloque1.shape("square")
        Bloque1.color("black")
        Bloque1.penup()

        while True:
            x = random.randint(-260/20, 260/20)*20
            y = random.randint(-260/20, 260/20)*20
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

    # Mover el cabezal de la serpiente
    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

    mov()

    time.sleep(posponer)
