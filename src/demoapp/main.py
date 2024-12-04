import streamlit as st
import pandas as pd
import plotly.express as px 
import os

st.sidebar.title("Skvělé ISV firmy")
page = st.sidebar.radio("Select a company", ["Company 1", "Company 2", "Company 3"])

def load_data(file_path):
    if not os.path.exists(file_path):
        st.error(f"File {file_path} does not exist.")
        return None
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            st.error(f"File {file_path} is empty.")
            return None
        return df
    except pd.errors.EmptyDataError:
        st.error(f"No columns to parse from {file_path}.")
        return None

if page == "Company 1":
    st.title("Company 1 Performance")
    df = load_data("company1.csv")
    if df is not None:
        fig = px.line(df, x='day', y='sales', title='Company 1 Sales Over Time')
        st.plotly_chart(fig)

elif page == "Company 2":
    st.title("Company 2 Revenue")
    df = load_data("company2.csv")
    if df is not None:
        fig = px.bar(df, x='month', y='revenue', title='Company 2 Monthly Revenue')
        st.plotly_chart(fig)

elif page == "Company 3":
    st.title("Company 3 Patient Distribution")
    df = load_data("company3.csv")
    if df is not None:
        fig = px.pie(df, names='department', values='patients', title='Patients per Department')
        st.plotly_chart(fig)


        