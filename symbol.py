from turtle import Turtle

FORTY_FIVE = 45
NINETY = 90
ONE_THIRTY_FIVE = 135


class Symbol(Turtle):

    # Initialize Cistercian numberical objects based on user defined input value and placement of value.
    def __init__(self, num, count):
        super().__init__()
        self.num = num
        self.count = count
        self.setposition(0, 0)
        self.pensize(5)
        self.hideturtle()
        self.setheading(NINETY)

        # Determines how glyph or symbol is drawn based on its placement of ones, tens, hundreds, or thousands.
        if self.count == 0:
            self.ones(self.num)
        elif self.count == 1:
            self.tens(self.num)
        elif self.count == 2:
            self.hundreds(self.num)
        elif self.count == 3:
            self.thousands(self.num)

    # Initializes drawing based on an ones placement.
    def ones(self, num):
        self.forward(50)
        self.draw(num, 1)

    # Initializes drawing based on the tens placement.
    def tens(self, num):
        self.forward(50)
        self.draw(num, -1)

    # Initializes drawing based on the hundreds placement.
    def hundreds(self, num):
        self.penup()
        self.forward(50)
        self.setheading(270)
        self.pendown()
        self.forward(50)
        self.draw(num, -1)

    # Initializes drawing based on the thousands placement.
    def thousands(self, num):
        self.penup()
        self.forward(50)
        self.setheading(270)
        self.pendown()
        self.forward(50)
        self.draw(num, 1)

    # Draws glyph or symbol based on its value.
    def draw(self, num, direction):
        if num == 0:
            pass
        elif num == 1:
            self.one(direction)
        elif num == 2:
            self.two(direction)
        elif num == 3:
            self.three(direction)
        elif num == 4:
            self.four(direction)
        elif num == 5:
            self.five(direction)
        elif num == 6:
            self.six(direction)
        elif num == 7:
            self.seven(direction)
        elif num == 8:
            self.eight(direction)
        elif num == 9:
            self.nine(direction)

    def one(self, direction):
        self.right(NINETY * direction)
        self.forward(15)

    def two(self, direction):
        self.backward(15)
        self.right(NINETY * direction)
        self.forward(15)

    def three(self, direction):
        self.right(ONE_THIRTY_FIVE * direction)
        self.forward(21.2)

    def four(self, direction):
        self.back(15)
        self.right(FORTY_FIVE * direction)
        self.forward(21.2)

    def five(self, direction):
        self.right(NINETY * direction)
        self.forward(15)
        self.right(ONE_THIRTY_FIVE * direction)
        self.forward(21.2)

    def six(self, direction):
        self.right(NINETY * direction)
        self.penup()
        self.forward(15)
        self.right(NINETY * direction)
        self.pendown()
        self.forward(15)

    def seven(self, direction):
        self.right(NINETY * direction)
        self.forward(15)
        self.right(NINETY * direction)
        self.forward(15)

    def eight(self, direction):
        self.backward(15)
        self.right(NINETY * direction)
        self.forward(15)
        self.left(NINETY * direction)
        self.forward(15)

    def nine(self, direction):
        self.right(NINETY * direction)
        self.forward(15)
        self.right(NINETY * direction)
        self.forward(15)
        self.right(NINETY * direction)
        self.forward(15)
