import sqlite3
from faker import Faker

con = sqlite3.connect('db_test_1.db')
cursor = con.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS people_data('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'first_name TEXT,'
               'last_name TEXT,'
               'mobile TEXT,'
               'city TEXT)')
con.commit()

fake = Faker('Ru')

data_main = []
counter = 0
for i in range(1000):
    data_main.append({
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'mobile': fake.phone_number(),
        'city': fake.city()})

# for row in data_main:
    # print(list(row.values()))

for row in data_main:
    cursor.execute("INSERT INTO people_data (first_name,last_name,mobile,city)"
                   "VALUES (?,?,?,?)", list(row.values()))
# con.commit()

result_name = cursor.execute("SELECT first_name FROM people_data")
count = 0
for name in result_name.fetchall():
    name = list(name)
    if name.count('Богдан'):
        count += 1
        print(name, count)
