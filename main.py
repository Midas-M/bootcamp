import pandas as pd
import plotly.express as px

def main():

    print('test')
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
fig.show()

if __name__ == "__main__":
    main()
