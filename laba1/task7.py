
sec = int(input("Введите количество секунд: "))


m = sec // 60
f_sec = sec % 60

# Вывод результата
print(f"{sec} – {m} минута {f_sec} секунд")