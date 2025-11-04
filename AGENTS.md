# Repository Guidelines

## Project Structure & Module Organization
`main.py` is the entry point; keep new analysis helpers close to the `main()` function or break them into purpose-driven modules under a future `src/` package if the script grows. Dataset samples live in `sample_data/` (currently `students.csv`), so stage replacement files there and reference them with relative paths. Project metadata and dependencies are managed via `pyproject.toml`, while repo-level context lives in `README.md` and `assignment.md`; update them whenever behavior changes.

## Build, Test, and Development Commands
- `uv sync` — install or update the Python 3.12 environment defined in `pyproject.toml`.
- `uv run python main.py` — execute the grade summary workflow inside the managed environment.
- `python main.py` — quick ad-hoc run when the environment is already activated manually.

## Coding Style & Naming Conventions
Follow PEP 8 with 4-space indentation, snake_case names for functions and variables (e.g. `compute_section_average`), and PascalCase only for classes. Prefer pandas-friendly vectorized operations over Python loops. 
Annotate new functions with type hints and include short docstrings describing inputs and outputs. 
Keep Plotly figure IDs descriptive (e.g. `section_grade_fig`) and reuse constants for shared column names to avoid typos.

## Testing Guidelines
No automated suite exists yet, so contributions should introduce `pytest` tests alongside new logic. Name new tests `test_<feature>.py` under a `tests/` folder and mirror the data-driven scenarios found in `sample_data/`. Until pytest is in place, validate changes by running `uv run python main.py` and confirming the printed table, summary statistics, and rendered bar chart. Share console snippets or screenshots when behavior changes.

## Commit & Pull Request Guidelines
Recent history favors short, descriptive commit titles (e.g. `Add grade visualization`); keep messages under 72 characters and write them in the imperative mood. Group related edits per commit, and note data updates explicitly. Pull requests should include: a concise summary, testing notes (`uv run python main.py` output or pytest results), linked issue IDs when available, and screenshots of visual changes.

## Data & Visualization Tips
Treat `sample_data/students.csv` as canonical demo data—retain its headers (`name`, `section`, `grade`) and document any schema changes in the PR. When adding plots, prefer `px.bar`/`px.scatter` for quick insight and call `fig.write_image` only behind a flag to keep CI deterministic. Consider gating interactive calls (`fig.show()`) so automated runs can disable them via an environment variable.
