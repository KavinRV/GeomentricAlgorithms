import tkinter
from tkinter import Tk

# Adding a Tk window
root: Tk = tkinter.Tk()
root.geometry('640x480')   # Configuring the resolution

# Adding the canvas to put the graph on it
CanvasNo1 = tkinter.Canvas(root, width=640, height=480)
CanvasNo1.grid()


def draw_axis(canvas_object):   # a function in order to draw the horizontal and vertical lines and setting the scroll
    canvas_object.update()
    x_origin = canvas_object.winfo_width() // 2
    y_origin = canvas_object.winfo_height() // 2
    canvas_object.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas_object.create_line(x_origin, 0, -x_origin, 0)
    canvas_object.create_line(0, y_origin, 0, -y_origin)


def parabola(number, size):  # Calculating the parabola
    result = number * number // size
    return result


def plot(canvas_object, size, color):  # The grand function to do the plotting process
    y_location = [parabola(each, size) for each in range(-size, size + 1)]
    x_location = list(range(-size, size + 1))
    for each_of in range(0, size*2+2):
        if each_of <= size*2-1:
            canvas_object.create_line(x_location[each_of], -y_location[each_of], x_location[each_of+1],
                                      -y_location[each_of+1], fill=str(color))
            # print('A line from X location of {} and Y location of {} to the X location of {} and Y location of {} was'
            #       ' drawn, Color = {}'.format(x_location[each_of], y_location[each_of], x_location[each_of+1],
            #                                   y_location[each_of+1], color))
        else:
            break


draw_axis(CanvasNo1)
plot(CanvasNo1, 500, 'red')
CanvasNo1.mainloop()   # running the window