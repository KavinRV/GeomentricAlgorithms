# import random


def side(p1, p2, p3):
    determinant = (p3[0] - p1[0]) * (p2[1] - p1[1]) - (p2[0] - p1[0]) * (p3[1] - p1[1])
    return determinant


class GiftWrap:
    def __init__(self, points, canvas):
        self.points = points
        self.canvas = canvas

    def left_most(self):
        """
        Finds the left most point
        :return: index of left most point
        """
        mini = 0
        for i in range(1, len(self.points)):
            if self.points[i][0] < self.points[mini][0]:
                mini = i
            elif self.points[i][0] == self.points[mini][0]:
                if self.points[i][1] > self.points[mini][1]:
                    mini = i
        return mini

    @property
    def convex_hull(self):
        """
        Compute convex hull using jarvis march method
        :return: List containing
        """
        length = len(self.points)
        if length < 3:
            return

        hull_points = []
        switch = True
        cur = self.left_most()
        p1 = cur

        while switch:
            hull_points.append((self.points[p1][0], self.points[p1][1]))
            p2 = (p1 + 1) % length

            for j in range(length):
                self.canvas.create_line(self.points[p1][0], self.points[p1][1], self.points[j][0],
                                        self.points[j][1],
                                        fill='#F54748', tags=('red_line', 'line', 'gift'), dash=(2, 4))
                # time.sleep(0.02)
                self.canvas.update()
                self.canvas.delete('red_line')
                if side(self.points[p1], self.points[j], self.points[p2]) < 0:
                    p2 = j
                    self.canvas.delete('black_line')
                    self.canvas.create_line(self.points[p2][0], self.points[p2][1], self.points[p1][0],
                                            self.points[p1][1],
                                            fill='#EDEDED', tags=('black_line', 'line', 'gift'), dash=(6, 4))
                    self.canvas.update()

            self.canvas.create_line(self.points[p2][0], self.points[p2][1], self.points[p1][0],
                                    self.points[p1][1],
                                    fill='#66DE93', tags=('green_line', 'line', 'gift'))
            p1 = p2

            if p1 == cur:
                self.canvas.delete('black_line')
                break

        return hull_points
