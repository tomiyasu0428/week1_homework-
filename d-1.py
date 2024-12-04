import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


# 半径1の円
circle1 = Circle(radius=1)
print(round(circle1.area(), 2))  # 3.14
print(round(circle1.perimeter(), 2))  # 6.28

# 半径3の円
circle3 = Circle(radius=3)
print(round(circle3.area(), 2))  # 28.27
print(round(circle3.perimeter(), 2))  # 18.85
