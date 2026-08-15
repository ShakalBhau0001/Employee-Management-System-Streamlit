import streamlit as st

from core.config import APP_ICON, APP_TITLE
from core.database import get_connection
from gui import dashboard_page, employees_page, import_page

st.set_page_config(page_title=APP_TITLE, page_icon=APP_ICON, layout="wide")

# checking db connection before rendering app
try:
    conn = get_connection()
    conn.close()
except Exception as e:  # noqa: BLE001
    st.error(f"Database connection failed: {e}")
    st.info("Run `python setup_db.py` first to create the database and table.")
    st.stop()

st.sidebar.title(f"{APP_ICON} {APP_TITLE}")
page = st.sidebar.radio("Navigate", ["Dashboard", "Employees", "Bulk Import"])

if page == "Dashboard":
    dashboard_page.render()
elif page == "Employees":
    employees_page.render()
elif page == "Bulk Import":
    import_page.render()
