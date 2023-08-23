import sqlite3

DB_NAME = 'exercise_database.db'

def modify_and_link_tables():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Ensure foreign key constraints are enforced for this session
    c.execute("PRAGMA foreign_keys = ON")

    # Create a new temporary table ExerciseDetailsTemp with the desired structure
    c.execute('''
    CREATE TABLE ExerciseDetailsTemp (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE,
        exercise_name TEXT,
        exercise_data TEXT,
        FOREIGN KEY(date) REFERENCES ExerciseHistory(date)
    )
    ''')

    # Copy data from ExerciseDetails to ExerciseDetailsTemp
    c.execute('''
    INSERT INTO ExerciseDetailsTemp (id, exercise_name, exercise_data)
    SELECT id, exercise_name, exercise_data FROM ExerciseDetails
    ''')

    # Delete the original ExerciseDetails table
    c.execute('DROP TABLE ExerciseDetails')

    # Rename ExerciseDetailsTemp to ExerciseDetails
    c.execute('ALTER TABLE ExerciseDetailsTemp RENAME TO ExerciseDetails')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

modify_and_link_tables()