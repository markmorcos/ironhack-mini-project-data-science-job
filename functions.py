import pandas as pd

def format_job_title(df, column_name="job_title"):
    df_copy = df.copy()
    def clean_title(title):
        if title.startswith("Machine Learning Engineer"): return "Machine Learning Engineer"
        if title.startswith("Statistician"): return "Statistician"
        if title.startswith("Data Scientist"): return "Data Scientist"
        return "Data Analyst"
    
    df_copy[column_name] = df_copy[column_name].apply(clean_title)
    return df_copy


def format_job_category(df, column_name="job_category"):
    df_copy = df.copy()
    job_category_dict = df_copy.dropna(subset=[column_name]).set_index("job_title")[column_name].to_dict()
    def fill_job_category(row):
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


def format_company_location(df, column_name="company_location"):
    df_copy = df.copy()
    df_copy[column_name] = df_copy[column_name].replace({ "US": "United States", "JP": "Japan", "UK": "United Kingdom", "DE": "Germany", "CN": "China", "MX": "Mexico", "IN": "India" })
    return df_copy
    
def format_employee_residence(df, column_name="employee_residence"):
    df_copy = df.copy()
    df_copy[column_name] = df_copy[column_name].replace({ "US": "United States", "JP": "Japan", "UK": "United Kingdom", "DE": "Germany", "CN": "China", "MX": "Mexico", "IN": "India" })
    return df_copy
    
def save_unique_values(df, column_name, file_name):
    unique_values = pd.DataFrame(df[column_name].unique(), columns=["name"])
    unique_values.index += 1
    unique_values.index.name = "id"
    unique_values.reset_index(inplace=True)
    unique_values.to_csv(f"./data/clean/{file_name}.csv", index=False)

def get_id_from_value(table):
    df = pd.read_csv(f"./data/clean/{table}.csv")
    df_map = { row["name"]: row["id"] for _, row in df.iterrows() }
    def get_id_from_table(value):
        return df_map.get(value)
    return get_id_from_table

def save_job_table(df, file_name="job"):
    df_copy = df[["salary_in_usd"]].copy()
  
    mappers = {
        "company_location_id": ("company_location", get_id_from_value("country")),
        "employee_residence_id": ("employee_residence", get_id_from_value("country")),
        "work_setting_id": ("work_setting", get_id_from_value("work_setting")),
        "employment_type_id": ("employment_type", get_id_from_value("employee_type")),
        "job_title_id": ("job_title", get_id_from_value("job_title")),
        "job_category_id": ("job_category", get_id_from_value("job_category")),
    }
    for column, (table, mapper) in mappers.items():
        df_copy[column] = df[table].apply(mapper)

    df_copy.index += 1
    df_copy.index.name = "id"
    df_copy.reset_index(inplace=True)
    df_copy.to_csv(f"./data/clean/{file_name}.csv", index=False)

    return df_copy