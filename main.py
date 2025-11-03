import pandas as pd
import plotly.express as px
 fatma-assignment


df = pd.read_csv("sample_data/students.csv")


fig = px.bar(
    df,
    x="name",
    y="grade",
    color="section",
    title="Student Grades by Section",
    barmode="group"
)



def main():
    data_path = "sample_data/students.csv"
    df = pd.read_csv(data_path)
    print("Student Grades:")
    print(df)
avg = df.groupby("section")["grade"].mean().reset_index()
print("\nAverage grade per section:")
print(avg)
fig = px.bar(
        df,
        x="name",
        y="grade",
        color="section",
        title="Student Grades by Section"
    )
 main
fig.show()


avg = df.groupby("section")["grade"].mean()
print("Average grade per section:")
print(avg)
