import sqlite3

conn = sqlite3.connect("expenses.db")
conn.row_factory = sqlite3.Row
c = conn.cursor()

conn.commit()
conn.close()