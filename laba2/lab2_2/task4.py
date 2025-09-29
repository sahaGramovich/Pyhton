def transpose_matrix(matrix):
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)

    return result

def input_matrix():
    print("Введите матрицу построчно (числа через пробел, пустая строка для завершения):")
    matrix = []
    while True:
        row_input = input().strip()
        if not row_input:
            break
        row = []
        for num in row_input.split():
            try:
                row.append(float(num))
            except ValueError:
                print(f"Элемент '{num}' не является числом, будет пропущен")
        if row:
            matrix.append(row)
    return matrix

def print_matrix(matrix, title="Матрица"):
    print(f"\n{title}:")
    for row in matrix:
        print(" ".join(f"{num:6.1f}" if isinstance(num, float) else f"{num:6}" for num in row))


matrix = input_matrix()

if matrix:
    print_matrix(matrix, "Исходная матрица")

    transposed = transpose_matrix(matrix)

    print_matrix(transposed, "Транспонированная матрица")

    print("\nПроверка: исходная матрица осталась неизменной")
    print_matrix(matrix, "Исходная матрица (проверка)")
else:
    print("Матрица пустая")