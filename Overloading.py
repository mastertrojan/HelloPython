class Vector:
    def __init__(self, x_comp, y_comp):
        self.x_comp = x_comp
        self.y_comp = y_comp

    def __abs__(self):
        return(x * x + y * y) ** 0.5
