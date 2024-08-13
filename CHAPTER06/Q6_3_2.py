class Shape:
    def __init__(self, name):
        self.name = name

    def show_attributes(self):
        print(f"name: {self.name}")

class Rectangle(Shape):
    angle = 90

    def __init__(self, width, height):
        super().__init__('rectangle')
        self.width = width
        self.height = height
        self.perimeter = self.calc_perimeter()
        self.area = self.calc_area()

    def calc_perimeter(self):
        w = self.width
        h = self.height
        return (w + h) * 2

    def calc_area(self):
        w = self.width
        h = self.height
        return w * h

    def show_attributes(self):
        super().show_attributes()
        ang = self.angle
        w = self.width
        h = self.height
        p = self.perimeter
        a = self.area
        print(f"width: {w}, height: {h}, angle: {ang}")
        print(f"perimeter: {p}, area: {a}")

r1 = Rectangle(4, 3)
r1.show_attributes()

