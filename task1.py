import numpy as np

# Расходы по месяцам (пример)
expenses = np.array([45, 40, 42, 38, 37, 35, 30, 32, 34, 39, 41, 44])

# зима: декабрь (12), январь (1), февраль (2)
winter_months = [11, 0, 1]
# лето: июнь (6), июль (7), август (8)
summer_months = [5, 6, 7]

winter_sum = np.sum(expenses[winter_months])
summer_sum = np.sum(expenses[summer_months])

print(f"Расходы зимой: {winter_sum}")
print(f"Расходы летом: {summer_sum}")

if winter_sum > summer_sum:
    print("Зимой тратится больше.")
elif summer_sum > winter_sum:
    print("Летом тратится больше.")
else:
    print("Расходы одинаковы.")

max_months = np.where(expenses == np.max(expenses))[0] + 1  # +1, чтобы месяцы начинались с 1
print(f"Месяцы с максимальными расходами: {max_months}")