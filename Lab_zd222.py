import turtle
import math

class Triangle:
    def __init__(self, x, y, x1, y1, x2, y2):
        self.position = (x, y)  # absolute position of the first vertex
        self.vertex1 = (x1, y1)  # position of the second vertex relative to the first
        self.vertex2 = (x2, y2)  # position of the third relative to the first vertex
        self.color = "black"  # default triangle color
        self.rotation = 0
        self.scale = (1, 1)

    def set_position(self, x, y):
        self.position = (x, y)

    def set_color(self, color):
        self.color = color

    def set_rotation(self, rotation):
        self.rotation = rotation

    def set_scale(self, scale_x, scale_y):
        self.scale = (scale_x, scale_y)

    def draw(self):
        turtle.penup()
        turtle.goto(self.position)
        turtle.pendown()
        turtle.fillcolor(self.color)
        turtle.begin_fill()

        # Застосувати обертання та масштабування
        turtle.setheading(self.rotation)
        turtle.goto(self.position[0] + self.vertex1[0] * self.scale[0], 
                    self.position[1] + self.vertex1[1] * self.scale[1])
        turtle.goto(self.position[0] + self.vertex2[0] * self.scale[0], 
                    self.position[1] + self.vertex2[1] * self.scale[1])
        turtle.goto(self.position)
        turtle.end_fill()

# Створити екран
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")

# Ініціалізувати черепашку
t = turtle.Turtle()
t.speed(0)  # Встановити найшвидшу швидкість малювання

# Намалюйте трикутники, що обертаються
for angle in range(0, 360, 10):
    triangle = Triangle(0, 0, 20 * math.cos(angle * math.pi / 180), 
                        20 * math.sin(angle * math.pi / 180),
                        -20 * math.cos(angle * math.pi / 180), 
                        20 * math.sin(angle * math.pi / 180))
    triangle.set_rotation(angle)
    triangle.set_color("blue")
    triangle.draw()

# Намалювати scaling triangles
for scale_factor in range(1, 6):
    triangle = Triangle(0, 0, 20, 0, 0, 40)
    triangle.set_scale(scale_factor, scale_factor)
    triangle.set_color("red")
    triangle.draw()

# Сховати черепашку
t.hideturtle()

# Тримайте вікно відкритим
turtle.done()