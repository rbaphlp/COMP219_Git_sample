import pandas as pd
import csv


csvfile = "job_data.csv"

def average_salaries(csvfile, job_titles):
        df = pd.read_csv(csvfile)
        updated_df = df[df['job_title'].isin(job_titles)]
        average_salaries = updated_df.groupby('job_title')['num_of_salaries'].mean()
        return average_salaries

job_titles = ["Data Architect","Senior Business Analyst","Data Scientist","Machine Learning Engineer"]

average_salaries_result = average_salaries(csvfile,job_titles)

print(average_salaries_result)

