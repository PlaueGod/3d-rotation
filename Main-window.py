import tkinter as tk
import turtle
from turtledemo.forest import symRandom

# main_window = tk.Tk()
# main_window.title("My GUI")
# main_window.configure(background="white")
# main_window.minsize(700, 700)
# main_window.maxsize(700, 700)
# main_window.geometry("700x700")
# main_window.mainloop()

turtle.bgcolor("white")
turtle.pencolor("blue")


turtle.teleport(-300,-300)
for i in range(20):
        turtle.pensize(10)
        turtle.speed(50)
        turtle.fd(700)
        turtle.left(120)


turtle.teleport(35,-480)

for i in range(20):
        turtle.pensize(10)
        turtle.speed(50)
        turtle.back(700)
        turtle.left(120)




