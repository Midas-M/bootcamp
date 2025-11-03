import pandas as pd
import plotly.express as px

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
    for _, row in avg.iterrows():
        fig.add_hline(
            y=row["grade"],
            line_dash="dash",
            annotation_text=f"{row['section']} avg: {row['grade']:.1f}",
            annotation_position="top left"
        )
    fig.show()

if __name__ == "__main__":
    main()

