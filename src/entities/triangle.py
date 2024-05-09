import math


class Triangle:
    """Kolmiota kuvaava luokka

    Attributes:
        vertex1: Vertex luokan olio
        vertex2: Vertex luokan olio
        vertex3: Vertex luokan olio
    """

    def __init__(self, vertex1, vertex2, vertex3) -> None:
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.vertex3 = vertex3
        self.triangle = [vertex1, vertex2, vertex3]
        self.circum_center = self.get_circum_center()
        self.edges = [(vertex1, vertex2), (
            vertex2, vertex3), (vertex1, vertex3)]
        self.radius = math.sqrt(
            (self.vertex1.x - self.circum_center[0])**2 + (self.vertex1.y - self.circum_center[1])**2)

    def __str__(self) -> str:
        return f"{[str(t) for t in self.triangle]}"

    def get_circum_center(self) -> list:
        """Selvittää kolmion ulkoympyrän keskipisteen koordinaatit

        Returns:
            list: keskipisteen koordinaatteja kuvaava [x, y] lista
            """

        y_difference_1, x_difference_1, dot_product_1 = self.do_vertex_calculations(
            self.vertex1, self.vertex2)

        y_difference_2, x_difference_2, dot_product_2 = self.do_vertex_calculations(
            self.vertex2, self.vertex3)

        x = (x_difference_2 * dot_product_1 - x_difference_1 *
             dot_product_2) // (y_difference_1 * x_difference_2 - y_difference_2 * x_difference_1)
        y = (y_difference_1 * dot_product_2 - y_difference_2 *
             dot_product_1) // (y_difference_1 * x_difference_2 - y_difference_2 * x_difference_1)

        return [x, y]

    def do_vertex_calculations(self, vertex1, vertex2) -> tuple:
        """Laskee kahdelle (x, y) pisteelle eri arvoja

        Args:
            vertex1 (Vertex): Toinen Vertex luokan olio
            vertex2 (Vertex): Toinen Vertex luokan olio

        Returns:
            tuple: tuplena y- ja x-koordinaattien erotus sekä pistetulo
        """
        y_difference = vertex2.y - vertex1.y
        x_difference = vertex1.x - vertex2.x

        dot_product = y_difference * vertex1.x + x_difference * vertex1.y

        middle_x = (vertex1.x + vertex2.x) // 2
        middle_y = (vertex1.y + vertex2.y) // 2

        dot_product = -x_difference * middle_x + y_difference * middle_y
        y_difference, x_difference = -x_difference, y_difference

        return y_difference, x_difference, dot_product

    def point_in_circumcircle(self, point: tuple) -> bool:
        """Tarkistaa, onko (x, y) piste tämän Triangle olion ulkoympyrän sisällä

        Args:
            point (tuple): pisteen (x, y) koordinaatti

        Returns:
            bool: Palauttaa True, jos piste ulkoympyrän sisällä, muuten False
        """

        point_distance = math.sqrt(
            (point[0] - self.circum_center[0])**2 + (point[1] - self.circum_center[1])**2)
        radius = math.sqrt(
            (self.vertex1.x - self.circum_center[0])**2 + (self.vertex1.y - self.circum_center[1])**2)

        return point_distance <= radius
