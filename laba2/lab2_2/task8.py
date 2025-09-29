import time

def timing(func):
    def wrapper(*args, kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # преобразуем в миллисекунды

        print(f"Функция {func.__name__} выполнилась за {execution_time:.2f} мс")

        return result

    return wrapper

@timing
def slow_function():
    """Функция с искусственной задержкой"""
    time.sleep(0.1)  # Задержка 100 мс
    return "Готово!"

@timing
def fast_function():
    """Быстрая функция"""
    return "Быстро!"

@timing
def sum_large_list():
    """Суммирование большого списка"""
    numbers = list(range(1000000))
    return sum(numbers)

@timing
def fibonacci(n):
    """Вычисление n-го числа Фибоначчи"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

@timing
def process_data(data_size):
    """Обработка данных различного размера"""
    data = [i  2
    for i in range(data_size)]
    return len(data)

print("=== Тест 1: Функция с задержкой ===")
result1 = slow_function()
print(f"Результат: {result1}")

print("\n=== Тест 2: Быстрая функция ===")
result2 = fast_function()
print(f"Результат: {result2}")

print("\n=== Тест 3: Суммирование большого списка ===")
result3 = sum_large_list()
print(f"Результат: {result3}")

print("\n=== Тест 4: Рекурсивная функция ===")
result4 = fibonacci(20)
print(f"fibonacci(20) = {result4}")

print("\n=== Тест 5: Функция с параметром ===")
result5 = process_data(100000)
print(f"Обработано элементов: {result5}")

print("\n=== Тест 6: Сравнение времени для разных размеров данных ===")
for size in [1000, 10000, 100000]:
    process_data(size)