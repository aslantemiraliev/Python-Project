import sqlite3

def create_database():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_title TEXT NOT NULL CHECK(LENGTH(product_title) <= 200),
            price REAL NOT NULL DEFAULT 0.0,
            quantity INTEGER NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def add_products():
    products = [
        ("Мыло", 50.0, 10),
        ("Шампунь", 120.0, 5),
        ("Гель для душа", 90.0, 8),
        ("Крем для рук", 200.0, 2),
        ("Зубная паста", 80.0, 20),
        ("Мочалка", 40.0, 15),
        ("Дезодорант", 150.0, 7),
        ("Лосьон", 300.0, 3),
        ("Туалетная бумага", 20.0, 50),
        ("Бритвенный станок", 100.0, 12),
        ("Косметичка", 250.0, 4),
        ("Расческа", 60.0, 25),
        ("Губка для обуви", 30.0, 18),
        ("Салфетки", 15.0, 100),
        ("Полотенце", 400.0, 6)
    ]
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT INTO products (product_title, price, quantity) 
        VALUES (?, ?, ?)
    ''', products)
    conn.commit()
    conn.close()

def update_quantity(product_id, new_quantity):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE products
        SET quantity = ?
        WHERE id = ?
    ''', (new_quantity, product_id))
    conn.commit()
    conn.close()

def update_price(product_id, new_price):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE products
        SET price = ?
        WHERE id = ?
    ''', (new_price, product_id))
    conn.commit()
    conn.close()

def delete_product(product_id):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM products
        WHERE id = ?
    ''', (product_id,))
    conn.commit()
    conn.close()

def fetch_all_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    for product in products:
        print(product)

def fetch_products_by_limit(price_limit, quantity_limit):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM products
        WHERE price < ? AND quantity > ?
    ''', (price_limit, quantity_limit))
    products = cursor.fetchall()
    conn.close()
    for product in products:
        print(product)

def search_products_by_name(keyword):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM products
        WHERE product_title LIKE ?
    ''', (f"%{keyword}%",))
    products = cursor.fetchall()
    conn.close()
    for product in products:
        print(product)

def main():
    create_database()
    add_products()

    print("Все товары:")
    fetch_all_products()

    print("\nИзменяем количество товара с ID 1 на 50:")
    update_quantity(1, 50)
    fetch_all_products()

    print("\nИзменяем цену товара с ID 2 на 99.99:")
    update_price(2, 99.99)
    fetch_all_products()

    print("\nУдаляем товар с ID 3:")
    delete_product(3)
    fetch_all_products()

    print("\nТовары дешевле 100 сом с количеством больше 5:")
    fetch_products_by_limit(100, 5)

    print("\nПоиск товаров с названием 'мыло':")
    search_products_by_name("мыло")

if __name__ == "__main__":
    main()
