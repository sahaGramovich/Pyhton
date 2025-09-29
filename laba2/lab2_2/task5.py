def cache(func):
    cache_dict = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))

        if key in cache_dict:
            print(f"Возвращаем результат из кэша для аргументов: {args}, {kwargs}")
            return cache_dict[key]

        print(f"Вычисляем результат для аргументов: {args}, {kwargs}")
        result = func(*args, **kwargs)
        cache_dict[key] = result

        return result

    return wrapper

@cache
def fibonacci(n):
    """Вычисление n-го числа Фибоначчи"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

@cache
def multiply(a, b):
    """Умножение двух чисел"""
    return a * b

@cache
def greet(name, greeting="Hello"):
    """Приветствие"""
    return f"{greeting}, {name}!"

print("=== Тест 1: Числа Фибоначчи ===")
print(f"fibonacci(5) = {fibonacci(5)}")
print(f"fibonacci(5) = {fibonacci(5)}")  # Должен взять из кэша
print(f"fibonacci(3) = {fibonacci(3)}")  # Должен взять из кэша
print(f"fibonacci(7) = {fibonacci(7)}")

print("\n=== Тест 2: Умножение ===")
print(f"multiply(3, 4) = {multiply(3, 4)}")
print(f"multiply(3, 4) = {multiply(3, 4)}")  # Должен взять из кэша
print(f"multiply(4, 3) = {multiply(4, 3)}")  # Разные аргументы

print("\n=== Тест 3: Приветствие ===")
print(f"greet('Alice') = {greet('Alice')}")
print(f"greet('Alice') = {greet('Alice')}")  # Должен взять из кэша
print(f"greet('Bob', greeting='Hi') = {greet('Bob', greeting='Hi')}")
print(f"greet('Bob', greeting='Hi') = {greet('Bob', greeting='Hi')}")  # Должен взять из кэша