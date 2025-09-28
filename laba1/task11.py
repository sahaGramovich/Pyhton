month = int(input("Введите месяц: "))
day = int(input("Введите число: "))

print("Ваша дата: " + str(month) + "." + str(day))

if (month == 12 and day >= 22) or (month == 1 and day <= 19):

    sign = "Козерог"

elif (month == 1 and day >= 20) or (month == 2 and day <= 18):

    sign = "Водолей"

elif (month == 2 and day >= 19) or (month == 3 and day <= 20):

    sign = "Рыбы"

elif (month == 3 and day >= 21) or (month == 4 and day <= 19):

    sign = "Овен"

elif (month == 4 and day >= 20) or (month == 5 and day <= 20):

    sign = "Телец"

elif (month == 5 and day >= 21) or (month == 6 and day <= 20):

    sign = "Близнецы"

elif (month == 6 and day >= 21) or (month == 7 and day <= 22):

    sign = "Paк"

elif (month == 7 and day >= 23) or (month == 8 and day <= 22):

    sign = "Лeв"

elif (month == 8 and day >= 23) or (month == 9 and day <= 22):

    sign = "Дева"

elif (month == 9 and day >= 23) or (month == 10 and day <= 22):

    sign = "Becы" 

elif (month == 10 and day >= 23) or (month == 11 and day <= 21):

    sign = "Скорпион"

elif (month == 11 and day >= 22) or (month == 12 and day <= 21):

    sign = "Стрелец"

else:
    sign = "Неизвестно (проверьте правильность ввода)"

print(f"\nВаш знак зодиака: {sign}")
