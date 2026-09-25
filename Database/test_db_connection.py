from database.connection import get_connection

try:
    connection = get_connection()
    print("Connected successfully to PostgreSQL")

except Exception as e:
    print("Connection failed:")
    print(e)

finally:
    if 'connection' in locals() and connection:
        connection.close()
        print("Connection closed.")

