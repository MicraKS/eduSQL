import sqlite3
from dataMob import description, mobile_phone, description_id, price, rating, title

conn = sqlite3.connect('homework.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Мобильные_телефоны(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
mobile_phone TEXT NOT NULL UNIQUE, 
description TEXT NOT NULL,
description_id INTEGER,
price INTEGER,
rating INTEGER,
title TEXT
)''')

for i in range(15):
    cursor.execute('INSERT INTO Мобильные_телефоны (mobile_phone, description, description_id, price, rating, title) '
                   'VALUES (?, ?, ?, ?, ?, ?)',
                   (mobile_phone[i], description[i], description_id[i], price[i], rating[i], title[i]))
    conn.commit()

print('Таблица успешно создана и заполнена данными!')

conn.close()
