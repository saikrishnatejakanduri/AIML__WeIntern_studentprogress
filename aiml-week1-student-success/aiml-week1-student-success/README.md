# Student Success Signals: A Data Quality & Learning Habits Audit

**WeIntern AIML Internship - Week 1 assignment**

## Overview
This beginner-friendly analytics project studies how attendance, study time, assignment scores, midterm scores, and student context fields relate to final marks. It completes the three handbook tasks: (1) Student Performance Dataset Analysis, (2) Data Visualization, and (3) Business Insight Report.

> **Important data note:** The included dataset is synthetic and generated for this assignment. It contains no real student records. The raw CSV deliberately includes missing values, exact duplicate rows, inconsistent category labels, and out-of-range numeric values to demonstrate a documented cleaning process. Numerical findings are examples from this simulated data only, not claims about real students.

## Dataset
- File: `data/raw/student_performance_raw.csv`
- Cleaned output: `data/cleaned/student_performance_cleaned.csv`
- Rows/columns in the raw data: inspect using the notebook; 12 exact duplicate rows are intentionally included.
- Columns: Student ID, gender, age, attendance percentage, study hours per week, assignment score, midterm score, final score, parental education, internet access, and extra activities.
- Dataset source: generated locally with NumPy for practice; no external dataset source is claimed.

## Work completed
1. Load and inspect first/last rows, shape, dtypes, nulls, and duplicates.
2. Provide a feature-understanding table.
3. Remove exact duplicates; normalize categorical labels; coerce numeric fields; flag out-of-range values; fill numeric predictor gaps with medians; retain missing categories as `Unknown`; remove rows without a valid final score rather than inventing a target.
4. Save a separate cleaned CSV and before/after quality reports.
5. Generate descriptive statistics, categorical summaries, and a numeric correlation matrix.
6. Create distribution, category comparison, relationship, box, attendance, and correlation heatmap charts with interpretations.
7. Write eight evidence-based observations and cautious, human-led recommendations.
8. Produce a business insight report in Markdown and PDF.

## Libraries
NumPy, Pandas, Matplotlib, Seaborn, Jupyter Notebook, and ReportLab (for the PDF report).

## Repository structure
```text
aiml-week1-student-success/
├── data/
│   ├── raw/student_performance_raw.csv
│   └── cleaned/student_performance_cleaned.csv
├── notebooks/week1_analysis.ipynb
├── outputs/
│   ├── charts/
│   ├── tables/
│   └── reports/
├── screenshots/
├── src/helper_scripts.py
├── README.md
├── GITHUB_UPLOAD_GUIDE.md
└── requirements.txt
```

## Run the project
### Option A: Jupyter locally
1. Install Python 3.10+.
2. Open a terminal in this repository folder.
3. (Recommended) Create and activate a virtual environment.
4. Install dependencies: `pip install -r requirements.txt`
5. Start Jupyter: `jupyter notebook`
6. Open `notebooks/week1_analysis.ipynb` and run all cells from top to bottom.

The notebook is written to locate the project root whether Jupyter starts from the repository root or the `notebooks/` folder. It saves charts and tables into `outputs/`.

### Option B: Google Colab
Upload the notebook and data folders while preserving the same folder structure, or upload the full ZIP to Drive and extract it. Run cells top to bottom after ensuring the `data/` and `src/` folders are alongside the notebook's project root.

## Outputs to review
- `outputs/tables/feature_understanding.csv`
- `outputs/tables/missing_values_before.csv` and `missing_values_after.csv`
- `outputs/tables/cleaning_summary.csv`
- `outputs/tables/descriptive_statistics.csv`
- `outputs/tables/correlation_matrix.csv`
- `outputs/tables/key_observations.txt`
- `outputs/charts/` (saved charts)
- `outputs/reports/business_insight_report.pdf` and `.md`

## Ethical and analytical limits
This is an educational demonstration, not a grade prediction or real-world student surveillance tool. Correlation is not causation. A real deployment would require validated real data, privacy safeguards, educator oversight, and fairness checks.

## Author
Prepared as a Week 1 AIML internship practice project. Add your preferred name and GitHub profile before publishing.
