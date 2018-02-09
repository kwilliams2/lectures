from turtle import Turtle

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


def main() -> int:
    yertle = Turtle()
    square(yertle, 300)
    hexagon(yertle, 300)
    triangel(yertle, 300)
    octogon(yertle, 300)


if __name__ == '__main__':
    main()

