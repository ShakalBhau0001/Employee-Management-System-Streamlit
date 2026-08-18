import io

import pandas as pd


def export_to_excel(data):
    """Convert list of dict rows to an in-memory Excel file, returns bytes."""
    df = pd.DataFrame(data)
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Employees")
    buffer.seek(0)
    return buffer.getvalue()
