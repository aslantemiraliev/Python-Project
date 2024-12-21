def bubble_sort(input_list):
    """
    Сортировка списка методом пузырьковой сортировки.
    """
    n = len(input_list)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if input_list[j] > input_list[j + 1]:
                # Меняем элементы местами
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
    return input_list

def selection_sort(input_list):
    """
    Сортировка списка методом сортировки выбором.
    """
    n = len(input_list)
    for i in range(n):
        # Находим минимальный элемент в оставшейся части списка
        min_index = i
        for j in range(i + 1, n):
            if input_list[j] < input_list[min_index]:
                min_index = j
        # Меняем местами текущий элемент и минимальный
        input_list[i], input_list[min_index] = input_list[min_index], input_list[i]
    return input_list

def binary_search(target, sorted_list):
    """
    Бинарный поиск элемента в отсортированном списке.
    """
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            print(f"Элемент {target} найден на позиции {mid}.")
            return
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print(f"Элемент {target} не найден.")

# Пример использования
unsorted_list = [64, 34, 25, 12, 22, 11, 90]

# Сортировка списка (можно использовать bubble_sort или selection_sort)
sorted_list = bubble_sort(unsorted_list.copy())
print("Отсортированный список (bubble_sort):", sorted_list)

# Или используйте selection_sort:
sorted_list_selection = selection_sort(unsorted_list.copy())
print("Отсортированный список (selection_sort):", sorted_list_selection)

# Бинарный поиск элемента в отсортированном списке
element_to_find = 25
binary_search(element_to_find, sorted_list)
