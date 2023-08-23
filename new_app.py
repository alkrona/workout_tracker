import psycopg2

# Connection parameters; adjust as necessary
DB_NAME = 'workout_db'
USER = 'kiran'
PASSWORD = '1111'
HOST = 'localhost'
PORT = '5432'

def connect_to_db():
    return psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST, port=PORT)

def create_tables():
    # Connect to the PostgreSQL database
    conn = connect_to_db()
    c = conn.cursor()

    # Create the ExerciseHistory table
    c.execute('''
    CREATE TABLE IF NOT EXISTS ExerciseHistory (
        date DATE PRIMARY KEY,
        exercised BOOL,
        weight REAL,
        protein_intake BOOL,
        water_consumed REAL
    )
    ''')

    # Create the ExerciseDetails table
    c.execute('''
    CREATE TABLE IF NOT EXISTS ExerciseDetails (
        id SERIAL PRIMARY KEY,
        date DATE REFERENCES ExerciseHistory(date),
        exercise_name TEXT,
        exercise_data TEXT
    )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    c.close()
    conn.close()

create_tables()
