from core.database import get_connection


def insert_employee(empid, name, address, mobile, designation, department, salary):
    """Insert a new employee record."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO EMP VALUES (%s,%s,%s,%s,%s,%s,%s)",
        (empid, name, address, mobile, designation, department, salary),
    )
    conn.commit()
    cur.close()
    conn.close()


def get_all_employees():
    """Fetch all employee records."""
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM EMP ORDER BY empid")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def get_employee(empid):
    """Fetch a single employee by id."""
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM EMP WHERE empid=%s", (empid,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row


def update_employee(empid, name, address, mobile, designation, department, salary):
    """Update an existing employee record."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """UPDATE EMP SET empname=%s, address=%s, mobileno=%s,
        designation=%s, department=%s, salary=%s WHERE empid=%s""",
        (name, address, mobile, designation, department, salary, empid),
    )
    count = cur.rowcount
    conn.commit()
    cur.close()
    conn.close()
    return count


def delete_employee(empid):
    """Delete an employee record by id."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM EMP WHERE empid=%s", (empid,))
    count = cur.rowcount
    conn.commit()
    cur.close()
    conn.close()
    return count


def search_employees(keyword):
    """Search employees by name, department or designation."""
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    like = f"%{keyword}%"
    cur.execute(
        """SELECT * FROM EMP WHERE empname LIKE %s OR department LIKE %s
        OR designation LIKE %s ORDER BY empid""",
        (like, like, like),
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
