class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def set_height(self, height):
        self.height = height
    def set_width(self, width):
        self.width = width
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

def resize_rectangle(rectangle, new_width, new_height):
    rectangle.set_width(new_width)
    rectangle.set_height(new_height)
    return rectangle.width * rectangle.height

rect = Rectangle(4, 5)
print(resize_rectangle(rect, 2, 3))  # Output: 6
Square = Square(4)
print(resize_rectangle(Square, 2, 3))  # Output: 9