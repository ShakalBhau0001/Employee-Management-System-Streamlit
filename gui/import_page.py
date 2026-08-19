import pandas as pd
import streamlit as st

from core.crud import (
    get_employee,
    insert_employee,
)

REQUIRED_COLS = [
    "empid",
    "empname",
    "address",
    "mobileno",
    "designation",
    "department",
    "salary",
]


def render():
    st.header("📥 Bulk Import")
    st.caption(f"File must have columns: {', '.join(REQUIRED_COLS)}")
    file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

    if not file:
        return

    df = pd.read_csv(file) if file.name.endswith(".csv") else pd.read_excel(file)
    st.dataframe(df, use_container_width=True)
    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    if missing:
        st.error(f"Missing columns: {', '.join(missing)}")
        return

    if st.button("Import Records"):
        added, skipped = 0, 0
        for _, row in df.iterrows():
            empid = int(row["empid"])
            if get_employee(empid):
                skipped += 1
                continue
            insert_employee(
                empid,
                row["empname"],
                row["address"],
                str(row["mobileno"]),
                row["designation"],
                row["department"],
                float(row["salary"]),
            )
            added += 1
        st.success(f"Imported {added} record(s). Skipped {skipped} duplicate(s).")
