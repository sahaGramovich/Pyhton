def analyze_transport_expenses(expenses):
    """
    Анализирует расходы на проезд по месяцам
    """
    # Названия месяцев для красивого вывода
    months_names = {
        1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель",
        5: "Май", 6: "Июнь", 7: "Июль", 8: "Август",
        9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"
    }

    # Определяем зимние и летние месяцы (номера месяцев с 1 до 12)
    winter_months = [12, 1, 2]  # декабрь, январь, февраль
    summer_months = [6, 7, 8]  # июнь, июль, август

    # Суммируем расходы по сезонам
    winter_total = sum(expenses[month - 1] for month in winter_months)
    summer_total = sum(expenses[month - 1] for month in summer_months)

    # Сравниваем сезоны
    print("Анализ расходов на проезд:")
    print(f"Зимние месяцы {[months_names[m] for m in winter_months]}: {winter_total} руб.")
    print(f"Летние месяцы {[months_names[m] for m in summer_months]}: {summer_total} руб.")

    if winter_total > summer_total:
        print("Больше денег тратится зимой")
    elif summer_total > winter_total:
        print("Больше денег тратится летом")
    else:
        print("Расходы зимой и летом одинаковы")

    # Создаем список кортежей (расход, номер месяца) и сортируем по убыванию расходов
    month_expenses = [(expense, month_num) for month_num, expense in enumerate(expenses, 1)]
    sorted_months = sorted(month_expenses, key=lambda x: x[0], reverse=True)

    print(f"\nВсе месяцы отсортированные по расходам (от наибольшего к наименьшему):")
    print("-" * 50)

    for i, (expense, month_num) in enumerate(sorted_months, 1):
        print(f"{i:2}. {months_names[month_num]:10} ({month_num:2} месяц): {expense:8} руб.")

    return winter_total, summer_total, sorted_months


# Пример использования
if __name__ == "__main__":
    # Ввод данных от пользователя
    print("Введите расходы на проезд по месяцам (12 чисел через пробел):")
    try:
        expenses = list(map(float, input().split()))
        if len(expenses) != 12:
            print("Ошибка: нужно ввести ровно 12 чисел!")
        else:
            analyze_transport_expenses(expenses)
    except ValueError:
        print("Ошибка: введите числа через пробел!")


# Альтернативный вариант с группировкой по одинаковым расходам
def analyze_with_groups(expenses):
    """
    Альтернативная версия с группировкой месяцев по одинаковым расходам
    """
    months_names = {
        1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель",
        5: "Май", 6: "Июнь", 7: "Июль", 8: "Август",
        9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"
    }

    # Создаем словарь для группировки месяцев по расходам
    expense_groups = {}
    for month_num, expense in enumerate(expenses, 1):
        if expense not in expense_groups:
            expense_groups[expense] = []
        expense_groups[expense].append(month_num)

    # Сортируем расходы по убыванию
    sorted_expenses = sorted(expense_groups.items(), key=lambda x: x[0], reverse=True)

    print("\n" + "=" * 60)
    print("Версия с группировкой по одинаковым расходам:")
    print("-" * 60)

    for i, (expense, months_list) in enumerate(sorted_expenses, 1):
        months_str = ", ".join([f"{months_names[m]} ({m})" for m in months_list])
        print(f"{i:2}. Расход: {expense:8} руб. | Месяцы: {months_str}")


