user_input = input("Введите числа через пробел: ")

numbers = []
for item in user_input.split():
    try:
        numbers.append(float(item))
    except ValueError:
        print(f"Элемент '{item}' не является числом и будет пропущен")

if len(numbers) < 2:
    print("Для поиска второго по величине числа нужно ввести хотя бы 2 числа")
else:

    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num

    second_max = None
    for num in numbers:
        if num != max_number:
            if second_max is None or num > second_max:
                second_max = num

    if second_max is None:
        print("Все числа одинаковые, второго по величине числа нет")
    else:
        print(f"Самое большое число: {max_number}")
        print(f"Второе по величине число: {second_max}")