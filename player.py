import datetime


class Humain:
    def __init__(self):
        self._x = 0

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    x = property(get_x, set_x)

H1 = Humain()

H1.x = 20

print(H1.x)












