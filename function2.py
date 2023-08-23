import psycopg2
import json

# Connection parameters; adjust as necessary
DB_NAME = 'workout_db'
USER = 'kiran'
PASSWORD = '1111'
HOST = 'localhost'
PORT = '5432'

def connect_to_db():
    return psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST, port=PORT)

def add_exercise_history(date, exercised, weight, protein_intake, water_consumed):
    conn = connect_to_db()
    c = conn.cursor()
    
    c.execute('''
    INSERT INTO ExerciseHistory (date, exercised, weight, protein_intake, water_consumed)
    VALUES (%s, %s, %s, %s, %s)
    ''', (date, exercised, weight, protein_intake, water_consumed))
    
    conn.commit()
    conn.close()
    print("ExerciseHistory added successfully!")

def add_exercise_details(date, exercise_name, exercise_data):
    # Convert exercise_data (list of tuples) into a serialized JSON string
    exercise_data_str = json.dumps(exercise_data)
    
    conn = connect_to_db()
    c = conn.cursor()
    
    c.execute('''
    INSERT INTO ExerciseDetails (date, exercise_name, exercise_data)
    VALUES (%s, %s, %s)
    ''', (date, exercise_name, exercise_data_str))
    
    conn.commit()
    conn.close()
    print("ExerciseDetails added successfully!")

def dategetter():
    conn = connect_to_db()
    c = conn.cursor()
    
    c.execute('''
    SELECT date FROM ExerciseHistory 
    ''')
    
    dates = c.fetchall()
    actual_dates = [date[0] for date in dates]
    conn.close()
    print("fetch successful")
    return actual_dates

# Example usage:
if __name__ == "__main__":
    add_exercise_details('2023-08-23', 'Squat', [(55, 8), (60, 6)])
