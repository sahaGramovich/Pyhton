
user_input = input("Введите числа через пробел: ")

numbers = []
for item in user_input.split():
    try:

        numbers.append(int(item))
    except ValueError:
        try:

            numbers.append(float(item))
        except ValueError:
            # Если и это не получается, пропускаем элемент
            print(f"Элемент '{item}' не является числом и будет пропущен")

print("\n" + "="*50)

unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(f"1. Уникальные числа: {unique_numbers}")

repeated_numbers = []
seen_numbers = []
for num in numbers:
    if num in seen_numbers and num not in repeated_numbers:
        repeated_numbers.append(num)
    seen_numbers.append(num)
print(f"2. Повторяющиеся числа: {repeated_numbers}")

even_numbers = []
odd_numbers = []
for num in numbers:

    if isinstance(num, int):
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
print(f"3. Четные числа: {even_numbers}")
print(f"   Нечетные числа: {odd_numbers}")

negative_numbers = []
for num in numbers:
    if num < 0:
        negative_numbers.append(num)
print(f"4. Отрицательные числа: {negative_numbers}")

float_numbers = []
for num in numbers:
    if isinstance(num, float):
        float_numbers.append(num)
print(f"5. Числа с плавающей точкой: {float_numbers}")

sum_multiple_5 = 0
for num in numbers:
    if num % 5 == 0:
        sum_multiple_5 += num
print(f"6. Сумма чисел, кратных 5: {sum_multiple_5}")

if numbers:
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    print(f"7. Самое большое число: {max_number}")
else:
    print("7. Список чисел пуст")

if numbers:
    min_number = numbers[0]
    for num in numbers:
        if num < min_number:
            min_number = num
    print(f"8. Самое маленькое число: {min_number}")
else:
    print("8. Список чисел пуст")