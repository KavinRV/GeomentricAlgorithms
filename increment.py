class Increment:
    def __init__(self, points, canvas):
        self.points = points
        self.canvas = canvas

    @staticmethod
    def side(p1, p2, p3):
        """
        Whether counter clock wise or clockwise turn
        :param p1: Point 1
        :param p2: Point 2
        :param p3: Point 3
        :return: ccw > 0 , cw < 0
        """
        determinant = (p3[0] - p1[0]) * (p2[1] - p1[1]) - (p2[0] - p1[0]) * (p3[1] - p1[1])
        return determinant

    @property
    def convex_hull(self):
        """
        Computes Convex Hull using incremental approach
        :return: List containing all vertices of the convex hull
        """
        self.points.sort()
        length = len(self.points)
        if length < 3:
            return

        upper_hull = []

        for i in range(0, length):
            while len(upper_hull) >= 2 and self.side(self.points[upper_hull[-2]], self.points[upper_hull[-1]],
                                                     self.points[i]) >= 0:
                len(upper_hull)
                temp = upper_hull.pop()
                self.canvas.delete(f'green_line{temp}')
                # time.sleep(0.2)
                # self.canvas.update()

            if len(upper_hull) > 0:
                self.canvas.create_line(self.points[upper_hull[-1]][0], self.points[upper_hull[-1]][1],
                                        self.points[i][0],
                                        self.points[i][1],
                                        fill='#66DE93', tags=(f'green_line{i}', 'line'))

                # self.canvas.delete('black_line')

            upper_hull.append(i)
            self.canvas.create_line(self.points[upper_hull[-1]][0], self.points[upper_hull[-1]][1],
                                    self.points[(i + 1) % length][0],
                                    self.points[(i + 1) % length][1],
                                    fill='#334756', tags=(f'black_line', 'line'), dash=(6, 4))
            self.canvas.update()
            # time.sleep(0.05)
            self.canvas.delete('black_line')

        lower_hull = []

        for i in range(length - 1, -1, -1):
            while len(lower_hull) >= 2 and self.side(self.points[lower_hull[-2]], self.points[lower_hull[-1]],
                                                     self.points[i]) >= 0:
                len(lower_hull)
                temp = lower_hull.pop()
                self.canvas.delete(f'red_line{temp}')
                # time.sleep(0.)
                # self.canvas.update()

            if len(lower_hull) > 0:
                self.canvas.create_line(self.points[lower_hull[-1]][0], self.points[lower_hull[-1]][1],
                                        self.points[i][0],
                                        self.points[i][1],
                                        fill='#F54738', tags=(f'red_line{i}', 'line'))
                # self.canvas.update()
                # time.sleep(0.2)
            lower_hull.append(i)
            self.canvas.create_line(self.points[lower_hull[-1]][0], self.points[lower_hull[-1]][1],
                                    self.points[(i + 1) % length][0],
                                    self.points[(i + 1) % length][1],
                                    fill='#334756', tags=(f'black_line', 'line'), dash=(6, 4))
            self.canvas.update()
            # time.sleep(0.05)
            self.canvas.delete('black_line')

        upper_hull.pop()
        lower_hull.pop()
        upper_hull.extend(lower_hull)
        return [self.points[i] for i in upper_hull]
