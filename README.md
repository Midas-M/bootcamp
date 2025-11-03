# bootcamp
An educational purposes repo

## Student grades demo
This project includes a small dataset (`students.csv`) with 10 students and their grades, plus a script that loads the data with pandas and prints descriptive statistics.

### Setup
1. Create and activate a Python 3.12 virtual environment.
2. Install dependencies (declared in `pyproject.toml`):
   ```bash
   uv sync
   ```

### Usage
Run the entry script to inspect the dataset:
```bash
python main.py
```
The script prints the student table followed by summary statistics (count, mean, min, quartiles, max) for the `grade` column.
