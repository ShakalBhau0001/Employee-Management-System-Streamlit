import pandas as pd
import streamlit as st

from core.config import DEPARTMENTS, DESIGNATIONS
from core.crud import (
    delete_employee,
    get_all_employees,
    get_employee,
    insert_employee,
    search_employees,
    update_employee,
)
from core.validators import is_valid_mobile, is_valid_name, is_valid_salary
from exporters.excel_exporter import export_to_excel
from exporters.pdf_exporter import export_to_pdf


def render():
    st.header("Employee Records")
    menu = st.radio("Action", ["View", "Add", "Update", "Delete"], horizontal=True)
    if menu == "View":
        _view_section()
    elif menu == "Add":
        _add_section()
    elif menu == "Update":
        _update_section()
    elif menu == "Delete":
        _delete_section()


def _view_section():
    keyword = st.text_input("Search by name / department / designation", "")
    data = search_employees(keyword) if keyword else get_all_employees()

    if not data:
        st.info("No records found.")
        return

    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
    col1, col2 = st.columns(2)
    with col1:
        st.download_button(
            "⬇️ Export to Excel",
            export_to_excel(data),
            file_name="employees.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
    with col2:
        st.download_button(
            "⬇️ Export to PDF",
            export_to_pdf(data, "Employee Report"),
            file_name="employees.pdf",
            mime="application/pdf",
        )


def _add_section():
    with st.form("add_form", clear_on_submit=True):
        empid = st.number_input("Employee Id", min_value=1, step=1)
        name = st.text_input("Employee Name")
        address = st.text_input("Address")
        mobile = st.text_input("Mobile No")
        designation = st.selectbox("Designation", DESIGNATIONS)
        department = st.selectbox("Department", DEPARTMENTS)
        salary = st.number_input("Salary", min_value=0.0, step=100.0, format="%.2f")
        submitted = st.form_submit_button("Add Employee")

    if submitted:
        if get_employee(empid):
            st.error("Employee Id already exists.")
        elif not is_valid_name(name):
            st.error("Name cannot be empty.")
        elif not is_valid_mobile(mobile):
            st.error("Mobile number must be 10 digits.")
        elif not is_valid_salary(salary):
            st.error("Salary must be greater than 0.")
        else:
            insert_employee(
                empid, name, address, mobile, designation, department, salary
            )
            st.success("Employee added successfully.")


def _update_section():
    empid = st.number_input("Enter Employee Id", min_value=1, step=1)

    if st.button("Fetch Record"):
        emp = get_employee(empid)
        st.session_state["emp_data"] = emp
        if not emp:
            st.error("No record found with this Id.")

    emp = st.session_state.get("emp_data")
    if emp:
        with st.form("update_form"):
            name = st.text_input("Employee Name", emp["empname"])
            address = st.text_input("Address", emp["address"])
            mobile = st.text_input("Mobile No", str(emp["mobileno"]))
            designation = st.selectbox(
                "Designation",
                DESIGNATIONS,
                index=DESIGNATIONS.index(emp["designation"])
                if emp["designation"] in DESIGNATIONS
                else 0,
            )
            department = st.selectbox(
                "Department",
                DEPARTMENTS,
                index=DEPARTMENTS.index(emp["department"])
                if emp["department"] in DEPARTMENTS
                else 0,
            )
            salary = st.number_input(
                "Salary", value=float(emp["salary"]), step=100.0, format="%.2f"
            )
            submitted = st.form_submit_button("Update Employee")

        if submitted:
            count = update_employee(
                empid, name, address, mobile, designation, department, salary
            )
            if count:
                st.success("Record updated successfully.")
                st.session_state["emp_data"] = None
            else:
                st.error("Update failed.")


def _delete_section():
    empid = st.number_input("Enter Employee Id to delete", min_value=1, step=1)
    if st.button("Delete Employee", type="primary"):
        count = delete_employee(empid)
        if count:
            st.success(f"Employee Id {empid} deleted successfully.")
        else:
            st.error("No record found with this Id.")
