class Rectangle:
    def __init__(self, width, height=None):
        if height is not None:
            self.width, self.height = width, height
        else:
            self.width = self.height = width

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        w = '*' * self.width + '\n'
        picture = w * self.height
        return picture

    def get_amount_inside(self, shape):
        places = self.get_area()
        horizontal_amount = self.width // shape.width
        vertical_amount = self.height // shape.height

        return horizontal_amount * vertical_amount


class Square(Rectangle):
    def __int__(self, length):
        super().__init__(length)

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, new_length):
        self.width = self.height = new_length


if __name__ == '__main__':
    rect = Rectangle(10, 5)

    print(rect.get_area())
    print(rect.get_diagonal())
    print(rect.get_perimeter())
    print(rect.get_picture())

    print(rect)

    print(rect.get_amount_inside(Square(5)))
