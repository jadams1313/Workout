import psycopg2

def connect_to_postgres():
    try:
        # Establish connection
        connection = psycopg2.connect(
            dbname="Workout",
            user="postgres",
            host="localhost",
            port="5432"
        )

        # Create a cursor
        cursor = connection.cursor()

        # Use the cursor to execute SQL commands
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print("Connected to PostgreSQL database. Database version:", db_version)

        # Close the cursor and connection
        cursor.close()
        connection.close()

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL:", error)

if __name__ == "__main__":
    connect_to_postgres()