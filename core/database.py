import mysql.connector

from core.config import DB_CONFIG


def get_connection():
    """Return a new MySQL connection to employee_db."""
    return mysql.connector.connect(**DB_CONFIG)


def get_server_connection():
    """Return connection without selecting a database (used for setup)."""
    cfg = {k: v for k, v in DB_CONFIG.items() if k != "database"}
    return mysql.connector.connect(**cfg)
