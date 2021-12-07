import random
import tkinter as tk

from giftwrap import GiftWrap
from graham import Graham
from increment import Increment

# ---------------------------- CONSTANTS ------------------------------- #
L_PINK = "#6B4F4F"
PINK = "#483434"
DICE = "#EDEDED"
LINE = "#1C7947"
FONT_NAME = "Helvetica"

points = []


# ---------------------------- ALGORITHMS ------------------------------- #


def get_point(event):
    px, py = event.x, event.y
    canvas.create_oval(px - 2.5, py - 2.5, px + 2.5, py + 2.5, fill=DICE, outline=DICE)
    points.append((event.x, event.y))


def rand_gen():
    reset()
    n = random.randint(150, 240)
    for i in range(n):
        px = random.randint(5, 1495)
        py = random.randint(5, 840)
        points.append((px, py))
        canvas.create_oval(px - 2, py - 2, px + 2, py + 2, fill=DICE, outline=DICE)


# Compute GiftWrap
def app_gw():
    canvas.delete('line')
    jarvis = GiftWrap(points, canvas)
    hull = jarvis.convex_hull
    for i in range(len(hull)):
        # global lines
        canvas.create_oval(hull[i][0] - 4, hull[i][1] - 4, hull[i][0] + 4, hull[i][1] + 4, fill='#87A7B3',
                           tags='line', outline='#87A7B3')


# Compute Incremental Approach
def app_inc():
    canvas.delete('line')
    convex = Increment(points, canvas)
    hull = convex.convex_hull
    for i in range(len(hull)):
        # global lines
        canvas.create_oval(hull[i][0] - 4, hull[i][1] - 4, hull[i][0] + 4, hull[i][1] + 4, fill='#87A7B3',
                           tags='line', outline='#87A7B3')


# Compute Graham Scan
def gra_sca():
    canvas.delete('line')
    convex = Graham(points, canvas)
    hull = convex.convex_hull
    for i in range(len(hull)):
        # global lines
        canvas.create_oval(hull[i][0] - 4, hull[i][1] - 4, hull[i][0] + 4, hull[i][1] + 4, fill='#87A7B3',
                           tags='line', outline='#87A7B3')


def reset():
    global points
    points = []
    canvas.delete('all')


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = tk.Tk()
window.geometry('1600x1300')
window.title("Convex Hull")
window.config(padx=50, pady=50, bg=PINK)

# Canvas
canvas = tk.Canvas(width=1500, height=850, bg=L_PINK, highlightthickness=0)
canvas.bind('<Button-1>', get_point)
canvas.place(x=50, y=50)
canvas.pack()

# Jarvis Button
jarvis_button = tk.Button(text="Jarvis", highlightbackground=L_PINK, fg=DICE, highlightthickness=0,
                          font=FONT_NAME, width=4, height=2)
jarvis_button.config(command=app_gw)
jarvis_button.place(x=370 + 150, y=855)

# Incremental Button
incre_button = tk.Button(text="Incremental", highlightbackground=L_PINK, fg=DICE, highlightthickness=0,
                         font=FONT_NAME, width=7, height=2)
incre_button.config(command=app_inc)
incre_button.place(x=440 + 150, y=855)

# Graham Scan Button
graham_button = tk.Button(text="Graham Scan", highlightbackground=L_PINK, fg=DICE, highlightthickness=0,
                          font=FONT_NAME, width=8, height=2)
graham_button.config(command=gra_sca)
graham_button.place(x=535 + 150, y=855)

# Reset Button
reset_button = tk.Button(text="Reset", highlightbackground=L_PINK, fg=DICE, highlightthickness=0,
                         font=FONT_NAME, width=4, height=2)
reset_button.config(command=reset)
reset_button.place(x=635 + 150, y=855)

# Random Button
random_button = tk.Button(text="Random", highlightbackground=L_PINK, fg=DICE, highlightthickness=0,
                          font=FONT_NAME, width=7, height=2)
random_button.config(command=rand_gen)
random_button.place(x=705 + 150, y=855)

window.mainloop()
