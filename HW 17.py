import sqlite3

# Подключение к базе данных (если файла базы данных не существует, он будет создан)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# SQL-запрос для создания таблицы countries
create_countries_table_query = """
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Первичный ключ с автоинкрементом
    title TEXT NOT NULL                   -- Название страны (обязательно)
);
"""

# Выполнение запроса
cursor.execute(create_countries_table_query)

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

print("Таблица 'countries' успешно создана.")

import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# SQL-запрос для вставки данных
insert_countries_query = """
INSERT INTO countries (title) VALUES
    ('Кыргызстан'),
    ('Германия'),
    ('Китай');
"""

# Выполнение запроса
cursor.execute(insert_countries_query)

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

print("3 записи успешно добавлены в таблицу 'countries'.")

import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# SQL-запрос для создания таблицы cities
create_cities_table_query = """
CREATE TABLE IF NOT EXISTS cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Первичный ключ с автоинкрементом
    title TEXT NOT NULL,                  -- Название города (обязательно)
    area REAL DEFAULT 0,                  -- Площадь города (по умолчанию 0)
    country_id INTEGER,                   -- Внешний ключ на таблицу countries
    FOREIGN KEY (country_id) REFERENCES countries (id)
);
"""

# Выполнение запроса
cursor.execute(create_cities_table_query)

# Сохранение изменений
conn.commit()

print("Таблица 'cities' успешно создана.")

# SQL-запрос для вставки данных в таблицу cities
insert_cities_query = """
INSERT INTO cities (title, area, country_id) VALUES
    ('Бишкек', 127.0, 1), -- Кыргызстан
    ('Ош', 182.0, 1),     -- Кыргызстан
    ('Берлин', 891.7, 2), -- Германия
    ('Мюнхен', 310.7, 2), -- Германия
    ('Пекин', 16410.54, 3), -- Китай
    ('Шанхай', 6340.5, 3),  -- Китай
    ('Гуанчжоу', 7434.4, 3); -- Китай
"""

# Выполнение запроса
cursor.execute(insert_cities_query)

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

print("7 городов успешно добавлены в таблицу 'cities'.")

import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# SQL-запрос для создания таблицы students
create_students_table_query = """
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Первичный ключ с автоинкрементом
    first_name TEXT NOT NULL,             -- Имя ученика (обязательно)
    last_name TEXT NOT NULL,              -- Фамилия ученика (обязательно)
    city_id INTEGER,                      -- Внешний ключ на таблицу cities
    FOREIGN KEY (city_id) REFERENCES cities (id)
);
"""

# Выполнение запроса
cursor.execute(create_students_table_query)

# Сохранение изменений
conn.commit()

print("Таблица 'students' успешно создана.")

# SQL-запрос для вставки данных в таблицу students
insert_students_query = """
INSERT INTO students (first_name, last_name, city_id) VALUES
    ('Айбек', 'Тилеков', 1),    -- Бишкек
    ('Салтанат', 'Мусаева', 2), -- Ош
    ('Ганс', 'Шмидт', 3),       -- Берлин
    ('Лукас', 'Мюллер', 4),     -- Мюнхен
    ('Ли', 'Вэй', 5),           -- Пекин
    ('Ван', 'Фан', 6),          -- Шанхай
    ('Чжан', 'Лэй', 7),         -- Гуанчжоу
    ('Максат', 'Токтомамбетов', 1), -- Бишкек
    ('Нурлан', 'Абдраимов', 2),     -- Ош
    ('Эмма', 'Шульц', 3),           -- Берлин
    ('София', 'Кляйн', 4),          -- Мюнхен
    ('Фэн', 'Мин', 5),              -- Пекин
    ('Лю', 'Хао', 6),               -- Шанхай
    ('Хуан', 'Юн', 7),              -- Гуанчжоу
    ('Эркин', 'Курбанов', 1);       -- Бишкек
"""

# Выполнение запроса
cursor.execute(insert_students_query)

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

print("15 учеников успешно добавлены в таблицу 'students'.")

import sqlite3


def main():
    # Подключение к базе данных
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    while True:
        # Вывод приветственного сообщения
        print(
            "Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")

        # Запрос списка городов
        cursor.execute("SELECT id, title FROM cities")
        cities = cursor.fetchall()

        # Отображение списка городов
        for city in cities:
            print(f"{city[0]}. {city[1]}")

        # Запрос id города у пользователя
        city_id = input("Введите id города: ")
        if city_id == '0':
            print("Выход из программы.")
            break

        # Проверка на корректность ввода
        if not city_id.isdigit() or int(city_id) not in [city[0] for city in cities]:
            print("Некорректный id города. Попробуйте снова.")
            continue

        # Вывод информации о выбранном городе
        print(f"Вы выбрали город с id: {city_id}")
        print("Программа пока что только отображает список городов.\n")

    # Закрытие соединения
    conn.close()


if __name__ == "__main__":
    main()
import sqlite3


def main():
    # Подключение к базе данных
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    while True:
        # Вывод приветственного сообщения
        print(
            "Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")

        # Запрос списка городов
        cursor.execute("""
             SELECT cities.id, cities.title, countries.title, cities.area
             FROM cities
             JOIN countries ON cities.country_id = countries.id
         """)
        cities = cursor.fetchall()

        # Отображение списка городов
        for city in cities:
            print(f"{city[0]}. {city[1]}")

        # Запрос id города у пользователя
        city_id = input("Введите id города: ")
        if city_id == '0':
            print("Выход из программы.")
            break

        # Проверка на корректность ввода
        if not city_id.isdigit() or int(city_id) not in [city[0] for city in cities]:
            print("Некорректный id города. Попробуйте снова.")
            continue

        # Запрос информации об учениках из выбранного города
        city_id = int(city_id)
        cursor.execute("""
             SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
             FROM students
             JOIN cities ON students.city_id = cities.id
             JOIN countries ON cities.country_id = countries.id
             WHERE cities.id = ?
         """, (city_id,))
        students = cursor.fetchall()

        # Если ученики найдены, отображаем информацию
        if students:
            print("\nУченики из выбранного города:")
            for student in students:
                print(
                    f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, Город: {student[3]}, Площадь: {student[4]}")
        else:
            print("В данном городе нет учеников.")
        print()

    # Закрытие соединения
    conn.close()


if __name__ == "__main__":
    main()
