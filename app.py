import sqlite3

DB_NAME = 'exercise_databasev2.db'

def create_tables():
    # Connect to your database
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Create the ExerciseHistory table
    c.execute('''
    CREATE TABLE IF NOT EXISTS ExerciseHistory (
        date DATE PRIMARY KEY,
        exercised BOOLEAN,
        weight REAL,
        protein_intake BOOLEAN,
        water_consumed REAL
    )
    ''')

    # Create the ExerciseDetails table
    c.execute('''
    CREATE TABLE IF NOT EXISTS ExerciseDetails (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE,
        exercise_name TEXT,
        exercise_data TEXT,
        FOREIGN KEY(date) REFERENCES ExerciseHistory(date)
    )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

create_tables()