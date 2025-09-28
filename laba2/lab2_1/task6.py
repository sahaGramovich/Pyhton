user_input = input("Введите элементы списка через пробел: ")
original_list = user_input.split()

print(f"Исходный список: {original_list}")

unique_list = []
for item in original_list:

    if item not in unique_list:
        unique_list.append(item)

print(f"Список без дубликатов: {unique_list}")