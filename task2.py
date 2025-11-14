# Ввод данных
lengths = list(map(int, input("Введите длины участков через пробел: ").split()))
speeds = list(map(int, input("Введите скорости на участках через пробел: ").split()))
k = int(input("Номер участка въезда k: "))
p = int(input("Номер участка выезда p: "))

# Участки нумеруются с 1, значит переводим в индексы Python
start = k - 1
end = p - 1

# Вычисление длины пути
distance = sum(lengths[start:end+1])

# Время на каждом участке = длина / скорость
time = sum(lengths[i] / speeds[i] for i in range(start, end+1))

# Средняя скорость: S / T
average_speed = distance / time

# Вывод результатов
print(f"S = {distance} км")
print(f"T = {time:.2f} час")
print(f"V = {average_speed:.2f} км/ч")
