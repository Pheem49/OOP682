class Shape:
    def resize(self, *args, **kwargs):
        pass

    def area(self):
        return self.width * self.height
    
    def set_height(self, height):
        self.height = height
    def set_width(self, width):
        self.width = width
class rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)

    def resize(self, new_width, new_height):
        self.set_width(new_width)
        self.set_height(new_height)
    
    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        super().__init__(side, side)
    
    def resize(self, *args, **kwargs):
        return super().resize(*args, **kwargs)
    
    def area(self):
        return super().area()

    
def resize_rectangle(rectangle, new_width, new_height):
    rectangle.resize(new_width, new_height)
    return rectangle.area()

rect = rectangle(4, 5)
print(resize_rectangle(rect, 2, 3))  # Output: 6
square = Square(4)
print(resize_rectangle(square, 2, 3))  # Output: 9
