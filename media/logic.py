import random


def play_game(starting_capital, attempts, number_range):
    secret_number = random.randint(1, number_range)
    capital = starting_capital

    print(f"Добро пожаловать в игру 'Угадай число'! У вас {attempts} попыток и начальный капитал: {starting_capital}.")

    for attempt in range(1, attempts + 1):
        print(f"\nПопытка {attempt} из {attempts}")
        print(f"Ваш текущий капитал: {capital}")

        try:
            bet = int(input("Введите ставку: "))
            if bet <= 0 or bet > capital:
                print("Ставка должна быть положительной и не превышать ваш текущий капитал.")
                continue
        except ValueError:
            print("Пожалуйста, введите корректное число для ставки.")
            continue

        try:
            guess = int(input(f"Угадайте число от 1 до {number_range}: "))
        except ValueError:
            print("Пожалуйста, введите корректное число для угадывания.")
            continue

        if guess < 1 or guess > number_range:
            print(f"Число должно быть в диапазоне от 1 до {number_range}.")
            continue

        if guess == secret_number:
            capital += bet
            print(f"Поздравляем! Вы угадали число {secret_number}. Ваш выигрыш составил {bet}, и теперь ваш капитал: {capital}")
            break
        else:
            capital -= bet
            print(f"Неправильно! Загаданное число {('меньше' if guess > secret_number else 'больше')} {guess}. Вы потеряли {bet}. Остаток капитала: {capital}")

        if capital <= 0:
            print("Ваш капитал закончился. Игра окончена.")
            break

    else:
        print(f"Игра окончена! Загаданное число было: {secret_number}")
    return capital
