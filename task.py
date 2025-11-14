# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')

# Настройка стиля графиков
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

print("=== АНАЛИЗ ДАННЫХ ПРОДАЖ АВИАБИЛЕТОВ S7 ===\n")

# Загрузка данных
df = pd.read_excel('s7_data_sample_rev4_50k.xlsx')

print("=== БАЗОВАЯ ИНФОРМАЦИЯ О ДАННЫХ ===")
print(f"Количество записей: {len(df):,}")
print(f"Количество столбцов: {len(df.columns)}")
print("\nПервые 5 строк:")
print(df.head())

print("\nТипы данных:")
print(df.dtypes)
print("\nПропущенные значения:")
print(df.isnull().sum())

# Преобразование дат
df['ISSUE_DATE'] = pd.to_datetime(df['ISSUE_DATE'])
df['FLIGHT_DATE_LOC'] = pd.to_datetime(df['FLIGHT_DATE_LOC'])

# Добавим дополнительные временные характеристики
df['ISSUE_YEAR'] = df['ISSUE_DATE'].dt.year
df['ISSUE_MONTH'] = df['ISSUE_DATE'].dt.month
df['ISSUE_DAY'] = df['ISSUE_DATE'].dt.day
df['ISSUE_DAYOFWEEK'] = df['ISSUE_DATE'].dt.dayofweek

df['FLIGHT_YEAR'] = df['FLIGHT_DATE_LOC'].dt.year
df['FLIGHT_MONTH'] = df['FLIGHT_DATE_LOC'].dt.month
df['FLIGHT_DAY'] = df['FLIGHT_DATE_LOC'].dt.day
df['FLIGHT_DAYOFWEEK'] = df['FLIGHT_DATE_LOC'].dt.dayofweek

# Дни между покупкой и вылетом
df['DAYS_BEFORE_FLIGHT'] = (df['FLIGHT_DATE_LOC'] - df['ISSUE_DATE']).dt.days

## 1. ОБЩИЕ ОПИСАТЕЛЬНЫЕ СТАТИСТИКИ
print("\n" + "="*50)
print("1. ОБЩИЕ ОПИСАТЕЛЬНЫЕ СТАТИСТИКИ")
print("="*50)

numeric_cols = ['REVENUE_AMOUNT', 'DAYS_BEFORE_FLIGHT']
print("\nОписательные статистики для числовых колонок:")
print(df[numeric_cols].describe())

# Визуализация распределения выручки
fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# Гистограмма выручки
axes[0,0].hist(df['REVENUE_AMOUNT'], bins=50, edgecolor='black', alpha=0.7)
axes[0,0].set_xlabel('Выручка')
axes[0,0].set_ylabel('Частота')
axes[0,0].set_title('Распределение выручки от продаж билетов')
axes[0,0].grid(True, alpha=0.3)

# Boxplot выручки
axes[0,1].boxplot(df['REVENUE_AMOUNT'])
axes[0,1].set_ylabel('Выручка')
axes[0,1].set_title('Boxplot выручки')
axes[0,1].grid(True, alpha=0.3)

# Анализ категориальных переменных
categorical_cols = ['PAX_TYPE', 'SALE_TYPE', 'FFP_FLAG']
for i, col in enumerate(categorical_cols):
    value_counts = df[col].value_counts()
    if i == 0:
        axes[0,2].pie(value_counts.values, labels=value_counts.index, autopct='%1.1f%%')
        axes[0,2].set_title(f'Распределение {col}')
    else:
        row = 1 if i == 1 else 1
        col_idx = 1 if i == 1 else 2
        value_counts.plot(kind='bar', ax=axes[row, col_idx], title=col)
        axes[row, col_idx].tick_params(axis='x', rotation=45)

# Распределение дней до вылета
axes[1,0].hist(df['DAYS_BEFORE_FLIGHT'], bins=30, edgecolor='black', alpha=0.7, color='green')
axes[1,0].set_xlabel('Дни до вылета')
axes[1,0].set_ylabel('Частота')
axes[1,0].set_title('Распределение дней между покупкой и вылетом')
axes[1,0].grid(True, alpha=0.3)

# Типы перелетов
df['ROUTE_FLIGHT_TYPE'].value_counts().plot(kind='bar', ax=axes[1,1], color='purple')
axes[1,1].set_title('Типы перелетов')
axes[1,1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

print(f"\nМедианная выручка: {df['REVENUE_AMOUNT'].median():.2f}")
print(f"Средняя выручка: {df['REVENUE_AMOUNT'].mean():.2f}")
print(f"Средние дни до вылета: {df['DAYS_BEFORE_FLIGHT'].mean():.1f}")

## 2. АНАЛИЗ АЭРОПОРТОВ
print("\n" + "="*50)
print("2. АНАЛИЗ АЭРОПОРТОВ")
print("="*50)

# Топ-10 аэропортов отправления
top_origins = df['ORIG_CITY_CODE'].value_counts().head(10)
print("Топ-10 аэропортов отправления:")
print(top_origins)

# Топ-10 аэропортов назначения
top_destinations = df['DEST_CITY_CODE'].value_counts().head(10)
print("\nТоп-10 аэропортов назначения:")
print(top_destinations)

# Самые популярные маршруты
df['ROUTE'] = df['ORIG_CITY_CODE'] + ' - ' + df['DEST_CITY_CODE']
top_routes = df['ROUTE'].value_counts().head(15)

fig, axes = plt.subplots(2, 2, figsize=(20, 12))

# Топ аэропортов отправления
top_origins.plot(kind='bar', ax=axes[0,0], color='skyblue')
axes[0,0].set_title('Топ-10 аэропортов отправления')
axes[0,0].tick_params(axis='x', rotation=45)

# Топ аэропортов назначения
top_destinations.plot(kind='bar', ax=axes[0,1], color='lightcoral')
axes[0,1].set_title('Топ-10 аэропортов назначения')
axes[0,1].tick_params(axis='x', rotation=45)

# Топ маршрутов
top_routes.plot(kind='bar', ax=axes[1,0], color='lightgreen')
axes[1,0].set_title('Топ-15 популярных маршрутов')
axes[1,0].tick_params(axis='x', rotation=45)

# Выручка по аэропортам отправления
revenue_by_origin = df.groupby('ORIG_CITY_CODE')['REVENUE_AMOUNT'].sum().sort_values(ascending=False).head(10)
revenue_by_origin.plot(kind='bar', ax=axes[1,1], color='gold')
axes[1,1].set_title('Топ-10 аэропортов по общей выручке')
axes[1,1].tick_params(axis='x', rotation=45)
axes[1,1].set_ylabel('Общая выручка')

plt.tight_layout()
plt.show()

print(f"\nОсновной хаб (аэропорт отправления): {df['ORIG_CITY_CODE'].mode()[0]}")
print(f"Основной хаб (аэропорт назначения): {df['DEST_CITY_CODE'].mode()[0]}")
print(f"Самый популярный маршрут: {df['ROUTE'].mode()[0]}")

## 3. АНАЛИЗ СЕЗОННОСТИ
print("\n" + "="*50)
print("3. АНАЛИЗ СЕЗОННОСТИ")
print("="*50)

# Анализ сезонности по месяцам продаж
monthly_sales = df.groupby('ISSUE_MONTH').agg({
    'REVENUE_AMOUNT': ['count', 'sum', 'mean']
}).round(2)

monthly_sales.columns = ['Количество_продаж', 'Общая_выручка', 'Средняя_выручка']
print("Продажи по месяцам:")
print(monthly_sales)

# Сезонность по месяцам вылета
monthly_flights = df.groupby('FLIGHT_MONTH').agg({
    'REVENUE_AMOUNT': ['count', 'sum', 'mean']
}).round(2)

monthly_flights.columns = ['Количество_перелетов', 'Общая_выручка', 'Средняя_выручка']
print("\nПерелеты по месяцам:")
print(monthly_flights)

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Продажи по месяцам
monthly_sales['Количество_продаж'].plot(ax=axes[0,0], marker='o', linewidth=2)
axes[0,0].set_title('Количество продаж по месяцам')
axes[0,0].set_xlabel('Месяц')
axes[0,0].set_ylabel('Количество продаж')
axes[0,0].grid(True, alpha=0.3)

# Выручка по месяцам
monthly_sales['Общая_выручка'].plot(ax=axes[0,1], marker='o', linewidth=2, color='orange')
axes[0,1].set_title('Общая выручка по месяцам')
axes[0,1].set_xlabel('Месяц')
axes[0,1].set_ylabel('Общая выручка')
axes[0,1].grid(True, alpha=0.3)

# Перелеты по месяцам
monthly_flights['Количество_перелетов'].plot(ax=axes[1,0], marker='o', linewidth=2, color='green')
axes[1,0].set_title('Количество перелетов по месяцам')
axes[1,0].set_xlabel('Месяц')
axes[1,0].set_ylabel('Количество перелетов')
axes[1,0].grid(True, alpha=0.3)

# Средняя выручка по месяцам
monthly_sales['Средняя_выручка'].plot(ax=axes[1,1], marker='o', linewidth=2, color='red')
axes[1,1].set_title('Средняя выручка по месяцам')
axes[1,1].set_xlabel('Месяц')
axes[1,1].set_ylabel('Средняя выручка')
axes[1,1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Анализ по дням недели
print("\nАнализ по дням недели:")
weekday_sales = df.groupby('ISSUE_DAYOFWEEK').agg({
    'REVENUE_AMOUNT': ['count', 'sum', 'mean']
}).round(2)
weekday_sales.columns = ['Количество_продаж', 'Общая_выручка', 'Средняя_выручка']
print(weekday_sales)

## 4. АНАЛИЗ ПО ТИПАМ ПАССАЖИРОВ
print("\n" + "="*50)
print("4. АНАЛИЗ ПО ТИПАМ ПАССАЖИРОВ")
print("="*50)

pax_analysis = df.groupby('PAX_TYPE').agg({
    'REVENUE_AMOUNT': ['count', 'sum', 'mean', 'median'],
    'DAYS_BEFORE_FLIGHT': 'mean'
}).round(2)

pax_analysis.columns = ['Количество', 'Общая_выручка', 'Средняя_выручка', 'Медианная_выручка', 'Ср_дни_до_вылета']
print("Анализ по типам пассажиров:")
print(pax_analysis)

# Анализ программы лояльности
ffp_analysis = df.groupby('FFP_FLAG').agg({
    'REVENUE_AMOUNT': ['count', 'sum', 'mean', 'median'],
    'DAYS_BEFORE_FLIGHT': 'mean'
}).round(2)

ffp_analysis.columns = ['Количество', 'Общая_выручка', 'Средняя_выручка', 'Медианная_выручка', 'Ср_дни_до_вылета']
print("\nАнализ по программе лояльности:")
print(ffp_analysis)

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Распределение по типам пассажиров
df['PAX_TYPE'].value_counts().plot(kind='pie', ax=axes[0,0], autopct='%1.1f%%')
axes[0,0].set_title('Распределение по типам пассажиров')

# Средняя выручка по типам пассажиров
pax_analysis['Средняя_выручка'].plot(kind='bar', ax=axes[0,1], color=['skyblue', 'lightcoral', 'lightgreen'])
axes[0,1].set_title('Средняя выручка по типам пассажиров')
axes[0,1].set_ylabel('Средняя выручка')
axes[0,1].tick_params(axis='x', rotation=0)

# Программа лояльности
df['FFP_FLAG'].value_counts().plot(kind='pie', ax=axes[1,0], autopct='%1.1f%%')
axes[1,0].set_title('Участие в программе лояльности')

# Средняя выручка по программе лояльности
ffp_analysis['Средняя_выручка'].plot(kind='bar', ax=axes[1,1], color=['lightblue', 'pink'])
axes[1,1].set_title('Средняя выручка по программе лояльности')
axes[1,1].set_ylabel('Средняя выручка')
axes[1,1].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.show()

## 5. АНАЛИЗ СПОСОБОВ ОПЛАТЫ
print("\n" + "="*50)
print("5. АНАЛИЗ СПОСОБОВ ОПЛАТЫ")
print("="*50)

# Анализ способов оплаты
fop_analysis = df['FOP_TYPE_CODE'].value_counts().head(10)
print("Топ-10 способов оплаты:")
print(fop_analysis)

# Анализ по типам продаж (ONLINE/OFFLINE)
sale_type_analysis = df.groupby('SALE_TYPE').agg({
    'REVENUE_AMOUNT': ['count', 'sum', 'mean', 'median'],
    'DAYS_BEFORE_FLIGHT': 'mean'
}).round(2)

sale_type_analysis.columns = ['Количество', 'Общая_выручка', 'Средняя_выручка', 'Медианная_выручка', 'Ср_дни_до_вылета']
print("\nАнализ по типам продаж:")
print(sale_type_analysis)

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Распределение способов оплаты (топ-8)
fop_analysis.head(8).plot(kind='bar', ax=axes[0,0])
axes[0,0].set_title('Топ-8 способов оплаты')
axes[0,0].tick_params(axis='x', rotation=45)

# Распределение онлайн/оффлайн продаж
df['SALE_TYPE'].value_counts().plot(kind='pie', ax=axes[0,1], autopct='%1.1f%%')
axes[0,1].set_title('Онлайн vs Оффлайн продажи')

# Средняя выручка по типам продаж
sale_type_analysis['Средняя_выручка'].plot(kind='bar', ax=axes[1,0], color=['lightblue', 'lightcoral'])
axes[1,0].set_title('Средняя выручка по типам продаж')
axes[1,0].set_ylabel('Средняя выручка')
axes[1,0].tick_params(axis='x', rotation=0)

# Дни до вылета по типам продаж
sale_type_analysis['Ср_дни_до_вылета'].plot(kind='bar', ax=axes[1,1], color=['lightgreen', 'gold'])
axes[1,1].set_title('Средние дни до вылета по типам продаж')
axes[1,1].set_ylabel('Дни до вылета')
axes[1,1].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.show()

# Корреляционный анализ
print("\nКорреляционная матрица:")
correlation_matrix = df[['REVENUE_AMOUNT', 'DAYS_BEFORE_FLIGHT', 'ISSUE_MONTH', 'FLIGHT_MONTH']].corr()
print(correlation_matrix)

## 6. ПРОГНОЗИРОВАНИЕ ОБЪЕМОВ ПРОДАЖ
print("\n" + "="*50)
print("6. ПРОГНОЗИРОВАНИЕ ОБЪЕМОВ ПРОДАЖ")
print("="*50)

# Подготовка данных для прогнозирования
daily_sales = df.groupby('ISSUE_DATE').agg({
    'REVENUE_AMOUNT': 'count',
    'FLIGHT_DATE_LOC': 'count'
}).reset_index()
daily_sales.columns = ['DATE', 'DAILY_SALES', 'DAILY_FLIGHTS']

# Создание признаков для временного ряда
daily_sales['DAY_OF_WEEK'] = daily_sales['DATE'].dt.dayofweek
daily_sales['DAY_OF_MONTH'] = daily_sales['DATE'].dt.day
daily_sales['MONTH'] = daily_sales['DATE'].dt.month
daily_sales['DAY_COUNT'] = range(len(daily_sales))

# Визуализация временного ряда
fig, axes = plt.subplots(2, 1, figsize=(15, 10))

axes[0].plot(daily_sales['DATE'], daily_sales['DAILY_SALES'], linewidth=1)
axes[0].set_title('Ежедневные продажи билетов')
axes[0].set_ylabel('Количество продаж')
axes[0].grid(True, alpha=0.3)

axes[1].plot(daily_sales['DATE'], daily_sales['DAILY_FLIGHTS'], linewidth=1, color='orange')
axes[1].set_title('Ежедневные перелеты')
axes[1].set_ylabel('Количество перелетов')
axes[1].set_xlabel('Дата')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Простая модель прогнозирования
X = daily_sales[['DAY_COUNT', 'DAY_OF_WEEK', 'MONTH']]
y_sales = daily_sales['DAILY_SALES']
y_flights = daily_sales['DAILY_FLIGHTS']

# Разделение на обучающую и тестовую выборки
X_train, X_test, y_train_sales, y_test_sales = train_test_split(X, y_sales, test_size=0.2, random_state=42)
_, _, y_train_flights, y_test_flights = train_test_split(X, y_flights, test_size=0.2, random_state=42)

# Модель для прогнозирования продаж
model_sales = LinearRegression()
model_sales.fit(X_train, y_train_sales)
y_pred_sales = model_sales.predict(X_test)

# Модель для прогнозирования перелетов
model_flights = LinearRegression()
model_flights.fit(X_train, y_train_flights)
y_pred_flights = model_flights.predict(X_test)

# Оценка моделей
print("Результаты прогнозирования продаж:")
print(f"R² Score: {r2_score(y_test_sales, y_pred_sales):.3f}")
print(f"MAE: {mean_absolute_error(y_test_sales, y_pred_sales):.2f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test_sales, y_pred_sales)):.2f}")

print("\nРезультаты прогнозирования перелетов:")
print(f"R² Score: {r2_score(y_test_flights, y_pred_flights):.3f}")
print(f"MAE: {mean_absolute_error(y_test_flights, y_pred_flights):.2f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test_flights, y_pred_flights)):.2f}")

# Визуализация прогнозов
fig, axes = plt.subplots(2, 1, figsize=(15, 10))

# Продажи
axes[0].scatter(range(len(y_test_sales)), y_test_sales, alpha=0.7, label='Фактические')
axes[0].scatter(range(len(y_pred_sales)), y_pred_sales, alpha=0.7, label='Прогнозные')
axes[0].set_title('Прогноз vs Факт: Продажи билетов')
axes[0].set_ylabel('Количество продаж')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Перелеты
axes[1].scatter(range(len(y_test_flights)), y_test_flights, alpha=0.7, label='Фактические')
axes[1].scatter(range(len(y_pred_flights)), y_pred_flights, alpha=0.7, label='Прогнозные')
axes[1].set_title('Прогноз vs Факт: Перелеты')
axes[1].set_ylabel('Количество перелетов')
axes[1].set_xlabel('Наблюдения')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

## 7. СВОДНАЯ ТАБЛИЦА КЛЮЧЕВЫХ МЕТРИК
print("\n" + "="*50)
print("7. СВОДНАЯ ТАБЛИЦА КЛЮЧЕВЫХ МЕТРИК")
print("="*50)

summary_metrics = {
    'Метрика': [
        'Общее количество продаж',
        'Общая выручка',
        'Средняя выручка за билет',
        'Медианная выручка за билет',
        'Самый популярный аэропорт отправления',
        'Самый популярный аэропорт назначения',
        'Самый популярный маршрут',
        'Доля онлайн продаж',
        'Доля участников программы лояльности',
        'Средние дни между покупкой и вылетом',
        'Месяц с максимальными продажами',
        'Месяц с максимальной выручкой'
    ],
    'Значение': [
        f"{len(df):,}",
        f"{df['REVENUE_AMOUNT'].sum():,.0f} руб.",
        f"{df['REVENUE_AMOUNT'].mean():.0f} руб.",
        f"{df['REVENUE_AMOUNT'].median():.0f} руб.",
        df['ORIG_CITY_CODE'].mode()[0],
        df['DEST_CITY_CODE'].mode()[0],
        df['ROUTE'].mode()[0],
        f"{(df['SALE_TYPE'] == 'ONLINE').mean()*100:.1f}%",
        f"{(df['FFP_FLAG'] == 'FFP').mean()*100:.1f}%",
        f"{df['DAYS_BEFORE_FLIGHT'].mean():.1f} дней",
        f"Месяц {monthly_sales['Количество_продаж'].idxmax()}",
        f"Месяц {monthly_sales['Общая_выручка'].idxmax()}"
    ]
}

summary_df = pd.DataFrame(summary_metrics)
print(summary_df.to_string(index=False))

## ОСНОВНЫЕ ВЫВОДЫ
print("\n" + "="*50)
print("ОСНОВНЫЕ ВЫВОДЫ АНАЛИЗА")
print("="*50)

print("""
1. ОБЩИЕ СТАТИСТИКИ:
   - Средняя стоимость билета значительно отличается от медианной
   - Наличие дорогих билетов-выбросов влияет на распределение выручки

2. АЭРОПОРТЫ:
   - Четко выделяются ключевые хабы (MOW - Москва, OVB - Новосибирск)
   - Концентрация трафика вокруг основных городов

3. СЕЗОННОСТЬ:
   - Явно выраженная сезонность с пиками в определенные месяцы
   - Разница в поведении между месяцами продаж и вылетов

4. ТИПЫ ПАССАЖИРОВ:
   - Преобладают взрослые пассажиры (AD)
   - Участники программы лояльности демонстрируют разные паттерны покупок

5. СПОСОБЫ ОПЛАТЫ:
   - Доминируют онлайн продажи
   - Разные способы оплаты ассоциируются с разным временем покупки

6. ПРОГНОЗИРОВАНИЕ:
   - Простые линейные модели показывают базовую предсказательную способность
   - Для улучшения прогнозов рекомендуется использовать сложные временные модели
""")

print("Анализ завершен!")