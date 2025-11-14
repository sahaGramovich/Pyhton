import turtle

# Настройка экрана
screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor("white")
screen.title("Крош из Смешариков")

# Создание черепашки
t = turtle.Turtle()
t.speed(5)
t.pensize(3)


# Функция для рисования круга
def draw_circle(x, y, radius, color, fill=True):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    if fill:
        t.begin_fill()
    t.color(color)
    t.circle(radius)
    if fill:
        t.end_fill()


# Функция для рисования овала
def draw_oval(x, y, width, height, color, fill=True):
    t.penup()
    t.goto(x, y)
    t.pendown()
    if fill:
        t.begin_fill()
    t.color(color)

    t.left(45)
    for _ in range(2):
        t.circle(width, 90)
        t.circle(height, 90)
    t.right(45)

    if fill:
        t.end_fill()


# Функция для рисования прямоугольника
def draw_rectangle(x, y, width, height, color, fill=True):
    t.penup()
    t.goto(x, y)
    t.pendown()
    if fill:
        t.begin_fill()
    t.color(color)
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill:
        t.end_fill()


# Рисуем Кроша
def draw_krosh():
    # Основное тело (большой синий круг)
    draw_circle(0, 0, 120, "lightblue")

    # Уши (два овала)
    draw_oval(-20, 120, 80, 5, "lightblue")  # Левое ухо
    draw_oval(40, 115, 80, 5, "lightblue")  # Правое ухо

    # Внутренняя часть ушей
    draw_oval(-20, 135, 50, 5, "white")  # Левое ухо внутреннее
    draw_oval(40, 130, 50, 5, "white")  # Правое ухо внутреннее

    # Глаза (большие белые круги)
    draw_circle(-40, 40, 35, "white")  # Левый глаз
    draw_circle(40, 40, 35, "white")  # Правый глаз

    # Зрачки (синие круги)
    draw_circle(-35, 55, 15, "blue")  # Левый зрачок
    draw_circle(45, 55, 15, "blue")  # Правый зрачок

    # Блики в глазах
    draw_circle(-40, 65, 5, "white")  # Блик левый
    draw_circle(40, 65, 5, "white")  # Блик правый

    # Нос (черный овал)
    draw_oval(5, 10, 15, 10, "black")  # Нос

    # Рот (дуга)
    t.penup()
    t.goto(-20, -20)
    t.pendown()
    t.color("black")
    t.setheading(-30)
    t.circle(30, 60)

    # Зубы (прямоугольники)
    draw_rectangle(-8, -25, 5, 8, "white")  # Левый зуб
    draw_rectangle(3, -25, 5, 8, "white")  # Правый зуб

    # Лапы (ноги) - расположены снизу
    draw_oval(-30, -130, 25, 15, "lightblue")  # Левая нога
    draw_oval(25, -130, 25, 15, "lightblue")  # Правая нога

    # Руки - расположены по бокам
    draw_oval(-110, 0, 20, 15, "lightblue")  # Левая рука
    draw_oval(140, 0, 20, 15, "lightblue")  # Правая рука

    # Брови (дуги над глазами)
    t.penup()
    t.goto(-65, 85)
    t.pendown()
    t.color("black")
    t.setheading(20)
    t.circle(25, 40)

    t.penup()
    t.goto(15, 85)
    t.pendown()
    t.setheading(20)
    t.circle(25, 40)


# Рисуем Кроша
draw_krosh()

# Подпись
t.penup()
t.goto(-120, -180)
t.color("black")
t.write("Крош из Смешариков", font=("Arial", 16, "bold"))

# Скрываем черепашку и завершаем
t.hideturtle()
screen.exitonclick()