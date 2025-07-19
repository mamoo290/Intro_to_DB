import mysql.connector
from mysql.connector import Error

def insert_book(title, author, published_year, price):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Kogsy@london2025',  # Your password here
            database='alx_book_store'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            insert_query = """
            INSERT INTO books (title, author, published_year, price)
            VALUES (%s, %s, %s, %s);
            """
            data = (title, author, published_year, price)
            cursor.execute(insert_query, data)
            connection.commit()
            print("Book inserted successfully!")
            cursor.close()
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            connection.close()

if __name__ == "__main__":
    # Example: Insert a sample book
    insert_book("The Great Gatsby", "F. Scott Fitzgerald", 1925, 10.99)

