# АНАЛИЗ ДИНАМИКИ ПРОДАЖ И ПРОГНОЗИРОВАНИЕ
print("=" * 80)
print("АНАЛИЗ ДИНАМИКИ ПРОДАЖ И ПРОГНОЗИРОВАНИЕ")
print("=" * 80)

# 1. СОЗДАНИЕ ДАННЫХ О ПРОДАЖАХ
print("\n1. СОЗДАНИЕ ДАННЫХ О ПРОДАЖАХ")
print("-" * 40)

# Базовые данные
products = ['Ноутбуки', 'Смартфоны', 'Планшеты', 'Наушники', 'Мониторы', 'Клавиатуры']
stores = ['Магазин А', 'Магазин Б', 'Магазин В', 'Магазин Г', 'Интернет-магазин']
months = ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек']

# Базовые цены и себестоимости
base_prices = {
    'Ноутбуки': 50000,
    'Смартфоны': 30000,
    'Планшеты': 25000,
    'Наушники': 5000,
    'Мониторы': 15000,
    'Клавиатуры': 2000
}

sales_data = []

# Генерация данных продаж
for month_index in range(12):
    for product in products:
        for store in stores:
            # Случайное количество с ростом со временем
            quantity = (20 + month_index * 5) + (month_index * 3)
            if product == 'Наушники':
                quantity *= 2
            elif product == 'Клавиатуры':
                quantity *= 3

            # Цена с небольшими колебаниями
            base_price = base_prices[product]
            price = base_price * (0.95 + (month_index % 3) * 0.05)
            cost_price = base_price * 0.6

            revenue = quantity * price
            profit = quantity * (price - cost_price)

            sales_data.append({
                'month': months[month_index],
                'month_number': month_index + 1,
                'product': product,
                'store': store,
                'quantity': quantity,
                'price': price,
                'cost_price': cost_price,
                'revenue': revenue,
                'profit': profit
            })

print(f"Сгенерировано записей: {len(sales_data)}")
print(f"Уникальных товаров: {len(products)}")
print(f"Точек продаж: {len(stores)}")
print(f"Период анализа: {len(months)} месяцев")

# 2. ОБЩАЯ СТАТИСТИКА ПРОДАЖ
print("\n2. ОБЩАЯ СТАТИСТИКА ПРОДАЖ")
print("-" * 40)

# Расчет общей статистики по товарам
product_statistics = {}

for product in products:
    total_quantity = 0
    total_revenue = 0
    total_profit = 0
    sum_prices = 0
    sum_cost_prices = 0
    record_count = 0

    for record in sales_data:
        if record['product'] == product:
            total_quantity += record['quantity']
            total_revenue += record['revenue']
            total_profit += record['profit']
            sum_prices += record['price']
            sum_cost_prices += record['cost_price']
            record_count += 1

    average_price = sum_prices / record_count if record_count > 0 else 0
    average_cost_price = sum_cost_prices / record_count if record_count > 0 else 0
    profitability = (total_profit / total_revenue * 100) if total_revenue > 0 else 0

    product_statistics[product] = {
        'quantity': total_quantity,
        'revenue': total_revenue,
        'profit': total_profit,
        'average_price': average_price,
        'average_cost_price': average_cost_price,
        'profitability': profitability
    }

print("\nОБЩАЯ СТАТИСТИКА ПО ТОВАРАМ:")
print("Товар".ljust(15) + "Кол-во".rjust(10) + "Выручка".rjust(15) + "Прибыль".rjust(15) + "Рент.%".rjust(10))
print("-" * 65)

for product, stats in product_statistics.items():
    print(
        f"{product:<15}{stats['quantity']:>10,.0f}{stats['revenue']:>15,.0f}{stats['profit']:>15,.0f}{stats['profitability']:>10.1f}")

# 3. ДИНАМИКА ПРОДАЖ ПО МЕСЯЦАМ
print("\n3. ДИНАМИКА ПРОДАЖ ПО МЕСЯЦАМ")
print("-" * 40)

monthly_dynamics = {}

for month in months:
    monthly_dynamics[month] = {
        'total_revenue': 0,
        'total_quantity': 0,
        'product_quantities': {}
    }

    for record in sales_data:
        if record['month'] == month:
            monthly_dynamics[month]['total_revenue'] += record['revenue']
            monthly_dynamics[month]['total_quantity'] += record['quantity']

            product = record['product']
            if product not in monthly_dynamics[month]['product_quantities']:
                monthly_dynamics[month]['product_quantities'][product] = 0
            monthly_dynamics[month]['product_quantities'][product] += record['quantity']

print("\nДИНАМИКА ВЫРУЧКИ ПО МЕСЯЦАМ:")
print("Месяц".ljust(10) + "Выручка".rjust(15) + "Кол-во".rjust(10) + "Топ товар".ljust(15))
print("-" * 50)

for month in months:
    data = monthly_dynamics[month]
    top_product = max(data['product_quantities'].items(), key=lambda x: x[1])[0] if data[
        'product_quantities'] else "Нет данных"
    print(f"{month:<10}{data['total_revenue']:>15,.0f}{data['total_quantity']:>10,.0f}  {top_product:<15}")

# 4. АНАЛИЗ ПО ТОЧКАМ ПРОДАЖ
print("\n4. АНАЛИЗ ЭФФЕКТИВНОСТИ ТОЧЕК ПРОДАЖ")
print("-" * 40)

store_statistics = {}

for store in stores:
    total_quantity = 0
    total_revenue = 0
    total_profit = 0
    unique_products = set()

    for record in sales_data:
        if record['store'] == store:
            total_quantity += record['quantity']
            total_revenue += record['revenue']
            total_profit += record['profit']
            unique_products.add(record['product'])

    average_sales = total_revenue / len(months)
    profitability = (total_profit / total_revenue * 100) if total_revenue > 0 else 0

    store_statistics[store] = {
        'quantity': total_quantity,
        'revenue': total_revenue,
        'profit': total_profit,
        'unique_products': len(unique_products),
        'average_sales': average_sales,
        'profitability': profitability
    }

print("\nСТАТИСТИКА ПО ТОЧКАМ ПРОДАЖ:")
print("Точка".ljust(20) + "Выручка".rjust(15) + "Прибыль".rjust(15) + "Средние".rjust(15) + "Рент.%".rjust(10))
print("-" * 75)

for store, stats in store_statistics.items():
    print(
        f"{store:<20}{stats['revenue']:>15,.0f}{stats['profit']:>15,.0f}{stats['average_sales']:>15,.0f}{stats['profitability']:>10.1f}")

# 5. АНАЛИЗ РОСТА/СПАДА
print("\n5. АНАЛИЗ РОСТА И СПАДА ПРОДАЖ")
print("-" * 40)

# Сравнение первого и последнего месяца
first_month = 'Янв'
last_month = 'Дек'

growth_analysis = {}

for product in products:
    revenue_first = 0
    revenue_last = 0

    for record in sales_data:
        if record['product'] == product:
            if record['month'] == first_month:
                revenue_first += record['revenue']
            elif record['month'] == last_month:
                revenue_last += record['revenue']

    growth = ((revenue_last - revenue_first) / revenue_first * 100) if revenue_first > 0 else 0

    growth_analysis[product] = {
        'revenue_start': revenue_first,
        'revenue_end': revenue_last,
        'growth_percent': growth
    }

print("\nАНАЛИЗ РОСТА ПРОДАЖ ЗА ПЕРИОД:")
print("Товар".ljust(15) + "Начало".rjust(15) + "Конец".rjust(15) + "Рост%".rjust(10))
print("-" * 55)

for product, stats in growth_analysis.items():
    status = "↑" if stats['growth_percent'] > 0 else "↓"
    print(
        f"{product:<15}{stats['revenue_start']:>15,.0f}{stats['revenue_end']:>15,.0f}{stats['growth_percent']:>9.1f}% {status}")

# 6. ПРОГНОЗИРОВАНИЕ ПРОДАЖ
print("\n6. ПРОГНОЗИРОВАНИЕ ПРОДАЖ НА СЛЕДУЮЩИЙ ПЕРИОД")
print("-" * 40)

# Простой прогноз на основе линейного роста
forecast_results = []

for product in products:
    # Собираем данные по месяцам
    revenue_by_month = []
    for month in months:
        monthly_revenue = 0
        for record in sales_data:
            if record['product'] == product and record['month'] == month:
                monthly_revenue += record['revenue']
        revenue_by_month.append(monthly_revenue)

    # Простой прогноз: средний рост последних 3 месяцев
    if len(revenue_by_month) >= 4:
        last_3_months = revenue_by_month[-3:]
        average_growth = 0
        for i in range(1, len(last_3_months)):
            growth = (last_3_months[i] - last_3_months[i - 1]) / last_3_months[i - 1] if last_3_months[i - 1] > 0 else 0
            average_growth += growth

        average_growth = average_growth / 2 if len(last_3_months) > 1 else 0
        current_revenue = revenue_by_month[-1]
        forecast_revenue = current_revenue * (1 + average_growth)
        trend = average_growth * 100
    else:
        current_revenue = revenue_by_month[-1] if revenue_by_month else 0
        forecast_revenue = current_revenue
        trend = 0

    forecast_results.append({
        'product': product,
        'current_revenue': current_revenue,
        'forecast_revenue': forecast_revenue,
        'trend_percent': trend
    })

print("\nПРОГНОЗ ПРОДАЖ НА СЛЕДУЮЩИЙ МЕСЯЦ:")
print("Товар".ljust(15) + "Текущая".rjust(15) + "Прогноз".rjust(15) + "Тренд%".rjust(10))
print("-" * 55)

for forecast in forecast_results:
    status = "↑" if forecast['trend_percent'] > 0 else "↓"
    print(
        f"{forecast['product']:<15}{forecast['current_revenue']:>15,.0f}{forecast['forecast_revenue']:>15,.0f}{forecast['trend_percent']:>9.1f}% {status}")

# 7. СВОДНЫЙ ОТЧЕТ
print("\n" + "=" * 80)
print("СВОДНЫЙ ОТЧЕТ ПО АНАЛИЗУ ПРОДАЖ")
print("=" * 80)

# Расчет общих показателей
total_revenue = sum(record['revenue'] for record in sales_data)
total_profit = sum(record['profit'] for record in sales_data)
total_quantity = sum(record['quantity'] for record in sales_data)
average_profitability = (total_profit / total_revenue * 100) if total_revenue > 0 else 0

print(f"\nОБЩИЕ ПОКАЗАТЕЛИ ЗА ПЕРИОД:")
print(f"▪ Общая выручка: {total_revenue:,.0f} руб.")
print(f"▪ Общая прибыль: {total_profit:,.0f} руб.")
print(f"▪ Средняя рентабельность: {average_profitability:.1f}%")
print(f"▪ Общее количество продаж: {total_quantity:,} шт.")
print(f"▪ Количество товарных позиций: {len(products)}")
print(f"▪ Количество точек продаж: {len(stores)}")

# Топ-3 товара по выручке
top_products = sorted(product_statistics.items(), key=lambda x: x[1]['revenue'], reverse=True)[:3]

print(f"\nТОП-3 ТОВАРА ПО ВЫРУЧКЕ:")
for i, (product, stats) in enumerate(top_products, 1):
    print(f"{i}. {product}: {stats['revenue']:,.0f} руб. (рентабельность: {stats['profitability']:.1f}%)")

# Топ-3 точки по выручке
top_stores = sorted(store_statistics.items(), key=lambda x: x[1]['revenue'], reverse=True)[:3]

print(f"\nТОП-3 ТОЧКИ ПРОДАЖ:")
for i, (store, stats) in enumerate(top_stores, 1):
    print(f"{i}. {store}: {stats['revenue']:,.0f} руб.")

# Наибольший рост
top_growth = sorted(growth_analysis.items(), key=lambda x: x[1]['growth_percent'], reverse=True)[:3]

print(f"\nНАИБОЛЬШИЙ РОСТ ПРОДАЖ:")
for i, (product, stats) in enumerate(top_growth, 1):
    print(f"{i}. {product}: +{stats['growth_percent']:.1f}%")

# Перспективные товары
promising_products = sorted(forecast_results, key=lambda x: x['trend_percent'], reverse=True)[:3]

print(f"\nПЕРСПЕКТИВНЫЕ ТОВАРЫ (по прогнозу):")
for i, product in enumerate(promising_products, 1):
    print(f"{i}. {product['product']}: прогноз роста +{product['trend_percent']:.1f}%")

# 8. ВИЗУАЛИЗАЦИЯ ДАННЫХ В ТЕКСТОВОМ ФОРМАТЕ
print("\n" + "=" * 50)
print("ВИЗУАЛИЗАЦИЯ ДАННЫХ")
print("=" * 50)

print("\nДИАГРАММА ВЫРУЧКИ ПО ТОВАРАМ:")
for product, stats in product_statistics.items():
    percent = (stats['revenue'] / total_revenue * 100) if total_revenue > 0 else 0
    bar = '█' * int(percent / 2)
    print(f"{product:<15} {bar} {percent:5.1f}% ({stats['revenue']:,.0f} руб.)")

print("\nДИАГРАММА ВЫРУЧКИ ПО ТОЧКАМ:")
for store, stats in store_statistics.items():
    percent = (stats['revenue'] / total_revenue * 100) if total_revenue > 0 else 0
    bar = '█' * int(percent / 2)
    print(f"{store:<20} {bar} {percent:5.1f}%")

print("\nДИНАМИКА ОБЩЕЙ ВЫРУЧКИ ПО МЕСЯЦАМ:")
max_revenue = max(monthly_dynamics[month]['total_revenue'] for month in months)
for month in months:
    revenue = monthly_dynamics[month]['total_revenue']
    percent = (revenue / max_revenue * 100) if max_revenue > 0 else 0
    bar = '█' * int(percent / 5)
    print(f"{month:<5} {bar} {revenue:>15,.0f} руб.")

# 9. РЕКОМЕНДАЦИИ
print("\n" + "=" * 50)
print("РЕКОМЕНДАЦИИ ПО РЕЗУЛЬТАТАМ АНАЛИЗА")
print("=" * 50)

print("""
1. ФОКУС НА ВЫСОКОМАРЖИНАЛЬНЫХ ТОВАРАХ:
   • Увеличить продвижение товаров с наибольшей рентабельностью
   • Оптимизировать ассортимент в каждой точке продаж

2. РАЗВИТИЕ ЭФФЕКТИВНЫХ КАНАЛОВ:
   • Усилить работу с наиболее прибыльными точками продаж
   • Изучить успешные практики лидирующих точек

3. СТИМУЛИРОВАНИЕ РОСТА:
   • Разработать акции для товаров с положительным трендом
   • Проанализировать причины спада по отдельным позициям

4. ПЛАНИРОВАНИЕ ЗАПАСОВ:
   • Учесть прогнозные значения при формировании закупок
   • Оптимизировать складские остатки

5. МОНИТОРИНГ ЭФФЕКТИВНОСТИ:
   • Внедрить ежемесячный анализ ключевых показателей
   • Сравнивать фактические результаты с прогнозами
""")

print("\n" + "=" * 80)
print("АНАЛИЗ ЗАВЕРШЕН!")
print("=" * 80)