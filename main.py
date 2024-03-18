from turtle import Screen
from symbol import Symbol

num = []
count = 0
a = 3

# Obtain a user-defined number between 1 and 9,999.  If input is out of range, user is required to re-enter a
# value that is within range.
user_number = int(input("Choose a number between 1 and 9999 to convert: "))

while user_number > 9999 or user_number < 1:
    user_number = int(input("The number you have chosen is out of range.  Please choose a number between 1 "
                            "and 9999 to convert: "))

# Converts user input into a four character string.
user_number_string = str(format(user_number, "04"))

# converts each character from the string into an integer and stores it on the list "num".
for d in user_number_string:
    num.append(int(d))

# Creates a screen object with a title and disables the tracing movements of the turtle object.
screen = Screen()

screen.title("Cistercian Number Convertor")
screen.tracer(0)

# Each item in list "num" is sent to class Symbol to convert into the Cistercian number symbol or glyph equivalent.
for _ in num:
    symbol = Symbol(num[a], count)
    count += 1
    a -= 1

# Updates the screen with the glyph or symbols based on the user's defined input.
screen.update()

# Converts symbol/glyph into an .eps file
screen.getcanvas().postscript(file="cis.eps")

# Exits out of screen object.
screen.exitonclick()
