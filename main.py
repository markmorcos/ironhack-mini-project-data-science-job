import pandas as pd
import functions

def main():
    df = pd.read_csv("./data/raw/dataset.csv")

    formatters = [
        functions.format_company_location,
        functions.format_employee_residence,
        functions.format_employment_type,
        functions.format_job_title,
        functions.format_job_category,
    ]
    for formatter in formatters:
        print(f"Running {formatter.__name__}... ", end="")
        df = formatter(df)
        print(f"Done ✅")

    tables = {
        "employee_residence": "country",
        "work_setting": "work_setting",
        "employment_type": "employee_type",
        "job_title": "job_title",
        "job_category": "job_category",
    }
    for column, table in tables.items():
        print(f"Saving {table}... ", end="")
        functions.save_unique_values(df, column, table)
        print(f"Done ✅")

    print("Saving job table... ", end="")
    functions.save_job_table(df)
    print("Done ✅")

    print("All done! 🎉")

if __name__ == "__main__":
    main()
