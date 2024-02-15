from tkinter import *
from random import randint
from random import choice

colors = ['blue', 'red', 'green', 'yellow', 'black', 'grey', 'pink', 'purple']
class Ball:
    def __init__(self):
        self.R = randint(10, 50)
        self.x = randint(self.R, 400 - self.R)
        self.y = randint(self.R, 400 - self.R)
        self.dx, self.dy = (10, 10)
        self.col = choice(colors)
        self.ball_id = canvas.create_oval(self.x - self.R, self.y - self.R, self.x + self.R, self.y + self.R, fill=self.col)
    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > 400 or self.x - self.R < 15:
            self.dx = -self.dx
        if self.y + self.R > 400 or self.y - self.R < 15:
            self.dy = -self.dy
    def show(self):
             canvas.move(self.ball_id, self.dx, self.dy)
def tick():
    for ball in balls:
        ball.move()
        ball.show()
    gui.after(50, tick)
def click(event):
    a = Ball()
    balls.append(a)
gui = Tk()
gui.geometry('400x400')
gui.resizable(False, False)
gui.columnconfigure(0, weight=1)
gui.rowconfigure(0, weight=1)
canvas = Canvas(gui)
canvas.grid(row=0, column=0, sticky = 'NSEW')
balls = []
canvas.bind('<Button-1>', click)
tick()
gui.mainloop()
