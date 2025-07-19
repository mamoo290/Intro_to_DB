import mysql.connector
from mysql.connector import Error

def create_tables():
    try:
        # Connect to MySQL database alx_book_store using your credentials
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Kogsy@london2025',  # Replace with your password if different
            database='alx_book_store'      # This is your database name
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # SQL command to create a 'books' table with columns for id, title, author, year, price
            create_books_table = """
            CREATE TABLE IF NOT EXISTS books (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                author VARCHAR(255),
                published_year INT,
                price DECIMAL(10, 2)
            );
            """

            # Execute the SQL command
            cursor.execute(create_books_table)

            # Save the changes to the database
            connection.commit()

            print("Table 'books' created successfully!")

            cursor.close()

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_tables()

