user_input = input("Введите строку: ")

if not user_input:
    print("Введена пустая строка")
else:

    compressed = ""
    current_char = user_input[0]
    count = 1

    for i in range(1, len(user_input)):
        if user_input[i] == current_char:

            count += 1
        else:

            compressed += current_char + str(count)

            current_char = user_input[i]
            count = 1

    compressed += current_char + str(count)

    print(f"Сжатая строка: {compressed}")