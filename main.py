import sqlite3
from pprint import pprint

con = sqlite3.connect('students.db')
cursor = con.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS grades(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER,
                    subject TEXT,
                    grade FLOAT,
                    FOREIGN KEY (student_id) REFERENCES students(id))''')
con.commit()


class University:
    def __init__(self, name):
        self.name = name

    def add_student(self, name: str, age: int):
        '''Функция добавления Имени студента и возраста в БД'''
        # self.students.append((name, age))
        with sqlite3.connect('students.db') as conn:
            cur = conn.cursor()
            sql = (f"INSERT INTO students (name, age) "
                   f"VALUES ('{name}', {age})")
            cur.execute(sql)
            id_student = cur.lastrowid
            conn.commit()
            return id_student

    def add_grade(self, student_id: int, subject: str, grade: float):
        '''
        Функция добавления данных студент айди?,предмета и оценки в БД
        '''
        # self.grades.append((student_id, subject, grade))
        with sqlite3.connect('students.db') as conn:
            cur = conn.cursor()
            sql = (f"INSERT INTO grades (student_id, subject, grade) "
                   f"VALUES ({student_id}, '{subject}', {grade})")
            cur.execute(sql)
            conn.commit()

    def get_students(self, subject=None) -> list:
        '''Функция вывода в консоль списка студентов и оценок
        :param subject: str
        :param return: list'''
        with sqlite3.connect('students.db') as conn:
            cur = conn.cursor()

            if subject:
                cur.execute('SELECT s.name, s.age, g.subject, g.grade '
                            'FROM students s, grades g '
                            'WHERE s.id = g.student_id AND g.subject = ?', (subject,))
            else:
                cur.execute('SELECT s.name, s.age, g.subject, g.grade '
                            'FROM students s, grades g '
                            'WHERE s.id = g.student_id')
            return cur.fetchall()


univer = University('Urban')

# univer.add_student('Елена', 24)
# univer.add_student('Сергей', 42)
# univer.add_student('Ира', 54)
# univer.add_student('Игорь', 23)
# univer.add_grade(1, 'Python', 4.9)
# univer.add_grade(1, 'Java', 5)
# univer.add_grade(2, 'Python', 5)
# univer.add_grade(2, 'Java', 4.9)
# univer.add_grade(3, 'Python', 4.8)
# univer.add_grade(3, 'Java', 3.9)
# univer.add_grade(4, 'Python', 4.3)
# univer.add_grade(4, 'Java', 4.6)
pprint(univer.get_students())
print('*' * 30)
pprint(univer.get_students('Python'))
