import sqlite3

conn = sqlite3.connect("expenses.db")
conn.row_factory = sqlite3.Row
c = conn.cursor()

c.execute('''
    Create table if not exists expenses(
          id integer primary key autoincrement,
          date text NOT NULL,
          category text NOT NULL,
          description text NOT NULL,
          amount real NOT NULL check (amount > 0)
          ) 
''')

conn.commit()
conn.close()