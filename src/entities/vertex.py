class Vertex:
    """Luokka pisteelle

    Attributes:
        x (int): Pisteen x koordinaatti
        y (int): Pisteen y koordinaatti
    """

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"{self.x}, {self.y}"
