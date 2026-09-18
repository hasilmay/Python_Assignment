#SQLite database operations
#import sqlite3 and connect to the database
import sqlite3
conn = sqlite3.connect('card.db')
cursor = conn.cursor()

#create a table
cursor.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL, age INTEGER)""")

#Insert data
cursor.execute("INSERT INTO users (name, age) VALUES ('Barbra',25)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Sharon', 29)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Mark', 35)")

#Retrieve data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

#close the connection
conn.close()

