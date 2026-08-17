import re


def is_valid_mobile(mobile):
    """Check mobile number is 10 digits."""
    return bool(re.fullmatch(r"\d{10}", str(mobile)))


def is_valid_name(name):
    """Check name is non-empty."""
    return bool(name and name.strip())


def is_valid_salary(salary):
    """Check salary is positive."""
    return float(salary) > 0
