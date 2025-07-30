from api_request import mock_fetch_data, fetch_data
import psycopg2

def connect_to_db():
    print("Connecting to the database...")
    try:
        conn = psycopg2.connect(
            host="db", 
            port="5432",
            dbname="db",
            user="db_user",
            password="db_password"
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        raise

def create_table(conn):
    print("Creating table if it does not exist...")
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE SCHEMA IF NOT EXISTS dev;
            CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
                id SERIAL PRIMARY KEY,
                city TEXT,
                temperature FLOAT,
                weather_descriptions TEXT,
                wind_speed FLOAT,
                time TIMESTAMP,
                inserted_at TIMESTAMP DEFAULT NOW(),
                utc_offset TEXT
            );
        """)
        conn.commit()
        print("Table was created")
    except psycopg2.Error as e:
        print(f"Error creating table: {e}")
        raise

def insert_records(conn, data):
    print("Inserting records into the database...")
    try:
        location = data['location']
        current = data['current']
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO dev.raw_weather_data(
                city, 
                temperature,
                weather_descriptions,
                wind_speed,
                time,
                inserted_at,
                utc_offset
            ) VALUES (%s, %s, %s, %s, %s, NOW(), %s)
        """,(
            location['name'],
            current['temperature'],
           current['weather_descriptions'][0],
            current['wind_speed'],
            location['localtime'],
            location['utc_offset']
        )
        )
        conn.commit()
        print("Records inserted successfully")

    except psycopg2.Error as e:
        print(f"Error inserting records: {e}")
        raise
def main():
    try:
        # data = mock_fetch_data()
        data = fetch_data()  
        conn = connect_to_db()
        create_table(conn)
        insert_records(conn, data)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
            print("Database connection closed.")
