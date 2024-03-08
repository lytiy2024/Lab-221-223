import turtle
from random import randint

class Triangle:
    def __init__(self, x, y, x1, y1, x2, y2):
        self.position = (x, y)  # absolute position of the first vertex
        self.vertex1 = (x1, y1)  # position of the second vertex relative to the first
        self.vertex2 = (x2, y2)  # position of the third relative to the first vertex
        self.color = "black"  # default triangle color

    def set_position(self, x, y):
        self.position = (x, y)

    def set_color(self, color):
        self.color = color

    def draw(self):
        turtle.penup()
        turtle.goto(self.position)
        turtle.pendown()
        turtle.fillcolor(self.color)
        turtle.begin_fill()
        turtle.goto(self.position[0] + self.vertex1[0], self.position[1] + self.vertex1[1])
        turtle.goto(self.position[0] + self.vertex2[0], self.position[1] + self.vertex2[1])
        turtle.goto(self.position)
        turtle.end_fill()

# Створити екран
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")

# Ініціалізувати черепашку
t = turtle.Turtle()
t.speed(0)  # Встановіть найшвидшу швидкість малювання

# Намалювати 100 triangles
for _ in range(100):
    x = randint(-300, 300)
    y = randint(-200, 200)
    vertex1 = (randint(-50, 50), randint(-50, 50))
    vertex2 = (randint(-50, 50), randint(-50, 50))
    color = ["red", "blue", "green", "yellow", "orange", "purple"][randint(0, 5)]
    
    triangle = Triangle(x, y, *vertex1, *vertex2)
    triangle.set_color(color)
    triangle.draw()

# Сховати черепашку
t.hideturtle()

# Тримати вікно відкритим
turtle.done()