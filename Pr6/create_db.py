import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

create_db = '''CREATE TABLE IF NOT EXISTS quotes (_BUS_ TEXT, _Price_ TEXT, _Locate_ TEXT)''' 

cursor.execute(create_db)
conn.commit()
conn.close()