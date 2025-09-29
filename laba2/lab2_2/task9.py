def type_check(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i, (arg, expected_type) in enumerate(zip(args, expected_types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Аргумент {i + 1} должен быть типа {expected_type.name}, "
                                    f"получен {type(arg).name}")

            if len(args) > len(expected_types):
                raise TypeError(f"Функция ожидает {len(expected_types)} аргументов, "
                                f"получено {len(args)}")

            return func(*args, **kwargs)

        return wrapper

    return decorator

print("=== Базовые примеры ===")

@type_check(int, int)
def add(a, b):
    return a + b

try:
    result = add(5, 3)
    print(f"add(5, 3) = {result}")
except TypeError as e:
    print(f"Ошибка: {e}")

try:
    result = add(5, "3")
    print(f"add(5, '3') = {result}")
except TypeError as e:
    print(f"Ошибка: {e}")

try:
    result = add(5.5, 3)
    print(f"add(5.5, 3) = {result}")
except TypeError as e:
    print(f"Ошибка: {e}")

print("\n=== Разные типы данных ===")

@type_check(str, int)
def repeat_string(s, n):
    return s * n

@type_check(float, float)
def divide(a, b):
    return a / b

@type_check(list, int)
def get_element(lst, index):
    return lst[index]

try:
    print(f"repeat_string('hello', 3) = {repeat_string('hello', 3)}")
except TypeError as e:
    print(f"Ошибка: {e}")

try:
    print(f"divide(10.0, 2.5) = {divide(10.0, 2.5)}")
except TypeError as e:
    print(f"Ошибка: {e}")

try:
    print(f"get_element([1, 2, 3], 1) = {get_element([1, 2, 3], 1)}")
except TypeError as e:
    print(f"Ошибка: {e}")

print("\n=== Проверка количества аргументов ===")

@type_check(int)
def square(x):
    return x * x

try:
    print(f"square(5) = {square(5)}")
except TypeError as e:
    print(f"Ошибка: {e}")

try:
    print(f"square(5, 10) = {square(5, 10)}")
except TypeError as e:
    print(f"Ошибка: {e}")

print("\n=== Сложные типы ===")

@type_check(str, (list, tuple))  # Второй аргумент может быть list или tuple
def process_data(name, data):
    return f"{name}: {len(data)} элементов"

try:
    print(f"process_data('test', [1, 2, 3]) = {process_data('test', [1, 2, 3])}")
except TypeError as e:
    print(f"Ошибка: {e}")

try:
    print(f"process_data('test', (1, 2, 3)) = {process_data('test', (1, 2, 3))}")
except TypeError as e:
    print(f"Ошибка: {e}")

try:
    print(f"process_data('test', 'string') = {process_data('test', 'string')}")
except TypeError as e:
    print(f"Ошибка: {e}")