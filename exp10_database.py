import sqlite3

# Create a new SQLite database (e.g., "mydatabase.db")
conn = sqlite3.connect("mydatabase.db")

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS mytable (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')

# Commit the changes to the database
conn.commit()

# Insert values into the table
cursor.execute("INSERT INTO mytable (name, age) VALUES (?, ?)", ("Abdul", 19))
cursor.execute("INSERT INTO mytable (name, age) VALUES (?, ?)", ("Yashas", 18))
cursor.execute("INSERT INTO mytable (name, age) VALUES (?, ?)", ("Python", 32))

# Commit the changes again
conn.commit()

# Retrieve and display values from the table
cursor.execute("SELECT * FROM mytable")
rows = cursor.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

# Update values in the table
new_age = 35
cursor.execute("UPDATE mytable SET age = ? WHERE name = ?", (new_age, "Abdul"))

# Commit the changes
conn.commit()

# Delete previous rows printed to make it look cleaner
cursor.execute("Delete from mytable")
conn.commit()

# Close the database connection
conn.close()
