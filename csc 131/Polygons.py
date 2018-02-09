"""
t.up() makes it so nothing's drawn
t.down() will put the pen on the paper and draw


"""


from turtle import Turtle
from turtle import Screen

#def regular_polygon(t: Turtle, length: int, num_sides: int):


def square(t: Turtle, length: int) -> None:
    """
    Draw a square with a given length
    :param t:  an instance of a Turtle used to draw a length square
    :param length: the length of the side of the int
    :return: None
    """
    for count in range(4):  #  executes 4 times
        t.forward(length)  #  Moves forward
        t.left(90)  #  turns

def hexagon(t: Turtle, length: int) -> None:
    """
    Draw a Hexagon with a given length
    :param t:  an instance of a Turtle used to draw a length square
    :param length: the length of the side of the int
    :return: None
    """
    for count in range(6):
        t.forward(length)
        t.left(60)

def triangel(t: Turtle, length: int) -> None:
    """
    Draw a square with a given length
    :param t:  an instance of a Turtle used to draw a length square
    :param length: the length of the side of the int
    :return: None
    """
    for count in range(3):
        t.forward(length)
        t.left(120)


def octogon(t: Turtle, length: int) -> None:
    """
    Draw a square with a given length
    :param t:  an instance of a Turtle used to draw a length square
    :param length: the length of the side of the int
    :return: None
    """
    for count in range(8):
        t.forward(length)
        t.left(45)


def radial_pattern(t: Turtle, n: int, length: int, shape) -> None:
    """

    :param t: turtle name
    :param n: number of shapes you wanna draw (it'll make a pattern)
    :param length: length of shape
    :param shape: what shape it'll call to draw
    :return: none
    """
    for count in range(n):
        shape(t, length)
        t.left(360/n)  #  this is where it makes the adjusts the angle so it doesn't draw over itself

def main() -> int:
    yertle = Turtle()
    screen = Screen()
    yertle.speed(100)
#    square(yertle, 300)
#    hexagon(yertle, 300)
#    triangel(yertle, 300)
#    octogon(yertle, 300)
    radial_pattern(yertle, 50, 100, square)
    screen.exitonclick()


if __name__ == '__main__':
    main()

