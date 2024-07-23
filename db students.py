import sqlite3 as sql

# Создание соединения с базой данных
with sql.connect('students.db') as connection:
    cursor = connection.cursor()

    # cursor.execute('''DROP TABLE IF EXISTS students''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           hobby TEXT,
                           first_name TEXT,
                           last_name TEXT,
                           birth_year INTEGER,
                           homework_score INTEGER
                       )''')

    cursor.execute('''INSERT INTO students (hobby, first_name, last_name, birth_year, homework_score)
    VALUES
    ('Reading', 'Islam', 'Kazbekov', 2007, 15),
    ('Gaming', 'Malsi', 'DoeDoeDoeDoeDoe', 1999, 12),
    ('Cooking', 'Pedro', 'Chikibamboni', 2000, 7),
    ('Painting', 'Pablo', 'Escobar', 1997, 15),
    ('Sports', 'Lionel', 'Messi', 1995, 9),
    ('Music', 'Cristiano', 'Ronaldo', 1996, 11),
    ('Traveling', 'Rafael', 'Nadal', 1994, 10),
    ('Dancing', 'Janis', 'Andetocoumbo', 2001, 6),
    ('Photography', 'LeBron', 'James', 2002, 13),
    ('Programming', 'Arnold', 'Shwarzneger', 2003, 5)
    ''')

    # Выборка студентов с фамилией больше 10 символов
    cursor.execute('''SELECT * FROM students WHERE LENGTH(last_name) > 10''')
    long_last_name_students = cursor.fetchall()
    print("Students with last name longer than 10 characters:")
    for student in long_last_name_students:
        print(student)

    # Обновление имен студентов, у которых баллы за дз больше 10
    cursor.execute('''UPDATE students SET first_name = 'genius'
                      WHERE homework_score > 10''')

    # Вывод студентов с обновленными именами
    cursor.execute('''SELECT * FROM students WHERE first_name = 'genius' ''')
    genius_students = cursor.fetchall()
    print("\nGenius students:")
    for student in genius_students:
        print(student)

    # Удаление студентов с четными id
    cursor.execute('''DELETE FROM students WHERE id % 2 = 0''')

    # Вывод всех студентов после удаления
    cursor.execute('''SELECT * FROM students''')
    remaining_students = cursor.fetchall()
    print("\nRemaining students:")
    for student in remaining_students:
        print(student)
