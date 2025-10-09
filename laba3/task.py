import json
from datetime import datetime


class Client:
    def __init__(self, client_id, name, phone, passport):
        self.client_id = client_id
        self.name = name
        self.phone = phone
        self.passport = passport
        self.accounts = {}


class BankAccount:
    def __init__(self, account_number, client, currency):
        self.account_number = account_number
        self.client = client
        self.currency = currency
        self.balance = 0.0
        self.is_active = True
        self.created_date = datetime.now()


class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = {}
        self.accounts = {}
        self.next_account_number = 3014001020001  # Типичный формат для Беларуси
        self.supported_currencies = ['BYN', 'USD', 'EUR', 'RUB', 'PLN']

    def create_client(self, name, phone, passport):
        client_id = len(self.clients) + 1
        client = Client(client_id, name, phone, passport)
        self.clients[client_id] = client
        return client

    def open_account(self, client_id, currency):
        if client_id not in self.clients:
            raise Exception("Клиент не найден")

        if currency not in self.supported_currencies:
            raise Exception(
                f"Валюта {currency} не поддерживается. Доступные валюты: {', '.join(self.supported_currencies)}")

        client = self.clients[client_id]

        if currency in client.accounts:
            raise Exception(f"У клиента уже есть счет в валюте {currency}")

        account_number = self.next_account_number
        self.next_account_number += 1

        account = BankAccount(account_number, client, currency)
        client.accounts[currency] = account
        self.accounts[account_number] = account

        return account

    def close_account(self, client_id, account_number):
        if client_id not in self.clients:
            raise Exception("Клиент не найден")

        if account_number not in self.accounts:
            raise Exception("Счет не найден")

        client = self.clients[client_id]
        account = self.accounts[account_number]

        if account.client.client_id != client_id:
            raise Exception("Этот счет не принадлежит данному клиенту")

        if account.balance > 0:
            raise Exception("Нельзя закрыть счет с положительным балансом. Сначала снимите все средства.")

        if account.balance < 0:
            raise Exception("Нельзя закрыть счет с задолженностью")

        account.is_active = False
        del client.accounts[account.currency]
        del self.accounts[account_number]

    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            raise Exception("Счет не найден")

        account = self.accounts[account_number]

        if not account.is_active:
            raise Exception("Счет закрыт")

        if amount <= 0:
            raise Exception("Сумма должна быть положительной")

        if amount > 100000:  # Лимит на крупные операции
            print("Внимание: крупная операция! Может потребоваться дополнительная проверка.")

        account.balance += amount

    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            raise Exception("Счет не найден")

        account = self.accounts[account_number]

        if not account.is_active:
            raise Exception("Счет закрыт")

        if amount <= 0:
            raise Exception("Сумма должна быть положительной")

        if amount > account.balance:
            raise Exception("Недостаточно средств на счете")

        if amount > 5000 and account.currency == 'BYN':
            print("Внимание: снятие крупной суммы в белорусских рублях")

        account.balance -= amount

    def transfer(self, from_account_number, to_account_number, amount):
        if from_account_number not in self.accounts:
            raise Exception("Счет отправителя не найден")

        if to_account_number not in self.accounts:
            raise Exception("Счет получателя не найден")

        from_account = self.accounts[from_account_number]
        to_account = self.accounts[to_account_number]

        if not from_account.is_active:
            raise Exception("Счет отправителя закрыт")

        if not to_account.is_active:
            raise Exception("Счет получателя закрыт")

        if from_account.currency != to_account.currency:
            raise Exception("Переводы между разными валютами не поддерживаются")

        if amount <= 0:
            raise Exception("Сумма должна быть положительной")

        if amount > from_account.balance:
            raise Exception("Недостаточно средств на счете отправителя")

        # Проверка на крупный перевод
        if amount > 20000:
            print("Внимание: крупный денежный перевод")

        from_account.balance -= amount
        to_account.balance += amount

    def get_client_accounts(self, client_id):
        if client_id not in self.clients:
            raise Exception("Клиент не найден")

        return self.clients[client_id].accounts

    def calculate_total_balance(self, client_id):
        """Рассчитать общий баланс по всем счетам в BYN"""
        if client_id not in self.clients:
            raise Exception("Клиент не найден")

        client = self.clients[client_id]
        total_byn = 0

        # Простые курсы для демонстрации (в реальной системе брать из API НБРБ)
        exchange_rates = {
            'BYN': 1.0,
            'USD': 3.2,
            'EUR': 3.4,
            'RUB': 0.035,
            'PLN': 0.8
        }

        for currency, account in client.accounts.items():
            if account.is_active:
                total_byn += account.balance * exchange_rates[currency]

        return total_byn

    def generate_statement(self, client_id, filename=None):
        if client_id not in self.clients:
            raise Exception("Клиент не найден")

        client = self.clients[client_id]

        if filename is None:
            filename = f"выписка_{client.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

        total_byn = self.calculate_total_balance(client_id)

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"БАНК: {self.name}\n")
            file.write(f"ВЫПИСКА ПО СЧЕТАМ КЛИЕНТА\n")
            file.write("=" * 50 + "\n")
            file.write(f"Клиент: {client.name}\n")
            file.write(f"ID клиента: {client.client_id}\n")
            file.write(f"Паспорт: {client.passport}\n")
            file.write(f"Телефон: {client.phone}\n")
            file.write(f"Дата формирования: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}\n")
            file.write("=" * 50 + "\n\n")

            file.write("СПИСОК СЧЕТОВ:\n")
            file.write("-" * 50 + "\n")

            has_active_accounts = False
            for currency, account in client.accounts.items():
                if account.is_active:
                    has_active_accounts = True
                    file.write(f"Номер счета: {account.account_number}\n")
                    file.write(f"Валюта: {currency}\n")
                    file.write(f"Баланс: {account.balance:,.2f} {currency}\n")
                    file.write(f"Дата открытия: {account.created_date.strftime('%d.%m.%Y')}\n")
                    file.write(f"Статус: {'Активен' if account.is_active else 'Закрыт'}\n")
                    file.write("-" * 30 + "\n")

            if not has_active_accounts:
                file.write("Нет активных счетов\n")

            file.write("\n" + "=" * 50 + "\n")
            file.write(f"ОБЩИЙ БАЛАНС (в BYN): {total_byn:,.2f} BYN\n")
            file.write("=" * 50 + "\n")
            file.write(f"\nСформировано: {datetime.now().strftime('%d.%m.%Y %H:%M')}\n")

        return filename


def main():
    # Создаем банк для Беларуси
    bank = Bank("Банк")

    # Создаем тестовых клиентов с белорусскими данными
    client1 = bank.create_client("Иванов Иван Иванович", "+375291234567", "МР1234567")
    client2 = bank.create_client("Петрова Мария Сергеевна", "+375337654321", "МР7654321")
    client3 = bank.create_client("Ковалевский Александр Петрович", "+375445551122", "МР1122334")

    # Открываем счета для тестовых клиентов
    try:
        # Первый клиент - BYN и USD
        bank.open_account(1, "BYN")
        bank.open_account(1, "USD")

        # Второй клиент - BYN и EUR
        bank.open_account(2, "BYN")
        bank.open_account(2, "EUR")

        # Третий клиент - BYN, USD, RUB
        bank.open_account(3, "BYN")
        bank.open_account(3, "USD")
        bank.open_account(3, "RUB")

        # Пополняем счета для демонстрации
        bank.deposit(3014001020001, 1500.50)  # BYN
        bank.deposit(3014001020002, 250.00)  # USD
        bank.deposit(3014001020003, 2750.00)  # BYN
        bank.deposit(3014001020004, 150.00)  # EUR
        bank.deposit(3014001020005, 3200.75)  # BYN
        bank.deposit(3014001020006, 500.00)  # USD
        bank.deposit(3014001020007, 10000.00)  # RUB

    except Exception as e:
        print(f"Ошибка при создании тестовых данных: {e}")

    current_client = None

    while True:
        print("        БАНКОВСКАЯ СИСТЕМА ")

        if current_client is None:
            print("1. Войти в систему")
            print("2. Зарегистрировать нового клиента")
            print("3. Выход")
        else:
            print(f"Добро пожаловать, {current_client.name}!")
            print("1. Открыть счет")
            print("2. Закрыть счет")
            print("3. Пополнить счет")
            print("4. Снять деньги")
            print("5. Перевести деньги")
            print("6. Показать мои счета")
            print("7. Выписка по счетам")
            print("8. Общий баланс (в BYN)")
            print("9. Выйти из системы")

        choice = input("Выберите действие: ")

        if current_client is None:
            if choice == "1":
                try:
                    client_id = int(input("Введите ваш ID клиента: "))
                    if client_id in bank.clients:
                        current_client = bank.clients[client_id]
                        print(f"Успешный вход! Добро пожаловать, {current_client.name}!")
                    else:
                        print("Клиент с таким ID не найден!")
                except ValueError:
                    print("Некорректный ID!")

            elif choice == "2":
                print("\nРегистрация нового клиента:")
                name = input("ФИО: ")
                phone = input("Номер телефона (+375...): ")
                passport = input("Номер паспорта (HB1...): ")

                if name and phone and passport:
                    client = bank.create_client(name, phone, passport)
                    print(f"Клиент успешно зарегистрирован! Ваш ID: {client.client_id}")
                    # Автоматически открываем счет в BYN
                    try:
                        account = bank.open_account(client.client_id, "BYN")
                        print(f"Открыт основной счет в BYN: {account.account_number}")
                    except Exception as e:
                        print(f"Ошибка при открытии счета: {e}")
                else:
                    print("Все поля обязательны для заполнения!")

            elif choice == "3":
                print("Дзякуй! Да пабачэння!")
                break

            else:
                print("Некорректный выбор!")

        else:
            if choice == "1":
                print(f"\nДоступные валюты: {', '.join(bank.supported_currencies)}")
                currency = input("Введите валюту счета: ").upper()
                try:
                    account = bank.open_account(current_client.client_id, currency)
                    print(f"Счет успешно открыт! Номер счета: {account.account_number}")
                except Exception as e:
                    print(f"Ошибка: {e}")

            elif choice == "2":
                try:
                    account_number = int(input("Введите номер счета для закрытия: "))
                    bank.close_account(current_client.client_id, account_number)
                    print("Счет успешно закрыт!")
                except Exception as e:
                    print(f"Ошибка: {e}")
                except ValueError:
                    print("Некорректный номер счета!")

            elif choice == "3":
                try:
                    account_number = int(input("Введите номер счета: "))
                    amount = float(input("Введите сумму для пополнения: "))
                    bank.deposit(account_number, amount)
                    print("Счет успешно пополнен!")
                except Exception as e:
                    print(f"Ошибка: {e}")
                except ValueError:
                    print("Некорректные данные!")

            elif choice == "4":
                try:
                    account_number = int(input("Введите номер счета: "))
                    amount = float(input("Введите сумму для снятия: "))
                    bank.withdraw(account_number, amount)
                    print("Снятие успешно выполнено!")
                except Exception as e:
                    print(f"Ошибка: {e}")
                except ValueError:
                    print("Некорректные данные!")

            elif choice == "5":
                try:
                    from_account = int(input("Введите номер счета отправителя: "))
                    to_account = int(input("Введите номер счета получателя: "))
                    amount = float(input("Введите сумму для перевода: "))
                    bank.transfer(from_account, to_account, amount)
                    print("Перевод успешно выполнен!")
                except Exception as e:
                    print(f"Ошибка: {e}")
                except ValueError:
                    print("Некорректные данные!")

            elif choice == "6":
                accounts = bank.get_client_accounts(current_client.client_id)
                if accounts:
                    print("\nВаши счета:")
                    for currency, account in accounts.items():
                        status = "Активен" if account.is_active else "Закрыт"
                        print(f"  Счет №{account.account_number}")
                        print(f"    Валюта: {currency}")
                        print(f"    Баланс: {account.balance:,.2f} {currency}")
                        print(f"    Статус: {status}")
                        print()
                else:
                    print("У вас нет открытых счетов.")

            elif choice == "7":
                try:
                    filename = bank.generate_statement(current_client.client_id)
                    print(f"Выписка сохранена в файл: {filename}")
                except Exception as e:
                    print(f"Ошибка: {e}")

            elif choice == "8":
                try:
                    total_balance = bank.calculate_total_balance(current_client.client_id)
                    print(f"Общий баланс по всем счетам: {total_balance:,.2f} BYN")
                except Exception as e:
                    print(f"Ошибка: {e}")

            elif choice == "9":
                current_client = None
                print("Вы вышли из системы.")

            else:
                print("Некорректный выбор!")


if __name__ == "__main__":
    main()
