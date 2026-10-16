# Student Success Signals: A Data Quality & Learning Habits Audit

**WeIntern AIML Internship | Week 1 Business Insight Report**

> **Data transparency:** The dataset is simulated for education and practice. It does not represent real students. Results below are descriptive of this generated sample only.

## 1. Project Context
This project explores how attendance, study time, assignment scores, and midterm scores are associated with final academic scores. It demonstrates the Week 1 workflow: inspect and clean a tabular dataset, perform descriptive analysis, visualize patterns, and translate observations into cautious recommendations. No predictive model is built.

## 2. Objective
- Assess the distribution of final scores.
- Explore numeric relationships with final scores.
- Review data quality and category representation.
- Produce practical support ideas that would need validation on real data.

## 3. Dataset Summary
| Metric | Result |
|---|---:|
| Raw records | 1,212 |
| Columns | 11 |
| Exact duplicates removed | 12 |
| Rows excluded due to missing/invalid final score | 17 |
| Final cleaned records | 1,183 |
| Final score mean | 76.2/100 |
| Final score median | 77.2/100 |
| Final score standard deviation | 11.8 |

Fields include student ID, gender, age, attendance percentage, study hours per week, assignment score, midterm score, final score, parental education, internet access, and extra activities. The dataset is synthetic and was generated locally for this assignment.

## 4. Analysis Approach
1. Inspected data shape, column types, missing values, and exact duplicates.
2. Normalized inconsistent categories and checked numeric ranges.
3. Set invalid numeric values to missing; used median imputation for numeric predictors; retained missing categories as `Unknown`; excluded rows without a valid final score instead of inventing an outcome.
4. Computed descriptive statistics, category counts, and Pearson correlations.
5. Created distribution, count, scatter, box, attendance relationship, and correlation heatmap figures.

## 5. Key Findings
1. The cleaned dataset contains 1,183 records. Final scores average 76.2/100 (median 77.2; standard deviation 11.8).
2. Study hours and final score have a Pearson correlation of r = 0.51, a positive linear association in this simulated sample.
3. Attendance and final score have a Pearson correlation of r = 0.43; this is descriptive and does not show that attendance alone causes a score change.
4. Assignment score and final score have a Pearson correlation of r = 0.70.
5. Midterm score and final score have a Pearson correlation of r = 0.74.
6. 23.3% of cleaned records have attendance below 75%; this threshold is an illustrative monitoring flag, not a validated intervention cut-off.
7. 1.7% of cleaned records have final scores below 50/100; these records could be reviewed as a group in a real pilot, with safeguards and context.
8. 1.6% of records have internet access recorded as Unknown after cleaning, indicating a need to improve response completeness.

## 6. Recommendations
1. Pilot an early-support review for students with repeated low attendance or falling assessment scores; use human review rather than an automated label.
2. Offer study-planning resources and optional tutoring to students who request help, then evaluate whether the support improves outcomes.
3. Use assignment and midterm performance as discussion prompts for teachers, while considering course difficulty and grading differences.
4. Improve completeness of fields such as internet access and parental education, and document why each field is collected.
5. Validate the patterns on a real, representative dataset and examine differences across groups before adopting thresholds or interventions.

## 7. Limitations
- The dataset is simulated. None of the numeric findings should be generalized to a real school.
- Correlation does not establish causation; other variables may contribute to observed relationships.
- Median imputation is a simple demonstration and can affect distributions. Imputed values should be tracked and sensitivity-checked in real work.
- The report does not establish any threshold as a validated early-warning rule.
- Real student data requires privacy safeguards, appropriate consent, restricted access, fairness checks, and educator oversight.

## 8. Conclusion
The sample demonstrates that assignment and midterm scores have stronger linear associations with final scores than study hours or attendance in this simulated data. That is expected in part because the score fields are related by the synthetic data generator. The practical output is the documented data workflow and reporting structure, not a claim about actual student performance. Before acting on these ideas, validate them using representative real data and discuss them with educators.

## Included visuals
See `outputs/charts/` for labeled figures and `outputs/tables/` for reproducible summary tables.
