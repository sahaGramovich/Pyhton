import math


def f(x):
    return 5 / (x**2 - 9)


print("x\t\tf(x)")
print("-" * 30)

for x in range(-10, 11):  # Целые числа от -10 до 10
    try:
        f_val = f(x)
        print(f"{x:4d}\t\t{f_val:12.4f}")
    except ZeroDivisionError:
        print(f"{x:4d}\t\tНе определена (деление на 0)")


print("\nДетальные значения (с шагом 0.5):")
print("x\t\tf(x)")
print("-" * 30)

x_values = [-10, -9, -8, -7, -6, -5, -4, -3.5, -3.1, -3.01, -3, -2.99, -2.9, -2.5,
            -2, -1, 0, 1, 2, 2.5, 2.9, 2.99, 3, 3.01, 3.1, 3.5, 4, 5, 6, 7, 8, 9, 10]

for x in x_values:
    try:
        f_val = f(x)
        print(f"{x:6.2f}\t\t{f_val:12.4f}")
    except ZeroDivisionError:
        print(f"{x:6.2f}\t\tНе определена (деление на 0)")

# Анализ особых точек
print("\nАнализ особых точек:")
print("Особые точки: x = -3 и x = 3 (знаменатель равен 0)")
print("Пределы в особых точках:")


print("\nДля x = -3:")
test_points = [-3.1, -3.01, -3.001, -3.0001, -2.9999, -2.999, -2.99, -2.9]
for x in test_points:
    try:
        f_val = f(x)
        print(f"x = {x:8.4f}, f(x) = {f_val:12.4f}")
    except:
        print(f"x = {x:8.4f}, Ошибка вычисления")


print("\nДля x = 3:")
test_points = [2.9, 2.99, 2.999, 2.9999, 3.0001, 3.001, 3.01, 3.1]
for x in test_points:
    try:
        f_val = f(x)
        print(f"x = {x:8.4f}, f(x) = {f_val:12.4f}")
    except:
        print(f"x = {x:8.4f}, Ошибка вычисления")


print("\nПоведение на бесконечности:")
print("При x -> ±∞, f(x) -> 0 (горизонтальная асимптота y = 0)")
for x in [5, 10, 20, 50, 100]:
    f_val = f(x)
    print(f"x = {x:4d}, f(x) = {f_val:10.6f}")