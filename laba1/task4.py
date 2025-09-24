
summa = int(input("Введите сумму в рублях: "))

k100 = summa // 100
summa = summa % 100

k50 = summa // 50
summa = summa % 50

k10 = summa // 10
summa = summa % 10

k5 = summa // 5
summa = summa % 5

m2 = summa // 2
m1 = summa % 2

print(f"Купюры по 100: {k100}")
print(f"Купюры по 50: {k50}")
print(f"Купюры по 10: {k10}")
print(f"Купюры по 5: {k5}")
print(f"Монеты по 2: {m2}")
print(f"Монеты по 1: {m1}")