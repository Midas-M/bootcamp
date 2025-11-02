# Assignment: Enhanced Student Grade Visualization

1. Fork and clone this repository to your local machine. Create a feature branch for your work.
2. Improve the student grade visualization in `main.py` or a new module. Use Plotly to produce a richer chart than the current bar graph. Feel free to experiment with colors, annotations, interactivity, or additional summary visuals.
   ```python
   import plotly.express as px

   fig = px.bar(df, x="name", y="grade")
   fig.show()
   ```
3. Commit your changes, push your feature branch, and open a pull request targeting the `main` branch.
4. In the PR description, briefly explain your visualization choices and any new instructions for running the project.

Helpful resources:
- Plotly Express documentation: https://plotly.com/python/plotly-express/
