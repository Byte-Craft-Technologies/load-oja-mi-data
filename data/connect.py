import psycopg2


def connect_to_db():
    try:
        # Define connection parameters
        connection = psycopg2.connect(
            host="localhost",
            port="5432",
            database="oja_mi_db",
            user="postgres",
            password="root"
        )
        print("Connection successful")
        return connection
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
   