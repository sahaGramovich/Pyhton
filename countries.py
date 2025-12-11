import argparse
import csv
import os
import time
import requests
from bs4 import BeautifulSoup

CACHE_DIR = "cache"
BASE_URL = "https://en.wikipedia.org/wiki/"

os.makedirs(CACHE_DIR, exist_ok=True)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/113.0.0.0 Safari/537.36"
    )
}

def find_capital(infobox):
    labels = [
        "Capital",
        "Capital and largest city",
        "Seat"
    ]

    for th in infobox.find_all("th"):
        text = th.get_text(" ", strip=True)

        for label in labels:
            if label in text:
                td = th.find_next("td")
                if not td:
                    continue

                # Берём первую ссылку обычно именно столица
                a = td.find("a")
                if a:
                    return a.get_text(strip=True)

                return td.get_text(" ", strip=True)

    return None


def extract_number(text):
    """Извлекает первое число из строки (для площади и населения)."""
    if not text:
        return None

    cleaned = text.replace(",", "")
    number = ""

    for ch in cleaned:
        if ch.isdigit():
            number += ch
        elif number:
            break

    return number if number else None


def find_area(infobox):
    labels = ["Area", "Area total", "Total area"]

    for th in infobox.find_all("th"):
        text = th.get_text(" ", strip=True)
        for label in labels:
            if text.startswith(label):
                td = th.find_next("td")
                if td:
                    return extract_number(td.get_text(" ", strip=True))
    return None


def find_population(infobox):
    labels = ["Population", "Population estimate"]

    for th in infobox.find_all("th"):
        text = th.get_text(" ", strip=True)
        for label in labels:
            if text.startswith(label):
                td = th.find_next("td")
                if td:
                    return extract_number(td.get_text(" ", strip=True))
    return None

def extract_info(html):
    soup = BeautifulSoup(html, "html.parser")
    infobox = soup.find("table", class_="infobox")

    if not infobox:
        return None, None, None

    capital = find_capital(infobox)
    area = find_area(infobox)
    population = find_population(infobox)

    return capital, area, population


def load_page(country):
    """Загрузка HTML с кешированием + user-agent."""
    filename = os.path.join(CACHE_DIR, country.replace(" ", "_") + ".html")

    # Если уже скачано — читаем из кеша
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()

    url = BASE_URL + country.replace(" ", "_")
    print(f"Загружаю страницу: {url}")

    try:
        response = requests.get(url, timeout=10, headers=HEADERS)
        response.raise_for_status()
    except Exception as e:
        print(f"Ошибка загрузки {country}: {e}")
        return None

    html = response.text

    # Сохраняем в cache
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

    time.sleep(1)
    return html

def main():
    parser = argparse.ArgumentParser(description="Wikipedia country parser")
    parser.add_argument("--input", default="countries.txt", help="Input text file")
    parser.add_argument("--output", default="countries_data.csv", help="Output CSV file")
    args = parser.parse_args()

    # Чтение стран из файла
    try:
        with open(args.input, "r", encoding="utf-8") as f:
            countries = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Ошибка: файл {args.input} не найден.")
        return

    print("Список стран:", countries)

    rows = []

    for country in countries:
        print(f"\nПарсинг: {country}")

        html = load_page(country)
        if not html:
            print(f"Пропуск страны: {country}")
            continue

        capital, area, population = extract_info(html)

        rows.append([country, capital, area, population])

    # Запись CSV
    with open(args.output, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["country", "city", "area", "population"])
        writer.writerows(rows)

    print(f"\nГотово! Результаты сохранены в {args.output}")


if __name__ == "__main__":
    main()