import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker
import random
from datetime import datetime, timedelta

# 1. Генерация синтетических данных
fake = Faker("ru_RU")
np.random.seed(42)
random.seed(42)

n_rows = 30  # количество записей
airports = ["Москва", "Санкт-Петербург", "Новосибирск", "Казань", "Екатеринбург"]
payment_methods = ["Карта", "Наличные", "Онлайн", "Баллы", "Подарочный сертификат"]
passenger_types = ["Обычный", "Постоянный клиент", "VIP"]

start_date = datetime(2023, 1, 1)
dates = [start_date + timedelta(days=random.randint(0, 364)) for _ in range(n_rows)]

data = []

for _ in range(n_rows):
    row = {
        "Дата": random.choice(dates),
        "Аэропорт": random.choice(airports),
        "Способ оплаты": random.choice(payment_methods),
        "Тип пассажира": random.choice(passenger_types),
        "Сумма": round(random.uniform(5000, 50000), 2)
    }
    data.append(row)

df = pd.DataFrame(data)

# Упорядочим по дате
df = df.sort_values(by="Дата").reset_index(drop=True)
df.index = range(1, len(df) + 1)

print("Первые 10 строк датасета:\n", df.head(10), "\n")

# 2. Описательная статистика
print("Описательные статистики по сумме продаж:\n")
print(df["Сумма"].describe(), "\n")

# 3. Анализ данных и визуализация
sns.set(style="whitegrid", palette="muted")

# Продажи по датам
plt.figure(figsize=(10, 4))
daily_sales = df.groupby("Дата")["Сумма"].sum()
daily_sales.plot()
plt.title("Динамика продаж авиабилетов по датам")
plt.xlabel("Дата")
plt.ylabel("Сумма продаж (₽)")
plt.tight_layout()
plt.show()

# Средняя сумма по аэропортам
plt.figure(figsize=(7, 4))
sns.barplot(x="Аэропорт", y="Сумма", data=df, errorbar=None)
plt.title("Средняя сумма продаж по аэропортам")
plt.tight_layout()
plt.show()

# Продажи по способу оплаты
plt.figure(figsize=(7, 4))
sns.boxplot(x="Способ оплаты", y="Сумма", data=df)
plt.title("Распределение сумм по способу оплаты")
plt.xticks(rotation=25)
plt.tight_layout()
plt.show()

# Продажи по типу пассажиров
plt.figure(figsize=(6, 4))
sns.barplot(x="Тип пассажира", y="Сумма", data=df, estimator=np.mean, errorbar=None)
plt.title("Средняя сумма покупки по типу пассажира")
plt.tight_layout()
plt.show()

# 4. Проверка сезонности (по месяцам)
df["Месяц"] = df["Дата"].dt.month

plt.figure(figsize=(8, 4))
sns.lineplot(x="Месяц", y="Сумма", data=df, estimator=np.sum, errorbar=None, marker="o")
plt.title("Сезонность продаж авиабилетов (по месяцам)")
plt.xlabel("Месяц")
plt.ylabel("Сумма продаж (₽)")
plt.tight_layout()
plt.show()

# 5. Сохранение результатов
df.to_csv("air_tickets_sales.csv", index=False, encoding="utf-8-sig")
print("Файл 'air_tickets_sales.csv' сохранён.")