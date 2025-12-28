import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Student Performance Analyzer (Streamlit App)")

# Number of students
n = st.number_input("Enter number of students:", min_value=1, step=1)

students = []
marks_list = []

st.write("### ✍️ Enter Student Details:")

for i in range(n):
    name = st.text_input(f"Student {i+1} Name:", key=f"name_{i}")
    m1 = st.number_input(f"Maths Marks of {name}", min_value=0, max_value=100, step=1, key=f"m1_{i}")
    m2 = st.number_input(f"Science Marks of {name}", min_value=0, max_value=100, step=1, key=f"m2_{i}")
    m3 = st.number_input(f"English Marks of {name}", min_value=0, max_value=100, step=1, key=f"m3_{i}")

    if name:
        students.append(name)
        marks_list.append([m1, m2, m3])

# Run analysis button
if st.button("Analyze Result"):
    
    marks = np.array(marks_list)

    df = pd.DataFrame(
        marks,
        columns=["Maths", "Science", "English"],
        index=students
    )

    df["Total"] = df.sum(axis=1)
    df["Average"] = df["Total"] / 3
    df["Result"] = np.where(df["Average"] >= 40, "Pass", "Fail")

    class_average = np.mean(df["Average"])
    topper = df["Total"].idxmax()

    st.write("## 📌 Results Table")
    st.dataframe(df)

    st.write("### 📈 Class Statistics:")
    st.write("**Class Average Marks:**", round(class_average, 2))
    st.write("**Topper of the Class:**", topper)

    # Bar Chart
    st.write("### 📊 Total Marks Comparison")
    fig = plt.figure(figsize=(8,5))
    plt.bar(df.index, df["Total"], color="skyblue")
    plt.title("Total Marks of Students")
    plt.xlabel("Students")
    plt.ylabel("Total Marks")
    plt.xticks(rotation=45)
    st.pyplot(fig)
