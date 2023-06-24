from tkinter import *
import random
import time

screen = Tk()
screen.title('Окно')
screen.resizable(False, False)
screen.wm_attributes("-topmost", 1)
canvas = Canvas(screen, width=1000, height=1000)
canvas.pack()
screen.update()


class Ball:
    def __init__(self, color, canvas, platform, score):
        self.hit_bot = False
        self.score = score
        self.platform = platform
        self.canvas = canvas
        self.ball = self.canvas.create_oval(10, 10, 60, 60, fill=color)
        self.canvas.move(self.ball, 465, 465)
        start = [-5, -6, -3, -4, 4, 5, 6, 3]
        self.x = random.choice(start)
        self.y = -4
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.ball, self.x, self.y)
        pos = self.canvas.coords(self.ball)
        if self.hit_platform(pos):
            self.y = -6

        if pos[1] <= 0:
            self.y = 6



        elif pos[3] >= self.canvas_height:
            self.hit_bot = True
            self.canvas.create_text(400, 400, fill="red", text=f'Вы проиграли', font=('arial', 50))



        elif pos[0] <= 0:
            self.x = 6

        elif pos[2] >= self.canvas_width:
            self.x = -6

    def hit_platform(self, pos):
        platform_pos = self.canvas.coords(self.platform.item)
        if pos[2] >= platform_pos[0] and pos[0] <= platform_pos[2]:
            if platform_pos[1] <= pos[3] <= platform_pos[3]:
                self.score.hit()

                return True

        return False


class Platform:
    def __init__(self, color, canvas):
        self.canvas = canvas
        self.item = self.canvas.create_rectangle(0, 0, 250, 25, fill=color)
        self.x = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.move(self.item, self.canvas_width / 2 - (250 / 2), 700)
        self.canvas.bind_all('<KeyPress-a>', self.left)
        self.canvas.bind_all('<KeyPress-d>', self.right)

    def draw(self):
        self.canvas.move(self.item, self.x, 0)
        pos = self.canvas.coords(self.item)
        if pos[0] <= 0:
            self.x = 10
        elif pos[2] >= self.canvas_width:
            self.x = -10

    def left(self, event):
        self.x = -10

    def right(self, event):
        self.x = 10


class Score:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.score = 0
        self.item = self.canvas.create_text(20, 20, fill=color, text=f'Ваш счет:{self.score}', font=('arial', 20))

    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.item, text=f"Ваш счет:{self.score}")


score = Score(canvas=canvas, color="black")
platform = Platform(color="Black", canvas=canvas)
ball = Ball(color="red", canvas=canvas, platform=platform, score=score)
while True:
    if not ball.hit_bot:
        platform.draw()
        ball.draw()
    else:
        time.sleep(3)
        break

    screen.update_idletasks()
    screen.update()
    time.sleep(0.0090)
