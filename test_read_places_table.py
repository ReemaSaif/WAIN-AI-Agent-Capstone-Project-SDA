from database.connection import get_connection

try:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM places LIMIT 5;")
    rows = cursor.fetchall()

    print("Sample rows from places table:")
    for row in rows:
        print(row)

except Exception as e:
    print("Failed to read data:")
    print(e)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection:
        connection.close()
        print("Connection closed.")


