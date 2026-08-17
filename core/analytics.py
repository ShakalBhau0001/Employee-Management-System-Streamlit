from core.database import get_connection


def total_employees():
    """Return total employee count."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM EMP")
    count = cur.fetchone()[0]
    cur.close()
    conn.close()
    return count


def department_wise_count():
    """Employee count grouped by department."""
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT department, COUNT(*) AS emp_count FROM EMP GROUP BY department")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def department_wise_salary():
    """Total and average salary grouped by department."""
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute(
        """SELECT department, SUM(salary) AS total_salary, AVG(salary) AS avg_salary
        FROM EMP GROUP BY department"""
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def salary_stats():
    """Overall min, max, avg salary."""
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT MIN(salary) AS min_sal, MAX(salary) AS max_sal, AVG(salary) AS avg_sal FROM EMP")
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row


def top_earners(limit=5):
    """Top N highest paid employees."""
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM EMP ORDER BY salary DESC LIMIT %s", (limit,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def designation_wise_count():
    """Employee count grouped by designation."""
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT designation, COUNT(*) AS emp_count FROM EMP GROUP BY designation")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
