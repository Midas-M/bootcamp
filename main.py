
import pandas as pd
import plotly.express as px


df = pd.read_csv("sample_data/students.csv")


fig = px.bar(
    df,
    x="name",
    y="grade",
    color="section",
    title="Student Grades by Section",
    barmode="group"
)

fig.show()


avg = df.groupby("section")["grade"].mean()
print("Average grade per section:")
print(avg)
