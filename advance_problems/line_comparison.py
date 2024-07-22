# Line Comparison Computation
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    @property
    def length(self):
        return math.sqrt((self.point2.x - self.point1.x)**2 + (self.point2.y - self.point1.y)**2)
    
    def __eq__(self, other):
        return self.length == other.length
    
    def __gt__(self, other):
        return self.length > other.length
    
    def __lt__(self, other):
        return self.length < other.length

if __name__ == '__main__':
    print('Welcome to Line Comparison Computation')

    point1 = Point(2, 5)
    point2 = Point(4, 6)

    point3 = Point(3, 7)
    point4 = Point(4, 8)
    line1 = Line(point1, point2)
    line2 = Line(point3, point4)

    if(line1 == line2):
        print("Both lines are of equal length")
    elif(line1 > line2):
        print("Line 1 is greater than line 2")
    elif(line1 < line2):
        print("Line 2 is greater than line 1")

    print(f"Length of the line-1: {line1.length:.2f}")
    print(f"Length of the line-2: {line2.length:.2f}")
    