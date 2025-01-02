import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Sidebar
st.sidebar.header("Dashboard")
page = st.sidebar.selectbox("Select Page", ["Overview", "Analytics", "Users", "Settings"])

# Main content
st.title("Enhanced Dashboard Overview")

# Filters
filter_option = st.selectbox("Select Timeframe", ["Today", "Week", "Month", "Year"])

# Sample data
data = {
    "Date": pd.date_range(start="2023-10-19", periods=7, freq='D'),
    "Revenue": np.random.randint(20, 120, size=7),
    "Users": np.random.randint(10, 60, size=7),
    "Systolic": np.random.randint(115, 125, size=7),
    "Diastolic": np.random.randint(75, 85, size=7),
    "Heart Rate": np.random.randint(65, 80, size=7),
    "Sleep Hours": np.random.uniform(6, 8, size=7),
    "Steps": np.random.randint(6000, 10000, size=7)
}
df = pd.DataFrame(data)

# Stats grid
st.subheader("Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", "$124,563", "+12.5%")
col2.metric("Active Users", "8,549", "+23%")
col3.metric("Conversion Rate", "4.6%", "-1.2%")

# Line chart for Revenue and Users
st.subheader("Revenue and Users Over Time")
fig = go.Figure()
fig.add_trace(go.Scatter(x=df["Date"], y=df["Revenue"], mode='lines+markers', name='Revenue'))
fig.add_trace(go.Scatter(x=df["Date"], y=df["Users"], mode='lines+markers', name='Users'))
st.plotly_chart(fig)

# Blood Pressure and Heart Rate charts
st.subheader("Health Metrics")
col1, col2 = st.columns(2)
with col1:
    st.write("Blood Pressure")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["Date"], y=df["Systolic"], mode='lines+markers', name='Systolic'))
    fig.add_trace(go.Scatter(x=df["Date"], y=df["Diastolic"], mode='lines+markers', name='Diastolic'))
    st.plotly_chart(fig)
with col2:
    st.write("Heart Rate")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["Date"], y=df["Heart Rate"], mode='lines+markers', name='Heart Rate'))
    st.plotly_chart(fig)

# Health Metrics Table
st.subheader("Health Metrics Overview")
st.dataframe(df[["Date", "Systolic", "Diastolic", "Heart Rate", "Sleep Hours", "Steps"]])

# Rankings
st.subheader("Top Performers")
rankings = [
    {"name": "John Doe", "score": 98.5},
    {"name": "Jane Smith", "score": 95.2},
    {"name": "Bob Johnson", "score": 92.8}
]
for i, rank in enumerate(rankings, 1):
    st.write(f"{i}. {rank['name']} - Performance Score: {rank['score']}")

# Settings page placeholder
if page == "Settings":
    st.write("Settings page content goes here.")

# Users page placeholder
if page == "Users":
    st.write("Users page content goes here.")

# Analytics page placeholder
if page == "Analytics":
    st.write("Analytics page content goes here.")