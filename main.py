import pandas as pd
import functions

def main():
    df = pd.read_csv("./data/raw/dataset.csv")

    formatters = [
        functions.format_employee_residence,
        functions.format_employment_type,
        functions.format_job_title,
        functions.format_job_category,
    ]
    for formatter in formatters:
        print(f"Running {formatter.__name__}... ", end="")
        df = formatter(df)
        print(f"Done ✅")

    columns = ["employee_residence", "work_setting", "employment_type", "job_title", "job_category"]
    for column in columns:
        print(f"Saving {column}... ", end="")
        functions.save_unique_values(df, column, column + ".csv")
        print(f"Done ✅")

if __name__ == "__main__":
    main()
