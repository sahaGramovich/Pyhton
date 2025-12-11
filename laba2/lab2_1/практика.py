import json
import os

class Student :
    def __init__(self, name, math_score, physics_score, language_score, status, desired_university):
        self.name = name
        self.math_score = math_score
        self.physics_score = physics_score
        self.language_score = language_score
        self.status = status
        self.desired_university = desired_university

    def to_dict(self):
            return {
                'name': self.name,
                'math_score': self.math_score,
                'physics_score': self.physics_score,
                'language_score': self.language_score,
                'status': self.status,
                'desired_university': self.desired_university
            }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['name'],
            data['math_score'],
            data['physics_score'],
            data['language_score'],
            data['status'],
            data['desired_university']
        )

    def __str__(self):
        return (f"Абитуриент: {self.name}\n"
                f"Баллы: математика={self.math_score}, физика={self.physics_score}, язык={self.language_score}\n"
                f"Статус: {self.status}\n"
                f"Желаемый ВУЗ: {self.desired_university}\n")

    class StudentManager:
        def __init__(self, filename='applicants.json'):
            self.filename = filename
            self.applicants = []
            self.load_from_file()

        def load_from_file(self):

            if os.path.exists(self.filename):
                try:
                    with open(self.filename, 'r', encoding='utf-8') as file:
                        data = json.load(file)
                        self.applicants = [Student .from_dict(item) for item in data]
                    print(f"Данные загружены из {self.filename}")
                except Exception as e:
                    print(f"Ошибка при загрузке файла: {e}")
                    self.applicants = []
            else:
                print("файл не найден, создан новый список абитуриентов")
                self.applicants = []
