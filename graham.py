from math import atan2
import time
low = (None, None)


def polar(a):
    b = low
    y_span = a[1] - b[1]
    x_span = a[0] - b[0]
    return atan2(y_span, x_span)


class Graham:
    def __init__(self, points, canvas):
        self.all_points = points
        self.bot_most()
        self.points = sorted(points, key=polar, reverse=True) # sorted by polar angles from bottom most point
        self.canvas = canvas

    def bot_most(self):
        global low
        mini = 0
        for i in range(1, len(self.all_points)):
            if self.all_points[i][1] > self.all_points[mini][1]:
                mini = i
            elif self.all_points[i][1] == self.all_points[mini][1]:
                if self.all_points[i][0] > self.all_points[mini][0]:
                    mini = i
        low = self.all_points[mini]

    @staticmethod
    def side(p1, p2, p3):
        determinant = (p3[0] - p1[0]) * (p2[1] - p1[1]) - (p2[0] - p1[0]) * (p3[1] - p1[1])
        return determinant

    @property
    def convex_hull(self):
        hull = [self.points[0]]
        for p in self.points[1:]:
            self.canvas.create_line(hull[-1][0], hull[-1][1],
                                    p[0],
                                    p[1],
                                    fill='blue', tags=(f'blue_line{hull[-1]}{p}', 'line'))
            self.canvas.update()
            time.sleep(0.2)
            while len(hull) > 1 and self.side(hull[-2], hull[-1], p) <= 0:

                self.canvas.delete(f'blue_line{hull[-1]}{p}')
                self.canvas.delete(f'blue_line{hull[-2]}{hull[-1]}')
                del hull[-1]
                self.canvas.create_line(hull[-1][0], hull[-1][1],
                                        p[0],
                                        p[1],
                                        fill='blue', tags=(f'blue_line{hull[-1]}{p}', 'line'))
                self.canvas.update()
                time.sleep(0.2)
                if len(hull) < 2:break
            hull.append(p)
            self.canvas.itemconfig(f'blue_line{hull[-2]}{hull[-1]}', fill='green')

        self.canvas.create_line(hull[-1][0], hull[-1][1],
                                hull[0][0],
                                hull[0][1],
                                fill='green', tags='line')
        return hull


