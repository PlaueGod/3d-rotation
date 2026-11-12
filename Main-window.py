import tkinter as tk
import turtle
import random


# ОКНО ОБЫЧНОЕ
# main_window = tk.Tk()
# main_window.title("My GUI")
# main_window.configure(background="white")
# main_window.minsize(700, 700)
# main_window.maxsize(700, 700)
# main_window.geometry("700x700")
# main_window.mainloop()

showturtle = turtle.Turtle()



turtle.bgcolor("green")
for i in range(random.randint(10,20)):
    turtle.begin_fill()
    for c in ('yellow','blue'):
        turtle.pensize(4)
        turtle.color(c)
        turtle.speed(20)
        turtle.fd(300)
        turtle.rt(201)
    turtle.end_fill()




