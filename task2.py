import numpy as np

# Входные данные
lengths = np.array([20, 8, 9, 18, 5, 12, 16, 16, 6, 7])
speeds = np.array([44, 70, 44, 66, 46, 38, 38, 37, 66, 67])

k = 4  # въехал на участок 4
p = 7  # выехал после 7-го участка

# индексы для Python (начинаются с 0)
start = k - 1
end = p

# отрезки, на которых ехал
segment_lengths = lengths[start:end]
segment_speeds = speeds[start:end]

S = np.sum(segment_lengths)
T = np.sum(segment_lengths / segment_speeds)
V = S / T

print(f"Пройденное расстояние: {S:.0f} км")
print(f"Время в пути: {T:.2f} ч")
print(f"Средняя скорость: {V:.2f} км/ч")
