import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker
import random
from datetime import datetime, timedelta
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# 1. Генерация данных
fake = Faker("ru_RU")
np.random.seed(42)
random.seed(42)

n_rows = 150
products = ["Ноутбук", "Смартфон", "Планшет", "Монитор", "Принтер"]
shops = ["Точка A", "Точка B", "Точка C", "Точка D"]

start_date = datetime(2024, 1, 1)
dates = [start_date + timedelta(days=random.randint(0, 364)) for _ in range(n_rows)]

data = []
for _ in range(n_rows):
    product = random.choice(products)
    shop = random.choice(shops)
    quantity = random.randint(1, 15)
    cost = round(random.uniform(10000, 80000), 2)  # себестоимость
    price = round(cost * random.uniform(1.1, 1.5), 2)  # цена продажи
    total = round(price * quantity, 2)
    profit = round((price - cost) * quantity, 2)
    date = random.choice(dates)
    data.append([date, product, shop, quantity, cost, price, total, profit])

cols = [
    "Дата", "Товар", "Точка продажи", "Количество",
    "Себестоимость", "Цена", "Сумма продаж", "Прибыль"
]

df = pd.DataFrame(data, columns=cols)
df = df.sort_values("Дата").reset_index(drop=True)
df.index = range(1, len(df) + 1)

print("Первые 5 строк данных:\n", df.head(), "\n")

# 2. Описательная статистика
print("📊 Общие статистики по продажам:")
print(df[["Количество", "Сумма продаж", "Прибыль"]].describe(), "\n")

# 3. Анализ динамики продаж
sns.set(style="whitegrid", palette="muted")

# 3.1 Динамика продаж по датам
daily_sales = df.groupby("Дата")["Сумма продаж"].sum()
plt.figure(figsize=(10, 4))
daily_sales.plot()
plt.title("Динамика продаж (ежедневно)")
plt.xlabel("Дата")
plt.ylabel("Сумма продаж (₽)")
plt.tight_layout()
plt.show()

# 3.2 Продажи по товарам
plt.figure(figsize=(7, 4))
sns.barplot(x="Товар", y="Сумма продаж", data=df, estimator=np.sum, errorbar=None)
plt.title("Объем продаж по видам товаров")
plt.tight_layout()
plt.show()

# 3.3 Продажи по точкам
plt.figure(figsize=(7, 4))
sns.barplot(x="Точка продажи", y="Сумма продаж", data=df, estimator=np.sum, errorbar=None)
plt.title("Объем продаж по точкам реализации")
plt.tight_layout()
plt.show()

# 3.4 Средняя цена и прибыльность товаров
product_summary = df.groupby("Товар")[["Себестоимость", "Цена", "Прибыль"]].mean().round(2)
print("Средние показатели по товарам:\n", product_summary, "\n")

plt.figure(figsize=(7, 4))
sns.barplot(x=product_summary.index, y=product_summary["Прибыль"])
plt.title("Средняя прибыль по товарам")
plt.tight_layout()
plt.show()

# 4. Прогноз продаж
# Аггрегируем по дням
daily_sum = df.groupby("Дата")["Сумма продаж"].sum().asfreq("D").fillna(0)

# Простая модель Хольта-Винтерса (Exponential Smoothing)
model = ExponentialSmoothing(daily_sum, trend="add", seasonal=None, initialization_method="estimated")
fit = model.fit(optimized=True)

forecast_days = 30
forecast = fit.forecast(forecast_days)

# Визуализация прогноза
plt.figure(figsize=(10, 4))
plt.plot(daily_sum.index, daily_sum.values, label="Исторические данные")
plt.plot(forecast.index, forecast.values, "--", label="Прогноз на 30 дней")
plt.title("Прогноз продаж (Exponential Smoothing)")
plt.xlabel("Дата")
plt.ylabel("Сумма продаж (₽)")
plt.legend()
plt.tight_layout()
plt.show()

# 5. Сохранение результатов
df.to_csv("sales_data.csv", index=False, encoding="utf-8-sig")
forecast_df = pd.DataFrame({"Дата": forecast.index, "Прогноз продаж": forecast.values})
forecast_df.to_csv("sales_forecast.csv", index=False, encoding="utf-8-sig")

print("Файлы 'sales_data.csv' и 'sales_forecast.csv' сохранены.")