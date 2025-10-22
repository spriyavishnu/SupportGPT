import os
import sqlite3
from dotenv import load_dotenv


# Load environment variables from a .env file (if present)
load_dotenv()


def get_database_connection(db_path: str = "supportgpt.db") -> sqlite3.Connection:
  """Establish and return a sqlite3.Connection with row factory set.

  Args:
    db_path: Path to the SQLite database file.

  Raises:
    sqlite3.Error: If a connection cannot be established.
  """

  try:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    print("Database connection established.")
    return conn
  except sqlite3.Error as e:
    print("Error connecting to database:", e)
    raise


def test_connection() -> bool:
  """Run a simple SELECT 1 to verify the database is reachable.

  Returns True on success, False on failure.
  """

  try:
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    _ = cursor.fetchone()
    cursor.close()
    conn.close()
    print("🎉 SQLite test passed!")
    return True
  except Exception as e:
    print("❌ SQLite test failed:", e)
    return False
def create_database(db_path: str = "supportgpt.db") -> bool:
  """Create the SupportTickets table and indexes if they don't exist.

  Returns True on success, False on failure.
  """

  try:
    conn = get_database_connection(db_path)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS SupportTickets (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      customer_email TEXT NOT NULL,
      subject TEXT NOT NULL,
      description TEXT,
      category TEXT,
      priority TEXT DEFAULT 'medium',
      status TEXT DEFAULT 'open',
      ai_priority_score INTEGER,
      suggested_solution TEXT,
      auto_categorized INTEGER DEFAULT 0,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_supporttickets_email
    ON SupportTickets(customer_email)
    """)

    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_supporttickets_status
    ON SupportTickets(status)
    """)

    # Add sample data if table is empty
    cursor.execute("SELECT COUNT(*) FROM SupportTickets")
    count = cursor.fetchone()[0]
    if count == 0:
      cursor.execute("""
      INSERT INTO SupportTickets
        (customer_email, subject, description, priority, status)
      VALUES
        ('john@example.com', 'Login issues', 'Cannot login to my account', 'high', 'open'),
        ('sarah@company.com', 'Feature request', 'Please add dark mode', 'medium', 'open'),
        ('mike@tech.com', 'Payment failed', 'Credit card payment declined', 'urgent', 'open')
      """)
      print("✅ Added sample tickets")

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ SQLite database initialized successfully!")
    return True

  except Exception as e:
    print(f"❌ Database initialization failed: {e}")
    return False


if __name__ == "__main__":
  # Basic CLI behavior when run as a script from PowerShell / terminal.
  print("Running database sanity checks...")
  ok = test_connection()
  print(f"test_connection -> {ok}")
  created = create_database()
  print(f"create_database -> {created}")