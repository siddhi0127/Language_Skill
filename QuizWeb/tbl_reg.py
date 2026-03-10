import sqlite3

# connect to database
conn = sqlite3.connect("users.db")

cursor = conn.cursor()

# create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tblregister(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
email TEXT,
password TEXT
)
""")

conn.commit()
conn.close()

print("users table created")