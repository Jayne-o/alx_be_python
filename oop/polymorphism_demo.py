import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement the area method.")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

 from polymorphism_demo import Rectangle, Circle

def main():
    rect = Rectangle(10, 5)
    circ = Circle(7)

    print(f"The area of the Rectangle is: {rect.area()}")
    print(f"The area of the Circle is: {circ.area()}")

if __name__ == "__main__":
    main()
