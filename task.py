import requests
from bs4 import BeautifulSoup
import csv
import time
import sys
import os
import argparse
from urllib.parse import quote


class WikipediaCountryParser:
    def __init__(self, cache_dir='cache'):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)

    def get_page_content(self, country_name):
        """Получает содержимое страницы с кэшированием"""
        cache_file = os.path.join(self.cache_dir, f"{country_name.replace(' ', '_')}.html")

        # Проверяем кэш
        if os.path.exists(cache_file):
            print(f"Загружаем из кэша: {country_name}")
            with open(cache_file, 'r', encoding='utf-8') as f:
                return f.read()

        # Загружаем с Википедии
        print(f"Загружаем с Википедии: {country_name}")
        url = f"https://en.wikipedia.org/wiki/{quote(country_name.replace(' ', '_'))}"

        try:
            response = self.session.get(url)
            response.raise_for_status()

            # Сохраняем в кэш
            with open(cache_file, 'w', encoding='utf-8') as f:
                f.write(response.text)

            return response.text
        except requests.RequestException as e:
            print(f"Ошибка при загрузке {country_name}: {e}")
            return None

    def parse_country_info(self, html_content, country_name):
        """Парсит информацию о стране из HTML"""
        if not html_content:
            return None

        soup = BeautifulSoup(html_content, 'lxml')

        try:
            # Ищем таблицу с информацией
            infobox = soup.find('table', {'class': 'infobox'})
            if not infobox:
                print(f"Не найдена инфобокс для {country_name}")
                return None

            # Извлекаем столицу
            capital = self.extract_capital(infobox)

            # Извлекаем площадь
            area = self.extract_area(infobox)

            # Извлекаем население
            population = self.extract_population(infobox)

            return {
                'country': country_name,
                'capital': capital,
                'area': area,
                'population': population
            }

        except Exception as e:
            print(f"Ошибка при парсинге {country_name}: {e}")
            return None

    def extract_capital(self, infobox):
        """Извлекает информацию о столице"""
        try:
            # Ищем строку с заголовком "Capital"
            rows = infobox.find_all('tr')
            for row in rows:
                th = row.find('th')
                if th and 'Capital' in th.get_text():
                    capital_link = row.find('td').find('a')
                    if capital_link:
                        return capital_link.get_text().strip()

            # Альтернативный метод поиска
            capital_th = infobox.find('th', string=lambda x: x and 'Capital' in x)
            if capital_th:
                capital_td = capital_th.find_next('td')
                if capital_td:
                    capital_link = capital_td.find('a')
                    if capital_link:
                        return capital_link.get_text().strip()

            return "N/A"
        except:
            return "N/A"

    def extract_area(self, infobox):
        """Извлекает информацию о площади"""
        try:
            # Ищем строку с заголовком "Area"
            area_th = infobox.find('th', string=lambda x: x and 'Area' in x)
            if area_th:
                area_td = area_th.find_next('td')
                if area_td:
                    area_text = area_td.get_text()
                    # Извлекаем число (убираем текст после чисел)
                    import re
                    area_match = re.search(r'(\d[\d,\.]*)', area_text.replace(',', ''))
                    if area_match:
                        return int(float(area_match.group(1)))

            return "N/A"
        except:
            return "N/A"

    def extract_population(self, infobox):
        """Извлекает информацию о населении"""
        try:
            # Ищем строку с заголовком "Population"
            pop_th = infobox.find('th', string=lambda x: x and 'Population' in x)
            if pop_th:
                pop_td = pop_th.find_next('td')
                if pop_td:
                    pop_text = pop_td.get_text()
                    # Извлекаем последнее число населения
                    import re
                    pop_matches = re.findall(r'(\d[\d,\.]*)', pop_text.replace(',', ''))
                    if pop_matches:
                        return int(float(pop_matches[-1]))

            return "N/A"
        except:
            return "N/A"

    def clean_number(self, number_str):
        """Очищает число от лишних символов"""
        if number_str == "N/A":
            return number_str
        return str(number_str).replace(',', '')


def main():
    parser = argparse.ArgumentParser(description='Парсер информации о странах с Википедии')
    parser.add_argument('--input', '-i', default='countries.txt',
                        help='Входной файл со списком стран')
    parser.add_argument('--output', '-o', default='countries_data.csv',
                        help='Выходной CSV файл')

    args = parser.parse_args()

    # Проверяем существование входного файла
    if not os.path.exists(args.input):
        print(f"Ошибка: Файл {args.input} не найден")
        sys.exit(1)

    # Читаем список стран
    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            countries = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Ошибка при чтении файла {args.input}: {e}")
        sys.exit(1)

    print(f"Найдено стран: {len(countries)}")

    # Создаем парсер
    wiki_parser = WikipediaCountryParser()

    # Собираем данные
    countries_data = []

    for i, country in enumerate(countries, 1):
        print(f"Обрабатываем {i}/{len(countries)}: {country}")

        html_content = wiki_parser.get_page_content(country)
        country_info = wiki_parser.parse_country_info(html_content, country)

        if country_info:
            countries_data.append(country_info)
            print(f"  ✓ Столица: {country_info['capital']}, "
                  f"Площадь: {country_info['area']}, "
                  f"Население: {country_info['population']}")
        else:
            print(f"  ✗ Не удалось получить данные для {country}")

        # Пауза между запросами
        if i < len(countries):
            time.sleep(1)

    # Сохраняем в CSV
    try:
        with open(args.output, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['country', 'capital', 'area', 'population']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for data in countries_data:
                writer.writerow(data)

        print(f"\nДанные сохранены в {args.output}")
        print(f"Успешно обработано: {len(countries_data)} из {len(countries)} стран")

    except Exception as e:
        print(f"Ошибка при сохранении в CSV: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

