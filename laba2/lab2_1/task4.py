user_input1 = input("Введите первый набор чисел через пробел: ")
set1 = []
for item in user_input1.split():
    try:
        set1.append(float(item))
    except ValueError:
        print(f"Элемент '{item}' не является числом и будет пропущен")

user_input2 = input("Введите второй набор чисел через пробел: ")
set2 = []
for item in user_input2.split():
    try:
        set2.append(float(item))
    except ValueError:
        print(f"Элемент '{item}' не является числом и будет пропущен")

print("\n" + "="*50)

common_numbers = []
for num in set1:
    if num in set2 and num not in common_numbers:
        common_numbers.append(num)
print(f"1. Числа в обоих наборах: {common_numbers}")

only_in_set1 = []
for num in set1:
    if num not in set2 and num not in only_in_set1:
        only_in_set1.append(num)

only_in_set2 = []
for num in set2:
    if num not in set1 and num not in only_in_set2:
        only_in_set2.append(num)

print(f"2. Числа только в первом наборе: {only_in_set1}")
print(f"   Числа только во втором наборе: {only_in_set2}")

all_except_common = []

for num in set1:
    if num not in common_numbers and num not in all_except_common:
        all_except_common.append(num)

for num in set2:
    if num not in common_numbers and num not in all_except_common:
        all_except_common.append(num)

print(f"3. Все числа кроме общих: {all_except_common}")