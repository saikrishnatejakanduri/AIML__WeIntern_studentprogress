"""Small reusable helpers for the WeIntern Week 1 student analysis."""
import pandas as pd

def normalize_gender(value):
    """Map common gender spellings/abbreviations to consistent labels."""
    if pd.isna(value):
        return "Unknown"
    x = str(value).strip().lower()
    mapping = {
        "m": "Male", "male": "Male", "man": "Male",
        "f": "Female", "female": "Female", "woman": "Female",
        "other": "Other", "prefer not to say": "Prefer not to say",
        "unknown": "Unknown", "": "Unknown"
    }
    return mapping.get(x, x.title() if x else "Unknown")

def normalize_yes_no(value):
    """Standardize common yes/no values without inventing missing answers."""
    if pd.isna(value):
        return "Unknown"
    x = str(value).strip().lower()
    if x in {"yes", "y", "1", "true"}:
        return "Yes"
    if x in {"no", "n", "0", "false"}:
        return "No"
    if x in {"", "unknown", "none", "nan"}:
        return "Unknown"
    return x.title()

def normalize_parental_education(value):
    """Normalize parental education labels to a controlled set."""
    if pd.isna(value):
        return "Unknown"
    x = str(value).strip().lower().replace("’", "'")
    mapping = {
        "high school": "High School", "highschool": "High School",
        "bachelor": "Bachelor's", "bachelors": "Bachelor's",
        "bachelor's": "Bachelor's", "master": "Master's",
        "masters": "Master's", "master's": "Master's",
        "doctorate": "Doctorate", "phd": "Doctorate", "other": "Other",
        "unknown": "Unknown", "": "Unknown"
    }
    return mapping.get(x, x.title() if x else "Unknown")

def set_out_of_range_to_missing(frame, limits):
    """Return a copy with values outside inclusive (minimum, maximum) bounds set to NaN."""
    result = frame.copy()
    flagged = {}
    for column, (minimum, maximum) in limits.items():
        if column not in result.columns:
            continue
        out_of_range = result[column].notna() & ~result[column].between(minimum, maximum)
        flagged[column] = int(out_of_range.sum())
        result.loc[out_of_range, column] = pd.NA
    return result, flagged
