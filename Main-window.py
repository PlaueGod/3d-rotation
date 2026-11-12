import tkinter as tk
import turtle

# main_window = tk.Tk()
# main_window.title("My GUI")
# main_window.configure(background="white")
# main_window.minsize(700, 700)
# main_window.maxsize(700, 700)
# main_window.geometry("700x700")
# main_window.mainloop()



turtle.bgcolor("green")
for i in range(15):
    for c in ('red','blue','white'):
        turtle.pensize(4)
        turtle.color(c)
        turtle.speed(20)
        turtle.fd(300)
        turtle.rt(201)
        turtle.delay(15)




