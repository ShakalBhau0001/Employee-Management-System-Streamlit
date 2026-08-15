# Employee-Management-System-Streamlit
Employee Management System is a modular Python + Streamlit web app to manage employee records with MySQL as the backend, department/salary dashboards, and PDF/Excel export.

> **Note : Project Work in Progress **

---

## 📂 Folder Structure

```
Employee-Management-System-Streamlit/
│
├── assets/                    # static assets (logo, images)
├── core/
│   ├── __init__.py
│   ├── config.py               # DB creds + constants
│   ├── database.py             # MySQL connection helpers
│   ├── crud.py                 # add/view/update/delete/search
│   ├── analytics.py            # dashboard aggregate queries
│   └── validators.py           # input validation
├── exporters/
│   ├── __init__.py
│   ├── excel_exporter.py       # export to .xlsx
│   └── pdf_exporter.py         # export to .pdf
├── gui/
│   ├── __init__.py
│   ├── dashboard_page.py       # department + salary dashboards
│   ├── employees_page.py       # CRUD screen
│   └── import_page.py          # bulk CSV/Excel import
│
├── main.py                     # Streamlit entrypoint
├── setup_db.py                 # one-time DB/table setup script
├── requirements.txt
├── LICENSE
└── .gitignore
```

---
