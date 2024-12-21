def bubble_sort(unsorted_list):
    """
    Сортировка списка методом пузырьковой сортировки.
    """
    n = len(unsorted_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                # Обмен элементов
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
    return unsorted_list


def binary_search(target, sorted_list):
    """
    Поиск элемента в списке методом двоичного поиска.
    """
    low, high = 0, len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            print(f"Элемент {target} найден на позиции {mid}.")
            return
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    print(f"Элемент {target} не найден в списке.")


# Пример использования
if __name__ == "__main__":
    # Пример списка для сортировки
    unsorted_list = [34, 7, 23, 32, 5, 62]
    print("Неотсортированный список:", unsorted_list)

    # Применяем bubble_sort
    sorted_list = bubble_sort(unsorted_list)
    print("Отсортированный список:", sorted_list)

    # Пример элемента для поиска
    target = 23

    # Применяем binary_search
    binary_search(target, sorted_list)
