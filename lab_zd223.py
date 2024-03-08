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
        self.pivot = (0, 0)  # default pivot at origin

    def set_position(self, x, y):
        self.position = (x, y)

    def set_color(self, color):
        self.color = color

    def set_rotation(self, rotation):
        self.rotation = rotation

    def set_scale(self, scale_x, scale_y):
        self.scale = (scale_x, scale_y)

    def set_pivot(self, pivot_x, pivot_y):
        self.pivot = (pivot_x, pivot_y)

    def rotate_relative_to_pivot(self, angle):
        # Трансформувати трикутник, щоб повертати, обертати та повертати назад
        dx = self.position[0] - self.pivot[0]
        dy = self.position[1] - self.pivot[1]
        new_x = dx * math.cos(angle) - dy * math.sin(angle) + self.pivot[0]
        new_y = dx * math.sin(angle) + dy * math.cos(angle) + self.pivot[1]
        self.position = (new_x, new_y)
        self.rotation += angle

    def stretch_relative_to_pivot(self, scale_x, scale_y):
        # Трансформувати трикутник у поворот, розтягування та назад
        dx = self.position[0] - self.pivot[0]
        dy = self.position[1] - self.pivot[1]
        new_x = dx * scale_x + self.pivot[0]
        new_y = dy * scale_y + self.pivot[1]
        self.position = (new_x, new_y)
        self.scale = (self.scale[0] * scale_x, self.scale[1] * scale_y)

    def draw(self):
        turtle.penup()
        turtle.goto(self.position)
        turtle.pendown()
        turtle.fillcolor(self.color)
        turtle.begin_fill()

        # Застосувати обертання та масштабування
        turtle.setheading(self.rotation * 180 / math.pi)
        turtle.goto(self.position[0] + self.vertex1[0] * self.scale[0], 
                    self.position[1] + self.vertex1[1] * self.scale[1])
        turtle.goto(self.position[0] + self.vertex2[0] * self.scale[0], 
                    self.position[1] + self.vertex2[1] * self.scale[1])
        turtle.goto(self.position)
        turtle.end_fill()

# Функція пошуку точки перетину двох прямих
def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return None  # Лінії не перетинаються, упс

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

# Функція обчислення точки перетину медіан трикутника
def median_intersection(triangle):
    mid_ab = ((triangle.position[0] + triangle.vertex1[0]) / 2, (triangle.position[1] + triangle.vertex1[1]) / 2)
    mid_bc = ((triangle.position[0] + triangle.vertex2[0]) / 2, (triangle.position[1] + triangle.vertex2[1]) / 2)
    mid_ca = ((triangle.vertex1[0] + triangle.vertex2[0]) / 2, (triangle.vertex1[1] + triangle.vertex2[1]) / 2)
    return line_intersection((triangle.position, mid_ab), (triangle.vertex1, mid_ca))

# Функція для обчислення точки перетину бісектрис кута трикутника
def bisector_intersection(triangle):
    len_ab = math.sqrt((triangle.vertex1[0] - triangle.position[0]) ** 2 + (triangle.vertex1[1] - triangle.position[1]) ** 2)
    len_bc = math.sqrt((triangle.vertex2[0] - triangle.position[0]) ** 2 + (triangle.vertex2[1] - triangle.position[1]) ** 2)
    len_ca = math.sqrt((triangle.vertex2[0] - triangle.vertex1[0]) ** 2 + (triangle.vertex2[1] - triangle.vertex1[1]) ** 2)
    point_ab = ((len_bc * triangle.position[0] + len_ca * triangle.vertex1[0]) / (len_bc + len_ca),
                (len_bc * triangle.position[1] + len_ca * triangle.vertex1[1]) / (len_bc + len_ca))
    point_bc = ((len_ca * triangle.position[0] + len_ab * triangle.vertex2[0]) / (len_ca + len_ab),
                (len_ca * triangle.position[1] + len_ab * triangle.vertex2[1]) / (len_ca + len_ab))
    point_ca = ((len_ab * triangle.vertex1[0] + len_bc * triangle.vertex2[0]) / (len_ab + len_bc),
                (len_ab * triangle.vertex1[1] + len_bc * triangle.vertex2[1]) / (len_ab + len_bc))
    return line_intersection((point_ab, triangle.position), (point_bc, triangle.vertex2))

# Створити екрана
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")

# Запустити черепашку
t = turtle.Turtle()
t.speed(0)  # Встановити найшвидшу швидкість малювання

# Точки трикутника
x, y = 0, 10
x1, y1 = 80, 0
x2, y2 = 0, 100

# Створити triangle
triangle = Triangle(x, y, x1, y1, x2, y2)

# Встановити опору для обертання та розтягування
pivot_rotation = bisector_intersection(triangle)
pivot_stretch = median_intersection(triangle)

# Намалювати обертовий трикутник навколо точки перетину бісектрис
for angle in range(0, 260, 30):
    triangle.set_pivot(*pivot_rotation)
    triangle.rotate_relative_to_pivot(math.radians(10))
    triangle.draw()

# Намалювати витягнутий трикутник відносно точки перетину медіан
for scale_factor in range(1, 10):
    triangle.set_pivot(*pivot_stretch)
    triangle.stretch_relative_to_pivot(1.1, 1.1)
    triangle.draw()

# Сховай черепашку
t.hideturtle()

# Тримайте вікно відкритим
turtle.done()

