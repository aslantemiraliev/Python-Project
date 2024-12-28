import sqlite3


def create_tables():
    # Подключение к базе данных
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    # Создаем таблицу stores, если она еще не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    # Добавляем несколько магазинов
    cursor.executemany('''
        INSERT INTO stores (name) VALUES (?)
    ''', [
        ('Asia',),
        ('Globus',),
        ('Spar',)
    ])

    # Сохраняем изменения и закрываем соединение
    conn.commit()
    conn.close()


# Создание таблиц и добавление магазинов
create_tables()

import sqlite3


def main():
    # Подключаемся к базе данных
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    while True:
        # Выводим фразу
        print(
            "\nВы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")

        # Получаем список магазинов из базы данных
        cursor.execute("SELECT id, name FROM stores")
        stores = cursor.fetchall()

        # Отображаем список магазинов
        for store in stores:
            print(f"{store[0]}. {store[1]}")

        # Запрос у пользователя id магазина
        store_id = input("Введите id магазина: ")

        # Если введено 0, выходим из программы
        if store_id == '0':
            print("Выход из программы.")
            break

        # Проверка на корректность ввода
        if not store_id.isdigit() or int(store_id) not in [store[0] for store in stores]:
            print("Некорректный id магазина. Попробуйте снова.")
            continue

        # Запрос продуктов из выбранного магазина
        store_id = int(store_id)
        cursor.execute("""
            SELECT products.name, categories.name, products.price, products.stock
            FROM products
            JOIN categories ON products.category_id = categories.id
            WHERE products.store_id = ?
        """, (store_id,))

        # Получаем все продукты из выбранного магазина
        products = cursor.fetchall()

        # Если продукты найдены, отображаем информацию
        if products:
            print("\nПродукты в выбранном магазине:")
            for product in products:
                print(f"Название продукта: {product[0]}")
                print(f"Категория: {product[1]}")
                print(f"Цена: {product[2]}")
                print(f"Количество на складе: {product[3]}")
                print("-" * 30)
        else:
            print("В данном магазине нет продуктов.")

    # Закрываем соединение с базой данных
    conn.close()


if __name__ == "__main__":
    main()
