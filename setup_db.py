import sqlite3

# Connect to database (it will create one if not exists)
conn = sqlite3.connect("incidents.db")
cursor = conn.cursor()

# Create incidents table (if not exists)
cursor.execute("""
CREATE TABLE IF NOT EXISTS incidents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    assignee TEXT,
    status TEXT DEFAULT 'Open'
)
""")

# Create users table (if not exists)
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

print("✅ Tables created successfully!")

# --- Insert a test user ---
try:
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("gauravmw", "gauravmw123"))
    print("✅ Test user added successfully! (username: gauravmw / password: gauravmw123)")
except sqlite3.IntegrityError:
    print("⚠️ Test user already exists, skipping...")

# Save changes and close
conn.commit()
conn.close()
