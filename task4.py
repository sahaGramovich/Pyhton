import math


# Простая функция для определенного интеграла методом прямоугольников
def calculate_integral(f, a, b, n=1000):
    """
    Вычисляет определенный интеграл функции f от a до b
    using rectangle method
    """
    h = (b - a) / n
    total = 0

    for i in range(n):
        x = a + i * h
        total += f(x) * h

    return total


# Простая функция для двойного интеграла
def calculate_double_integral(f, a, b, c, d, n=100):
    """
    Вычисляет двойной интеграл функции f(x,y)
    по области [a,b] x [c,d]
    """
    hx = (b - a) / n
    hy = (d - c) / n
    total = 0

    for i in range(n):
        x = a + i * hx
        for j in range(n):
            y = c + j * hy
            total += f(x, y) * hx * hy

    return total


# Примеры функций
def f1(x):
    """f(x) = x²"""
    return x ** 2


def f2(x):
    """f(x) = sin(x)"""
    return math.sin(x)


def f3(x, y):
    """f(x,y) = x + y"""
    return x + y


def f4(x, y):
    """f(x,y) = x * y"""
    return x * y


# Основная программа
print("ВЫЧИСЛЕНИЕ ИНТЕГРАЛОВ")
print("=" * 40)

# Определенный интеграл 1: ∫x² dx от 0 до 1
result1 = calculate_integral(f1, 0, 1)
print(f"\n1. ∫x² dx от 0 до 1")
print(f"   Результат: {result1:.4f}")
print(f"   Точное значение: 0.3333")
print(f"   Ошибка: {abs(result1 - 1 / 3):.4f}")

# Определенный интеграл 2: ∫sin(x) dx от 0 до π
result2 = calculate_integral(f2, 0, math.pi)
print(f"\n2. ∫sin(x) dx от 0 до π")
print(f"   Результат: {result2:.4f}")
print(f"   Точное значение: 2.0000")
print(f"   Ошибка: {abs(result2 - 2):.4f}")

# Двойной интеграл 1: ∫∫(x+y) dy dx от 0 до 1
result3 = calculate_double_integral(f3, 0, 1, 0, 1)
print(f"\n3. ∫∫(x+y) dy dx от 0 до 1")
print(f"   Результат: {result3:.4f}")
print(f"   Точное значение: 1.0000")

# Двойной интеграл 2: ∫∫(x*y) dy dx от 0 до 2
result4 = calculate_double_integral(f4, 0, 2, 0, 1)
print(f"\n4. ∫∫(x*y) dy dx от 0 до 2")
print(f"   Результат: {result4:.4f}")
print(f"   Точное значение: 1.0000")

print("\n" + "=" * 40)
print("Готово!")