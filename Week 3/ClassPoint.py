import math
class Point:
    def __init__(self, x = int, y = int):
        self.x = x
        self.y = y

    def show (self):
        print (f"({self.x}, {self.y})")

    def symmetry_O (self):
        return Point(-self.x, -self.y)

    def distance_O (self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def distance (self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx ** 2 + dy ** 2)

A = Point (3, 4)
A.show ()

xb = int(input("Hoành độ của B: "))
yb = int(input("Tung độ của B: "))
B = Point (xb, yb)
B.show ()

C = B.symmetry_O()
C.show ()

BO = B.distance_O()
print (f"Khoảng cách từ B đến gốc tọa độ: {BO:.2f}")

AB = A.distance(B)
print (f"Khoảng cách từ A đến B: {AB:.2f}")

