import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page settings
st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("🎓 Student Academic Performance Dashboard")
st.write("Analysis of student academic performance and improvement")

# Load dataset
df = pd.read_csv("dataset/students.csv")

# Statistics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Students", len(df))
col2.metric("Average Marks", round(df["Final_Marks"].mean(), 2))
col3.metric("Highest Marks", df["Final_Marks"].max())
col4.metric("Lowest Marks", df["Final_Marks"].min())

st.divider()

# Display dataset
# Student Search
st.subheader("Individual Student Analysis")

student_id = st.selectbox(
    "Select Student ID",
    df["Student_ID"]
)

student = df[df["Student_ID"] == student_id].iloc[0]

col1, col2, col3 = st.columns(3)

col1.metric("Final Marks", student["Final_Marks"])
col2.metric("Attendance", str(student["Attendance"]) + "%")
col3.metric("Study Hours", student["Study_Hours"])

st.write("### Academic Details")

st.write("Previous Marks:", student["Previous_Marks"])
st.write("Assignment Score:", student["Assignment_Score"])
st.write("Internal Marks:", student["Internal_Marks"])

st.divider()

# Complete Student Records
st.subheader("All Student Records")
st.dataframe(df, use_container_width=True)

# Study hours graph
st.subheader("Study Hours vs Final Marks")

fig, ax = plt.subplots()
sns.scatterplot(data=df, x="Study_Hours", y="Final_Marks", ax=ax)
st.pyplot(fig)
plt.close(fig)

# Attendance graph
st.subheader("Attendance vs Final Marks")

fig, ax = plt.subplots()
sns.scatterplot(data=df, x="Attendance", y="Final_Marks", ax=ax)
st.pyplot(fig)
plt.close(fig)

# Correlation heatmap
st.subheader("Correlation Heatmap")

fig, ax = plt.subplots(figsize=(9, 5))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)
plt.close(fig)

# Performance categories (illustrative thresholds)
st.subheader("Student Performance Categories")

df["Performance"] = pd.cut(
    df["Final_Marks"],
    bins=[-1, 49, 74, 100],
    labels=["Needs Support", "Average", "Good"]
)

st.bar_chart(df["Performance"].value_counts())

st.success("Dashboard loaded successfully!")