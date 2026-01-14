import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker
import random

# Создаём генератор фейковых данных
fake = Faker("ru_RU")
np.random.seed(42)
random.seed(42)

# 1. Генерация данных
years = [2020, 2021, 2022, 2023, 2024]
forms = ["очная", "заочная"]
specialties = ["Информатика", "Экономика", "Право", "Дизайн", "Строительство"]

data = []

for _ in range(30):
    fio = fake.name()
    year = random.choice(years)
    form = random.choice(forms)
    score_ct = round(random.uniform(100, 400), 1)
    avg_school = round(random.uniform(6, 10), 2)
    total = round(score_ct * 0.6 + avg_school * 10 * 0.4, 2)
    spec = random.choice(specialties)
    address = fake.address().replace("\n", ", ")
    phone = fake.phone_number()
    data.append([fio, year, form, score_ct, avg_school, total, spec, address, phone])

columns = [
    "ФИО",
    "Год поступления",
    "Форма обучения",
    "Балл ЦТ/ЦЭ",
    "Средний балл аттестата",
    "Общий балл",
    "Специальность",
    "Адрес",
    "Телефон",
]

df = pd.DataFrame(data, columns=columns)
df.reset_index(drop=True, inplace=True)
print(df, "\n")

# 2. Анализ и визуализация
sns.set(style="whitegrid", palette="viridis")

# Средний балл ЦТ/ЦЭ по годам
plt.figure(figsize=(8, 4))
sns.barplot(x="Год поступления", y="Балл ЦТ/ЦЭ", data=df, errorbar=None)
plt.title("Динамика среднего балла ЦТ/ЦЭ по годам")
plt.tight_layout()
plt.show()

# Средний балл аттестата по годам
plt.figure(figsize=(8, 4))
sns.lineplot(x="Год поступления", y="Средний балл аттестата", data=df, marker="o")
plt.title("Средний балл аттестата по годам")
plt.tight_layout()
plt.show()

# Количество поступивших по специальностям
plt.figure(figsize=(7, 4))
sns.countplot(x="Специальность", data=df)
plt.title("Количество поступивших по специальностям")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# Статистика по формам обучения
plt.figure(figsize=(5, 4))
df["Форма обучения"].value_counts().plot.pie(
    autopct="%1.1f%%", startangle=90, colors=sns.color_palette("pastel")
)
plt.ylabel("")
plt.title("Распределение по формам обучения")
plt.tight_layout()
plt.show()

# 3. Сохранение результата
df.to_csv("synthetic_students.csv", index=False, encoding="utf-8-sig")
print(" Файл 'synthetic_students.csv' сохранён.")