import pandas as pd
import plotly.express as px
import streamlit as st

from core.analytics import (
    department_wise_count,
    department_wise_salary,
    designation_wise_count,
    salary_stats,
    top_earners,
    total_employees,
)
from core.crud import get_all_employees
from exporters.excel_exporter import export_to_excel
from exporters.pdf_exporter import export_to_pdf


def render():
    st.header("📊 Dashboard")

    total = total_employees()
    stats = salary_stats()
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Employees", total)
    c2.metric("Avg Salary", f"{stats['avg_sal']:,.2f}" if stats["avg_sal"] else "0")
    c3.metric("Max Salary", f"{stats['max_sal']:,.2f}" if stats["max_sal"] else "0")
    c4.metric("Min Salary", f"{stats['min_sal']:,.2f}" if stats["min_sal"] else "0")

    st.divider()
    _department_dashboard()
    st.divider()
    _salary_dashboard()
    st.divider()
    _export_dashboard()


def _department_dashboard():
    st.subheader("Department-wise Overview")
    dept_count = department_wise_count()
    desig_count = designation_wise_count()

    if not dept_count:
        st.info("No data to show.")
        return

    col1, col2 = st.columns(2)
    with col1:
        df = pd.DataFrame(dept_count)
        fig = px.pie(
            df, names="department", values="emp_count", title="Employees by Department"
        )
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        df2 = pd.DataFrame(desig_count)
        fig2 = px.bar(
            df2, x="designation", y="emp_count", title="Employees by Designation"
        )
        st.plotly_chart(fig2, use_container_width=True)


def _salary_dashboard():
    st.subheader("Salary-wise Overview")
    dept_salary = department_wise_salary()

    if not dept_salary:
        st.info("No data to show.")
        return

    df = pd.DataFrame(dept_salary)
    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(
            df, x="department", y="total_salary", title="Total Salary by Department"
        )
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig2 = px.bar(
            df, x="department", y="avg_salary", title="Average Salary by Department"
        )
        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Top 5 Earners")
    top = top_earners(5)
    if top:
        st.dataframe(pd.DataFrame(top), use_container_width=True)


def _export_dashboard():
    st.subheader("Export Full Report")
    data = get_all_employees()
    col1, col2 = st.columns(2)
    with col1:
        st.download_button(
            "⬇️ Download Full Report (Excel)",
            export_to_excel(data),
            file_name="employee_report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
    with col2:
        st.download_button(
            "⬇️ Download Full Report (PDF)",
            export_to_pdf(data, "Full Employee Report"),
            file_name="employee_report.pdf",
            mime="application/pdf",
        )
