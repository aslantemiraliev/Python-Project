
def guess_number():
    import os

    print("Загадайте число от 1 до 100, и я попробую его угадать.")
    print('Отвечайте "да", "больше" или "меньше" на мои предположения.')

    # Диапазон поиска
    low, high = 1, 100
    attempts = []
    attempts_count = 0

    while True:
        # Генерация предположения
        guess = (low + high) // 2
        attempts.append(guess)
        attempts_count += 1

        # Вывод предположения
        print(f"Мое предположение: {guess}")
        user_response = input('Ваш ответ ("да", "больше", "меньше"): ').strip().lower()

        # Обработка ответа
        if user_response == "да":
            print(f"Ура! Я угадал число {guess} за {attempts_count} попыток.")

            # Запись результатов в файл
            with open("../results.txt", "a") as file:
                file.write(
                    f"Загаданное число: {guess}\n"
                    f"Количество попыток: {attempts_count}\n"
                    f"Список попыток: {attempts}\n"
                    f"{'-' * 20}\n"
                )
            break
        elif user_response == "больше":
            low = guess + 1
        elif user_response == "меньше":
            high = guess - 1
        else:
            print('Пожалуйста, ответьте "да", "больше" или "меньше".')

        # Проверка на случай некорректных ответов
        if low > high:
            print("Похоже, произошла ошибка. Проверьте свои ответы!")
            break


# Запуск программы
guess_number()
