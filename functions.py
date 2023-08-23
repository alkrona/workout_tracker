import sqlite3
import json

DB_NAME = 'exercise_databasev2.db'

def add_exercise_history(date, exercised, weight, protein_intake, water_consumed):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    c.execute('''
    INSERT INTO ExerciseHistory (date, exercised, weight, protein_intake, water_consumed)
    VALUES (?, ?, ?, ?, ?)
    ''', (date, exercised, weight, protein_intake, water_consumed))
    
    conn.commit()
    conn.close()
    print("ExerciseHistory added successfully!")

def add_exercise_details(date, exercise_name, exercise_data):
    # Convert exercise_data (list of tuples) into a serialized JSON string
    exercise_data_str = json.dumps(exercise_data)
    
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    c.execute('''
    INSERT INTO ExerciseDetails (date, exercise_name, exercise_data)
    VALUES (?, ?, ?)
    ''', (date, exercise_name, exercise_data_str))
    
    conn.commit()
    conn.close()
    print("ExerciseDetails added successfully!")
def dategetter():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    
    c.execute('''
    SELECT date FROM ExerciseHistory 
    ''')
   
    conn.commit()
    dates = c.fetchall()
    actual_dates = []
    for date in dates:
        actual_dates.append(date[0])
    conn.close()
    print("fetch successful")
    return actual_dates

# Example usage:
if __name__ == "__main__":
    add_exercise_details('2023-08-23', 'Squat', [ (55, 8), (60, 6)])