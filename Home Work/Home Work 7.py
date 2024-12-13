def nearest_number_and_sorted(numbers, target):
    # Проверка на пустой список
    if not numbers:
        raise ValueError("Список не может быть пустым.")

    # Сортировка по расстоянию до целевого числа
    sorted_numbers = sorted(numbers, key=lambda x: abs(x - target))
    # Ближайшее число — первый элемент отсортированного списка
    closest_number = sorted_numbers[0]

    return closest_number, sorted_numbers


# Пример использования
numbers = [10, 20, 30, 25, 5]
target = 23
result = nearest_number_and_sorted(numbers, target)
print(result)  # (25, [25, 20, 30, 10, 5])
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6]
def element_by_index(iterable=[1, 2, 3, 4, 5]):
    while True:
        try:
            # Запрос индекса у пользователя
            index = int(input(f"Введите индекс элемента (от 0 до {len(iterable) - 1}): "))
            # Вывод элемента по индексу
            print(f"Элемент с индексом {index}: {iterable[index]}")
        except IndexError:
            print(f"Ошибка: допустимые индексы от 0 до {len(iterable) - 1}.")
        except ValueError:
            print("Ошибка: введите целое число.")
        except KeyboardInterrupt:
            print("\nВыход из программы.")
            break

# Пример использования
element_by_index(["a", "b", "c", "d", "e"])
