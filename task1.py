import random
import datetime
from collections import defaultdict


# Генератор случайных данных
class DataGenerator:
    def __init__(self):
        self.first_names = [
            "Александр", "Михаил", "Дмитрий", "Андрей", "Сергей", "Алексей",
            "Екатерина", "Мария", "Анна", "Ольга", "Наталья", "Ирина"
        ]
        self.last_names = [
            "Иванов", "Петров", "Сидоров", "Кузнецов", "Попов", "Васильев",
            "Смирнова", "Козлова", "Новикова", "Морозова", "Волкова"
        ]
        self.middle_names = [
            "Александрович", "Сергеевич", "Дмитриевич", "Андреевич", "Михайлович",
            "Александровна", "Сергеевна", "Дмитриевна", "Андреевна", "Михайловна"
        ]

        self.subjects = ["Математика", "Русский язык", "Физика", "Химия", "Биология", "История"]
        self.specialties = [
            "Информатика", "Экономика", "Медицина", "Юриспруденция",
            "Строительство", "Психология", "Филология"
        ]
        self.education_forms = ["Бюджет", "Платная", "Целевая"]

        self.cities = ["Минск", "Гомель", "Витебск", "Могилев", "Гродно", "Брест"]
        self.streets = ["Ленина", "Советская", "Победы", "Мира", "Молодежная", "Центральная"]

    def generate_name(self):
        first = random.choice(self.first_names)
        last = random.choice(self.last_names)
        middle = random.choice(self.middle_names)
        return f"{last} {first} {middle}"

    def generate_phone(self):
        return f"+37529{random.randint(1000000, 9999999)}"

    def generate_address(self):
        city = random.choice(self.cities)
        street = random.choice(self.streets)
        house = random.randint(1, 100)
        return f"{city}, ул. {street}, д. {house}"

    def generate_ct_scores(self):
        scores = {}
        num_subjects = random.randint(2, 3)
        selected_subjects = random.sample(self.subjects, num_subjects)

        for subject in selected_subjects:
            scores[subject] = random.randint(45, 100)
        return scores

    def generate_student(self, year):
        ct_scores = self.generate_ct_scores()
        certificate_score = round(random.uniform(6.0, 9.9), 1)

        # Общий балл - среднее ЦТ + балл аттестата
        avg_ct = sum(ct_scores.values()) / len(ct_scores)
        total_score = round(avg_ct + certificate_score, 1)

        return {
            'fio': self.generate_name(),
            'year': year,
            'form': random.choice(self.education_forms),
            'ct_scores': ct_scores,
            'certificate': certificate_score,
            'total_score': total_score,
            'specialty': random.choice(self.specialties),
            'address': self.generate_address(),
            'phone': self.generate_phone()
        }


# Анализ данных
class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def calculate_subject_dynamics(self):
        subject_years = defaultdict(lambda: defaultdict(list))

        for student in self.data:
            year = student['year']
            for subject, score in student['ct_scores'].items():
                subject_years[subject][year].append(score)

        result = {}
        for subject, years_data in subject_years.items():
            result[subject] = {}
            for year, scores in sorted(years_data.items()):
                result[subject][year] = sum(scores) / len(scores)
        return result

    def calculate_certificate_dynamics(self):
        year_certificates = defaultdict(list)

        for student in self.data:
            year_certificates[student['year']].append(student['certificate'])

        result = {}
        for year, scores in sorted(year_certificates.items()):
            result[year] = sum(scores) / len(scores)
        return result

    def calculate_passing_scores(self):
        specialty_years = defaultdict(lambda: defaultdict(list))

        for student in self.data:
            specialty_years[student['specialty']][student['year']].append(student['total_score'])

        result = {}
        for specialty, years_data in specialty_years.items():
            result[specialty] = {}
            for year, scores in sorted(years_data.items()):
                result[specialty][year] = min(scores)  # Проходной балл - минимальный
        return result

    def count_by_specialty(self):
        specialty_count = defaultdict(int)
        for student in self.data:
            specialty_count[student['specialty']] += 1
        return dict(specialty_count)

    def count_by_education_form(self):
        form_count = defaultdict(int)
        for student in self.data:
            form_count[student['form']] += 1
        return dict(form_count)


# Визуализация ASCII графиков
class ASCIIVisualizer:
    @staticmethod
    def print_line_chart(title, data, width=50):
        print(f"\n{title}")
        print("=" * 60)

        if isinstance(list(data.values())[0], dict):
            # Для вложенных данных (по предметам/специальностям)
            years = sorted(set(year for subj_data in data.values() for year in subj_data.keys()))
            subjects = list(data.keys())

            # Заголовок
            header = "Год    " + "".join(f"{subj[:8]:>10}" for subj in subjects)
            print(header)
            print("-" * len(header))

            for year in years:
                row = f"{year}    "
                for subject in subjects:
                    if year in data[subject]:
                        value = data[subject][year]
                        row += f"{value:>10.1f}"
                    else:
                        row += " " * 10
                print(row)
        else:
            # Для простых данных
            max_val = max(data.values())
            min_val = min(data.values())

            for key, value in sorted(data.items()):
                bar_length = int((value - min_val) / (max_val - min_val) * width) if max_val != min_val else width
                bar = "█" * bar_length
                print(f"{key}: {value:.1f} {bar}")

    @staticmethod
    def print_bar_chart(title, data, width=50):
        print(f"\n{title}")
        print("=" * 60)

        max_val = max(data.values())

        for key, value in sorted(data.items(), key=lambda x: x[1], reverse=True):
            bar_length = int(value / max_val * width)
            bar = "█" * bar_length
            print(f"{key:<15}: {value:>3} {bar}")

    @staticmethod
    def print_pie_chart(title, data):
        print(f"\n{title}")
        print("=" * 60)

        total = sum(data.values())

        for key, value in sorted(data.items(), key=lambda x: x[1], reverse=True):
            percentage = (value / total) * 100
            print(f"{key}: {value} ({percentage:.1f}%)")

        # Простая ASCII диаграмма
        print("\nДиаграмма:")
        symbols = ["▓", "▒", "░", "▄", "▀", "■"]
        for i, (key, value) in enumerate(sorted(data.items(), key=lambda x: x[1], reverse=True)):
            if i < len(symbols):
                percentage = (value / total) * 100
                bar = symbols[i] * int(percentage / 5)
                print(f"{bar} {key}")


# Основная программа
def main():
    # Генерация данных
    print("Генерация данных о вступительной кампании...")
    generator = DataGenerator()

    data = []
    current_year = datetime.datetime.now().year
    for year in range(current_year - 5, current_year):
        for _ in range(100):  # по 100 студентов в год
            data.append(generator.generate_student(year))

    print(f"Сгенерировано {len(data)} записей за период {current_year - 5}-{current_year - 1} гг.")

    # Анализ данных
    analyzer = DataAnalyzer(data)
    visualizer = ASCIIVisualizer()

    # 1. Динамика среднего балла ЦТ по предметам
    subject_dynamics = analyzer.calculate_subject_dynamics()
    visualizer.print_line_chart("ДИНАМИКА СРЕДНЕГО БАЛЛА ЦТ ПО ПРЕДМЕТАМ", subject_dynamics)

    # 2. Динамика среднего балла аттестата
    certificate_dynamics = analyzer.calculate_certificate_dynamics()
    visualizer.print_line_chart("ДИНАМИКА СРЕДНЕГО БАЛЛА АТТЕСТАТА", certificate_dynamics)

    # 3. Динамика проходного балла
    passing_scores = analyzer.calculate_passing_scores()
    visualizer.print_line_chart("ДИНАМИКА ПРОХОДНОГО БАЛЛА ПО СПЕЦИАЛЬНОСТЯМ", passing_scores)

    # 4. Количество поступивших по специальностям
    specialty_counts = analyzer.count_by_specialty()
    visualizer.print_bar_chart("КОЛИЧЕСТВО ПОСТУПИВШИХ ПО СПЕЦИАЛЬНОСТЯМ", specialty_counts)

    # 5. Статистика по формам обучения
    form_counts = analyzer.count_by_education_form()
    visualizer.print_pie_chart("РАСПРЕДЕЛЕНИЕ ПО ФОРМАМ ОБУЧЕНИЯ", form_counts)

    # Дополнительная статистика
    print("\n" + "=" * 60)
    print("ОБЩАЯ СТАТИСТИКА")
    print("=" * 60)

    total_students = len(data)
    avg_total_score = sum(student['total_score'] for student in data) / total_students
    avg_certificate = sum(student['certificate'] for student in data) / total_students

    print(f"Общее количество студентов: {total_students}")
    print(f"Средний общий балл: {avg_total_score:.1f}")
    print(f"Средний балл аттестата: {avg_certificate:.1f}")
    print(f"Количество специальностей: {len(specialty_counts)}")

    # Статистика по годам
    print("\nСТАТИСТИКА ПО ГОДАМ:")
    print("-" * 40)
    years = sorted(set(student['year'] for student in data))
    for year in years:
        year_students = [s for s in data if s['year'] == year]
        year_avg_score = sum(s['total_score'] for s in year_students) / len(year_students)
        print(f"{year} год: {len(year_students)} студентов, средний балл: {year_avg_score:.1f}")


if __name__ == "__main__":
    main()