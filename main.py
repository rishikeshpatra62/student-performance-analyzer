import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

students = []
marks_list = []

n = int(input("Enter number of students: "))


            # Input Section #

for i in range(n):
    name = input(f"\nEnter name of student {i+1}: ")
    students.append(name)

    m1 = int(input("Enter Maths marks: "))
    m2 = int(input("Enter Science marks: "))
    m3 = int(input("Enter English marks: "))

    marks_list.append([m1, m2, m3])


            # NumPy Array #

marks = np.array(marks_list)

            # Pandas DataFrame #

df = pd.DataFrame(
    marks,
    columns=["Maths", "Science", "English"],
    index=students
)

            # Analysis #

df["Total"] = df.sum(axis=1)
df["Average"] = df["Total"] / 3
df["Result"] = np.where(df["Average"] >= 40, "Pass", "Fail")

class_average = np.mean(df["Average"])
topper = df["Total"].idxmax()


print("\n📊 STUDENT PERFORMANCE ANALYZER")
print("--------------------------------")
print(df)

print("\nClass Average Marks:", round(class_average, 2))
print("Topper of the Class:", topper)


            # Visualization using (Matplotlib) #

plt.figure(figsize=(8,5))
plt.bar(df.index, df["Total"], color="skyblue")
plt.title("Total Marks of Students")
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
