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
def dategetter():
    conn = connect_to_db()
    c = conn.cursor()
    
    c.execute('''
    SELECT * FROM ExerciseHistory 
    ''')
    
    dates = c.fetchall()
    for date in dates:
        print(date)
if __name__=="__main__":
    dategetter()