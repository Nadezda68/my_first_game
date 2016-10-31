# coding: utf-8

import turtle
import random
import sys


def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_line(from_x, from_y, to_x, to_y):
    gotoxy(from_x, from_y)
    turtle.goto(to_x, to_y)


def draw_gibbet(step):
    turtle.color("blue")
    if step == 1:
        # вертикальная балка
        draw_line(-160, -100, -160, 80)
    elif step == 2:
        # горизонтальная балка
        draw_line(-160, 80, -80, 80)
    elif step == 3:
        # ребро жесткости
        draw_line(-160, 40, -120, 80)
    elif step == 4:
        # веревка
        draw_line(-80, 80, -80, 40)
    elif step == 5:
        # голова
        gotoxy(-80, 0)
        turtle.circle(20)
    elif step == 6:
        # туловище
        draw_line(-80, 0, -80, -50)
    elif step == 7:
        # левая рука
        draw_line(-80, -10, -100, -20)
    elif step == 8:
        # правая рука
        draw_line(-80, -10, -60, -20)
    elif step == 9:
        # левая нога
        draw_line(-80, -50, -100, -60)
    elif step == 10:
        # правая нога
        draw_line(-80, -50, -60, -60)


x = random.randint(1, 100)
print(x)

gotoxy(-350, 250)
turtle.write("Я загадал число от 1 до 100. Попробуй угадать!",
             font=("Arial", 18, "normal"))

try_count = 0

answer = turtle.textinput("Хотите играть?", "Y/N")
if answer == 'N':
    sys.exit(77)

answer = turtle.textinput("Давать подсказки?", "Y/N")
hints = False
if answer == 'Y':
    hints = True

while True:
    number = turtle.numinput("Попробуй угадать", "Число", 0, 1, 100)
    if number == x:
        gotoxy(-150, -200)
        turtle.write("Ура! Вы победили", font=("Arial", 28, "normal"))
        break
    else:
        turtle.color('red')
        gotoxy(-150, 100)
        turtle.write("Неверно!", font=("Arial", 20, "normal"))
        try_count += 1
        draw_gibbet(try_count)

        if try_count == 10:
            turtle.color("black")
            gotoxy(-150, -80)
            turtle.write("Александер вы проиграли!", font=("Arial", 20, "normal"))
            break

    if hints:
        gotoxy(200, 200 - try_count * 11)
        if number < x:
            turtle.write(str(number) + " Загаданное число больше",font=("Arial", 8, "normal"))
        else:
            turtle.write(str(number) + " Загаданное число меньше")

input('Нажмите любую клавишу')