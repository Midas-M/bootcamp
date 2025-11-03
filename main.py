
import pandas as pd
import plotly.express as px

def main():
    data_path = "sample_data/students.csv"
    df = pd.read_csv(data_path)

    print("Student grade data:")
    print(df.to_string(index=False))

    # Show descriptive statistics for the grade distribution
    stats = df["grade"].describe()
    print("\nGrade statistics:")
    print(stats.to_string())

    # New code: Plotly visualization
    fig = px.bar(
        df,
        x="name",
        y="grade",
        color="section",
        title="Student Grades by Section",
        hover_data=["section", "grade"]
    )

    # Calculate and show average grade per section
    avg = df.groupby("section")["grade"].mean()
    print("\nAverage grade by section:")
    print(avg)

    fig.show()

if __name__ == "__main__":
    main()