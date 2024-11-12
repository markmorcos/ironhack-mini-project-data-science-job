import pandas as pd

def format_job_title(df, column_name="job_title"):
    df_copy = df.copy()
    def clean_title(title):
        if title.startswith("Machine Learning"): return "Machine Learning"
        if title.startswith("Statistician"): return "Statistician"
        if title.startswith("Data Scientist"): return "Data Scientist"
        return "Data Analyst"
    
    df_copy[column_name] = df_copy[column_name].apply(clean_title)
    return df_copy


def format_job_category(df, column_name="job_category"):
    df_copy = df.copy()
    def fill_job_category(row):
        job_category_dict = df_copy.dropna(subset=[column_name]).set_index("job_title")[column_name].to_dict()
        if pd.isnull(row[column_name]) and row["job_title"] in job_category_dict: return job_category_dict[row["job_title"]]
        else: return row[column_name]
    df_copy[column_name] = df_copy.apply(fill_job_category, axis=1)
    return df_copy

def format_employment_type(df):
    df_copy = df.copy()
    df_copy["employment_type"] = df_copy["employment_type"].replace({ "CT": "Contract", "FL": "Freelance", "FT": "Full-Time", "PT": "Part-Time" })
    return df_copy

def format_experiences_level(df):
    df_copy = df.copy()
    df_copy["experience_level"] = df_copy["experience_level"].fillna("Not provided")
    df_copy["experience_level"] = df_copy["experience_level"].replace({"MI": "Mid-level", "SE": "Senior-level", "EN": "Entry-level", "EX": "Executive-level"})
    return df_copy


def format_employee_residency(df, column_name="employee_residence"):
    df_copy = df.copy()
    df_copy[column_name] = df_copy[column_name].replace({ "US": "United States", "JP": "Japan", "UK": "United Kingdom", "DE": "Germany", "CN": "China", "MX": "Mexico", "IN": "India" })
    return df_copy
    