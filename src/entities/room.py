class Room:
    """Huonetta kuvaava luokka

    Attributes:
            x (int): Huoneen vasemmanpuolimmaisin x-koordinaatti
            y (int): Huoneen ylin y-koordinaatti
            width (int): Huoneen leveys
            height (int): Huoneen korkeus
    """

    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f"{self.x}, {self.y}, {self.width}, {self.height}"
