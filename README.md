## 👨‍💼 Employee Management System (Streamlit + MySQL, Modular)

## 📘 Overview

**Employee Management System** is a modular Python + Streamlit web app to manage employee records with MySQL as the backend, department/salary dashboards, and PDF/Excel export.

Ported and redesigned from the original [Employee-Management-System-Using-Java](https://github.com/ShakalBhau0001) (Java + JDBC + Oracle, CLI-based).

## 🧭 Philosophy

1. **Separation of concerns** — `core` handles data, `exporters` handle files, `gui` handles UI. Nothing crosses lanes.
2. **One function, one job** — every CRUD/analytics function does exactly one query.
3. **Fail loud** — DB and validation errors surface in the UI, never swallowed silently.

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

## 🧰 Tech Stack

| Layer        | Technology              |
| ------------ | ------------------------|
| GUI          | Streamlit               |
| Database     | MySQL                   |
| DB Driver    | mysql-connector-python  |
| Charts       | Plotly                  |
| Excel Export | pandas + openpyxl       |
| PDF Export   | reportlab               |

## ✨ Features

- Add / View / Update / Delete employee records
- Search by name, department or designation
- Input validation (10-digit mobile, non-empty name, positive salary)
- Bulk import employees from CSV/Excel
- Dashboard: total employees, salary stats, department-wise pie & bar charts, designation-wise chart
- Salary dashboard: total/average salary by department, top 5 earners
- Export any view (filtered or full) to PDF or Excel

## ⚙️ Setup Guide

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Configure MySQL credentials

Edit `core/config.py` (default: `root` / `root`).

### 3️⃣ Create database and table

```bash
python setup_db.py
```

### 4️⃣ Run the app

```bash
streamlit run main.py
```

## 🗄️ EMP Table Schema

| Column       | Type          |
| ------------ | ------------- |
| empid        | INT (PK)      |
| empname      | VARCHAR(50)   |
| address      | VARCHAR(50)   |
| mobileno     | BIGINT        |
| designation  | VARCHAR(20)   |
| department   | VARCHAR(20)   |
| salary       | DECIMAL(7,2)  |

## 🛣️ Roadmap

- [ ] Admin login/authentication
- [ ] Employee photo upload (assets/)
- [ ] Attendance/leave tracking module
- [ ] Email payslip generator

> ⚠️ **Disclaimer:** For learning purposes. Use environment variables for DB credentials in production, not hardcoded values.

---

## 🪪 Author

> **Creator: Shakal Bhau**

> **GitHub: [ShakalBhau0001](https://github.com/ShakalBhau0001)**

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!

---
