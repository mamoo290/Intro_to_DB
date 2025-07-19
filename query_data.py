import mysql.connector
from mysql.connector import Error

def query_books():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Kogsy@london2025',
            database='alx_book_store'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM books;")
            rows = cursor.fetchall()
            print("Books in database:")
            for row in rows:
                print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Year: {row[3]}, Price: ${row[4]}")
            cursor.close()
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            connection.close()

if __name__ == "__main__":
    query_books()

