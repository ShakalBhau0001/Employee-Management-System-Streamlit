from core.config import DB_CONFIG
from core.database import get_connection, get_server_connection


def main():
    conn = get_server_connection()
    cur = conn.cursor()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
    conn.commit()
    cur.close()
    conn.close()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS EMP (
            empid INT PRIMARY KEY,
            empname VARCHAR(50),
            address VARCHAR(50),
            mobileno BIGINT,
            designation VARCHAR(20),
            department VARCHAR(20),
            salary DECIMAL(10,2)
        )
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Database and table ready.")


if __name__ == "__main__":
    main()
