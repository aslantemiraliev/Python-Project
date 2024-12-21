from decouple import config
from .logic import play_game

if __name__ == "__main__":
    try:
        number_range = config('NUMBER_RANGE', cast=int)
        attempts = config('ATTEMPTS', cast=int)
        starting_capital = config('STARTING_CAPITAL', cast=int)
    except Exception as e:
        print("Ошибка при чтении конфигурации. Убедитесь, что файл settings.ini заполнен правильно.", e)
        exit(1)

    final_capital = play_game(starting_capital, attempts, number_range)
    print(f"Спасибо за игру! Ваш итоговый капитал: {final_capital}")
