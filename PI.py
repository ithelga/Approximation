# Created by Helga on 02.10.2020

from tkinter import *
from random import uniform
from math import *

R = 150
width = 2 * R
hight = 2 * R
n = 10000


# Создаем окно программы
window = Tk()

# Создаем область для рисования
c = Canvas(window, width=4 * R, height=4 * R, bg="black")
c.pack()

center = 2 * R
c.create_rectangle(center - R, center - R, center + R, center + R, fill="black")
c.create_oval(center - R, center - R, center + R, center + R, fill="black")

def create_point(x, y, color, line):
    c.create_oval(center + x + 1, center + y + 1, center + x - 1, center + y - 1, fill= color,
                         outline=line)

def calc_points(n): #определяем параметры случайных точек
    ncircl1 = 0
    lst = []
    for i in range(0, n):
        x = uniform(-R, R)
        y = uniform(-R, R)
        if sqrt(x ** 2 + y ** 2) < R:
            ncircl1 += 1
            color = "medium violet red"
        else:
            color = "pink"
        lst.append((x,y,color))
    return lst, ncircl1


def draw_point():
    if points:
        x,y,color = points.pop() #срезаем параметры одной точки для отрисовки
        create_point(x, y, color, color)
        window.after(1, draw_point)
    else:
        print('all points')
        c.create_text(150, 500, anchor=W, font="Arial",
                      text=f"Аппроксимация пи: {pi}",fill="white" )


points, ncircl = calc_points(n)
print(points)


''' вероятность определяет количестсво точек которые попали внутрь радиуса деленные на все точки 
сторона квадрата width = 2R
Геометрически:
P = S(круга) / S(квадрата) = πR^2 / width^2 = πR^2 / (2R)^2 = π / 4
Монте Карло:
P = S(точек в круге) / S(точек в квадрате) = π / 4

'''
pi = ncircl / n * 4
print(pi)
window.title("PI")
window.after(1, draw_point) #метод для отрисовки с задержкой
window.mainloop()
