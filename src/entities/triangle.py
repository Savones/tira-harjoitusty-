from vertex import Vertex


class Triangle:
    def __init__(self, vertex1, vertex2, vertex3):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.vertex3 = vertex3
        self.triagle = [vertex1, vertex2, vertex3]
        self.circum_center = self.get_circum_center()

    def get_circum_center(self):
        a = self.vertex2.y - self.vertex1.y
        b = self.vertex1.x - self.vertex2.x
        c = a * (self.vertex1.x) + b * (self.vertex1.y)

        middle = [(self.vertex1.x + self.vertex2.x)//2,
                  (self.vertex1.y + self.vertex2.y)//2]
        c = -b * (middle[0]) + a * (middle[1])
        a, b = -b, a

        e = self.vertex3.y - self.vertex2.y
        f = self.vertex2.x - self.vertex3.x
        g = e * (self.vertex2.x) + f * (self.vertex2.y)

        middle = [(self.vertex2.x + self.vertex3.x)//2,
                  (self.vertex2.y + self.vertex3.y)//2]
        g = -f * (middle[0]) + e * (middle[1])
        e, f = -f, e

        x = (f * c - b * g)//(a * f - e * b)
        y = (a * g - e * c)//(a * f - e * b)

        return [x, y]
