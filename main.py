import tkinter as tk
from giftwrap import GiftWrap
from increment import Increment
import random
from queue import PriorityQueue as pq

# ---------------------------- CONSTANTS ------------------------------- #
L_PINK = "#EAE7C6"
PINK = "#BCCC9A"
DICE = "#C37B89"
LINE = "#1C7947"
FONT_NAME = "Helvetica"

points = []

# ---------------------------- ALGORITHMS ------------------------------- #


def get_point(event):
    px, py = event.x, event.y
    canvas.create_rectangle(px - 2, py - 2, px + 2, py + 2, fill=DICE, outline=DICE)
    points.append((event.x, event.y))


def rand_gen():
    reset()
    n = random.randint(150, 240)
    for i in range(n):
        px = random.randint(5, 1495)
        py = random.randint(5, 900)
        points.append((px, py))
        canvas.create_rectangle(px - 2, py - 2, px + 2, py + 2, fill=DICE, outline=DICE)


def app_gw():
    canvas.delete('line')
    jarvis = GiftWrap(points, canvas)
    hull = jarvis.convex_hull
    for i in range(len(hull)):
        # global lines
        canvas.create_oval(hull[i][0] - 3, hull[i][1] - 3, hull[i][0] + 3, hull[i][1] + 3, fill='#F0A500',
                           tags='line', outline='#F0A500')


def app_inc():
    canvas.delete('line')
    convex = Increment(points, canvas)
    hull = convex.convex_hull
    for i in range(len(hull)):
        # global lines
        canvas.create_oval(hull[i][0] - 3, hull[i][1] - 3, hull[i][0] + 3, hull[i][1] + 3, fill='#F0A500',
                           tags='line', outline='#F0A500')


def reset():
    global points
    points = []
    canvas.delete('all')


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.geometry('1600x1300')
window.title("Convex Hull")
window.config(padx=50, pady=50, bg=PINK)

canvas = tk.Canvas(width=1500, height=950, bg=L_PINK, highlightthickness=0)
canvas.bind('<Button-1>', get_point)
canvas.place(x=50, y=50)
canvas.pack()

jarvis_button = tk.Button(text="Jarvis", highlightbackground=L_PINK, fg=DICE, highlightthickness=0,
                          font=FONT_NAME, width=4, height=2)
jarvis_button.config(command=app_gw)
jarvis_button.place(x=170, y=505)

incre_button = tk.Button(text="Incremental", highlightbackground=L_PINK, fg=DICE, highlightthickness=0,
                         font=FONT_NAME, width=7, height=2)
incre_button.config(command=app_inc)
incre_button.place(x=240, y=505)

reset_button = tk.Button(text="Reset", highlightbackground=L_PINK, fg=DICE, highlightthickness=0,
                         font=FONT_NAME, width=4, height=2)
reset_button.config(command=reset)
reset_button.place(x=335, y=505)

reset_button = tk.Button(text="Random", highlightbackground=L_PINK, fg=DICE, highlightthickness=0,
                         font=FONT_NAME, width=7, height=2)
reset_button.config(command=rand_gen)
reset_button.place(x=240, y=550)


window.mainloop()
