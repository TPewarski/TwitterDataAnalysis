import sqlite3

def create_database():
    conn = sqlite3.connect('mydatabase.db')  # This will create a new database file 'mydatabase.db' if it doesn't exist
    cursor = conn.cursor()
    
    # Create a new table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       email TEXT NOT NULL UNIQUE)''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
