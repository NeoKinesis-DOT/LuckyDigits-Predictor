import sqlite3

# Create a connection to the database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create the table
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS database(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               date TEXT UNIQUE,
               pm_1 TEXT,
               pm_3 TEXT,
               pm_6 TEXT,
               pm_8 TEXT)
"""
)

# Commit the changes
conn.commit()
conn.close()

print("Database created successfully")
