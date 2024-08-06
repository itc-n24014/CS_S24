import math
class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def base_area(self):
        return math.pi * self.radius**2

    def side_area(self):
        return 2 * math.pi * self.radius * self.height

    def surface_area(self):
        return 2 * self.base_area() + self.side_area()

    def volume(self):
        return self.base_area() * self.height

cylinder = Cylinder(5, 10)

print("底面積:", cylinder.base_area())
print("側面の面積:", cylinder.side_area())
print("表面積:", cylinder.surface_area())
print("体積:", cylinder.volume())
