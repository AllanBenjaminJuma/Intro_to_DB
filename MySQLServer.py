import mysql.connector
from mysql.connector import Error

def create_alx_book_store_database():
    """
    Connects to MySQL server and creates the 'alx_book_store' database
    if it doesn't already exist.
    """
    # Configure your database connection details here
    # IMPORTANT: Replace with your actual MySQL server credentials
    config = {
        'host': 'localhost',
        'user': 'your_mysql_username', # e.g., 'root'
        'password': 'your_mysql_password', # e.g., 'password123'
        # Do NOT specify 'database' here, as we are creating it
    }

    connection = None
    try:
        # Establish a connection to the MySQL server
        # We connect without specifying a database initially
        connection = mysql.connector.connect(**config)

        if connection.is_connected():
            cursor = connection.cursor()

            # SQL statement to create the database if it does not already exist
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"

            # Execute the query
            cursor.execute(create_db_query)

            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # Handle connection and other MySQL-specific errors
        print(f"Error connecting to MySQL or creating database: {e}")
    finally:
        # Ensure the connection is closed
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_alx_book_store_database()