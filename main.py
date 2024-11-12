import pandas as pd
import functions

def main():
    df = pd.read_csv("dataset.csv")

    df = functions.format_job_title(df)
    df = functions.format_job_category(df)
    df = functions.format_employment_type(df)
    df = functions.format_experiences_level(df)
    df = functions.format_employee_residency(df)

    print(df.head())

if __name__ == "__main__":
    main()
