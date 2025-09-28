import random


secret_number = random.randint(1, 100)
attempts = 0

print("Я загадал число от 1 до 100. Попробуй угадать!")


while True:

    guess_input = input("Твоя догадка: ")


    if guess_input.isdigit():
        guess = int(guess_input)
        attempts += 1


        if guess == secret_number:
            print(f"Поздравляю! Ты угадал число {secret_number} за {attempts} попыток!")
            break
        elif guess < secret_number:
            print("Больше!")
        else:
            print("Меньше!")
    else:
        print("Пожалуйста, введите число!")