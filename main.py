import sqlite3
from faker import Faker

con = sqlite3.connect('db_test.db')
cursor = con.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS people_data('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'first_name TEXT,'
               'last_name TEXT,'
               'mobile INTEGER,'
               'city TEXT)')
con.commit()

fake = Faker('Ru')

data = []

for i in range(100):
    data.append({'first_name': fake.first_name(),
                 'last_name': fake.last_name(),
                 'mobile': fake.phone_number(),
                 'city': fake.city()})

for row in data:
    print(row)

for row in data:
    cursor.execute("INSERT INTO people_data (first_name,last_name,mobile,city)"
                   "VALUES (?,?,?,?)", row.values())
    con.commit()
