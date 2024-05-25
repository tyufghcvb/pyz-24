from models.camp import Camp
from models.exercise import Exercise
from models.training_unit import TrainingUnit

import sqlite3


def get_db_connection():
    conn = sqlite3.connect('example.db')
    conn.row_factory = sqlite3.Row
    return conn


def create_tables(conn):
    cursor = conn.cursor()

    # Tabela dla Camp
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Camp (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT,
        training_units INTEGER,
        start_date TEXT,
        end_date TEXT
    )
    ''')

    # Tabela dla Exercise
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Exercise (
        id INTEGER PRIMARY KEY,
        exercise_name TEXT NOT NULL,
        description TEXT,
        training_type TEXT,
        exercise_reps INTEGER,
        exercise_weight REAL,
        exercise_side TEXT DEFAULT 'LR',
        exercise_intensity INTEGER DEFAULT 100
    )
    ''')

    # Tabela dla TrainingUnit
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS TrainingUnit (
        id INTEGER PRIMARY KEY,
        description TEXT,
        camp_id INTEGER,
        camp_name TEXT,
        training_number INTEGER,
        training_type TEXT,
        date TEXT,
        FOREIGN KEY (camp_id) REFERENCES Camp (id)
    )
    ''')

    conn.commit()


def insert_camp(conn, camp):
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO Camp (id, name, description, training_units, start_date, end_date)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (camp.id, camp.name, camp.description, camp.training_units, camp.start_date, camp.end_date))
    conn.commit()


def insert_exercise(conn, exercise):
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO Exercise (id, exercise_name, description, training_type, exercise_reps, exercise_weight, exercise_side, exercise_intensity)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (exercise.id, exercise.exercise_name, exercise.description, exercise.training_type, exercise.exercise_reps,
          exercise.exercise_weight, exercise.exercise_side, exercise.exercise_intensity))
    conn.commit()


def insert_training_unit(conn, training_unit):
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO TrainingUnit (id, description, camp_id, camp_name, training_number, training_type, date)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (training_unit.id, training_unit.description, training_unit.camp_id, training_unit.camp_name,
          training_unit.training_number, training_unit.training_type, training_unit.date))
    conn.commit()


def display_training_unit(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM TrainingUnit')
    training_units = cursor.fetchall()

    for unit in training_units:
        print(
            f'ID: {unit["id"]}, Description: {unit["description"]}, Camp Name: {unit["camp_name"]},  Training Type: {unit["training_type"]}, Date: {unit["date"]}')
    conn.commit()


if __name__ == '__main__':
    conn = get_db_connection()
    # create_tables(conn)
    # conn.close()

    camp1 = Camp(1, '2024 May Camp', 'Ploymetric', 10, '2024-05-01', '2024-05-31')
    exercise1 = Exercise(1, 'Push-up', 'Upper body exercise', 'Strength', 20, 0, 'LR', 80)
    training_unit1 = TrainingUnit(1, 'Morning workout', 1, '2024 May Camp', 1, 'Strength', '2024-06-01')

    # Zapisywanie obiektów do bazy danych
    # insert_camp(conn, camp1)
    # insert_exercise(conn, exercise1)
    # insert_training_unit(conn, training_unit1)

    display_training_unit(conn)

    conn.close()
