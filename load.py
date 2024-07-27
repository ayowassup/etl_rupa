import json
import sqlite3


def load_to_sqlite(json_file, db_name='etl.db'):
    try:
        with open(json_file, 'r') as f:
            products = json.load(f)
    except Exception as e:
        print(f'Error reading JSON file: {e}')
        return

    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # Create table if not exists
    c.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            final_price TEXT,
            initial_price TEXT,
            discounted TEXT,
            rating TEXT,
            product_url TEXT,
            image_url TEXT
        )
        ''')

    try:
        for product in products:
            c.execute('''
                INSERT INTO products (name, final_price, initial_price, discounted, rating, product_url, image_url)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                product['name'],
                product['final_price'],
                product['initial_price'],
                product['discounted'],
                product['rating'],
                product['product_url'],
                product['image_url']
            ))
        conn.commit()
    except Exception as e:
        print(f'Error inserting data into SQLite: {e}')

    conn.close()
    print('Data successfully loaded to SQLite database')


if __name__ == '__main__':
    load_to_sqlite('transformed_products.json')
