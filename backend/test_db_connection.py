import pyodbc

# Test the connection
try:
    connection_string = (
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=localhost\\SQLEXPRESS;"
        "Database=agentops;"
        "Trusted_Connection=yes;"
        "Connection Timeout=5"
    )
    
    conn = pyodbc.connect(connection_string)
    print("✓ Connection successful!")
    conn.close()
except pyodbc.Error as e:
    print(f"✗ Connection failed: {e}")
except Exception as e:
    print(f"✗ Error: {e}")
