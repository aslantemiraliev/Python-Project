def zodiac_sign(day, month):
    if not (1 <= month <= 12):
        return "Неверный месяц. Введите значение от 1 до 12."

    days_in_month = {
        1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    if not (1 <= day <= days_in_month[month]):
        return f"Неверный день. В {month}-м месяце может быть максимум {days_in_month[month]} дней."

    zodiac = [
        (20, "Козерог"), (19, "Водолей"), (20, "Рыбы"), (20, "Овен"),
        (20, "Телец"), (21, "Близнецы"), (22, "Рак"), (22, "Лев"),
        (22, "Дева"), (22, "Весы"), (21, "Скорпион"), (21, "Стрелец"), (19, "Козерог")
    ]

    if day > zodiac[month - 1][0]:
        return zodiac[month][1]
    else:
        return zodiac[month - 1][1]

try:
    day = int(input("Введите день рождения (1-31): "))
    month = int(input("Введите месяц рождения (1-12): "))

    result = zodiac_sign(day, month)
    print(result)
except ValueError:
    print("Ошибка ввода! Введите числа для дня и месяца, например, 15 и 5.")

