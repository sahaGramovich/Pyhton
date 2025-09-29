import datetime


def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            args_str = ", ".join([repr(arg) for arg in args])
            kwargs_str = ", ".join([f"{key}={repr(value)}" for key, value in kwargs.items()])
            all_args = ", ".join(filter(None, [args_str, kwargs_str]))

            with open(filename, 'a', encoding='utf-8') as file:
                file.write(f"{current_time} - {func.name}({all_args})\n")

            return func(*args, **kwargs)

        return wrapper

    return decorator

@log_calls("function_calls.log")
def add_numbers(a, b):
    return a + b

@log_calls("function_calls.log")
def multiply_numbers(x, y, multiplier=1):
    return x * y * multiplier


@log_calls("function_calls.log")
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


print(add_numbers(5, 3))
print(multiply_numbers(4, 5))
print(multiply_numbers(2, 3, multiplier=10))
print(greet("Alice"))
print(greet("Bob", greeting="Hi"))

@log_calls("function_calls.log")
def get_current_time():
    return datetime.datetime.now()

print(get_current_time())