import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"

class LineSegment:
    def __init__(self, *args):
        if len(args) == 0:
            self.__d1, self.__d2 = Point(8, 5), Point(1, 0)
        elif len(args) == 2 and isinstance(args[0], Point):
            self.__d1, self.__d2 = args[0], args[1]
        elif len(args) == 4:
            self.__d1, self.__d2 = Point(args[0], args[1]), Point(args[2], args[3])
        elif len(args) == 1 and isinstance(args[0], LineSegment):
            old = args[0]
          
            self.__d1 = Point(old.getD1().x, old.getD1().y)
            self.__d2 = Point(old.getD2().x, old.getD2().y)

    def getD1(self): return self.__d1
    def getD2(self): return self.__d2

    def length(self):
        return math.sqrt((self.__d1.x - self.__d2.x)**2 + (self.__d1.y - self.__d2.y)**2)

    def hien_thi(self):
        print(f"Đoạn thẳng: {self.__d1} đến {self.__d2} | Dài: {self.length():.2f}")


p_goc = Point(0, 0)
seg_ref = LineSegment(p_goc, Point(3, 4))
seg_copy = LineSegment(seg_ref)

print("Trước khi đổi gốc:")
seg_ref.hien_thi()
seg_copy.hien_thi()

p_goc.x = 100 
print("\nSau khi đổi p_goc.x = 100:")
print("Seg_ref bị đổi theo vì dùng chung điểm:")
seg_ref.hien_thi() 
print("Seg_copy giữ nguyên vì là bản sao độc lập:")
seg_copy.hien_thi()