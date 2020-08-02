# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 12:04:23 2020

@author: Sashank
"""

import pandas as pd

df = pd.read_csv(r"glassdoor_jobs.csv")

#salary parsing


df = df[df['Salary Estimate'] != '-1']

salary = df['Salary Estimate'].apply(lambda x :  x.split('(')[0])
minus_kd = salary.apply(lambda x : x.replace('K','').replace('$',''))

df['hour'] = salary.apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['EMP prov salary'] = salary.apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)

min_hr = minus_kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary','').replace(':',''))
df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))


df['avg_salary'] = (df.min_salary + df.max_salary)/2

#Company name text only
df['Company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis=1)

#state field
df['State'] = df['Location'].apply(lambda x: x.split(',')[1])

df['same_state'] = df.apply(lambda x: 1 if x['Location'] == x['Headquarters'] else 0 , axis = 1)

#age of company
df['age'] = df['Founded'].apply(lambda x : int(2020 - x) if x > 0 else -1)

#parsing of job description
#python
df['python_job'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python_job.value_counts()

#R
df['R_job'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() else 0)
df.R_job.value_counts()
#spark
df['spark_job'] = df['Job Description'].apply(lambda x : 1 if 'spark' in x.lower() else 0)
df.spark_job.value_counts()

#aws
df['aws_job'] = df['Job Description'].apply(lambda x : 1 if 'aws' in x.lower() or 'amazon web services' in x.lower() else 0)
df.aws_job.value_counts()

#excel
df['excel_job'] = df['Job Description'].apply(lambda x : 1 if 'excel' in x.lower() else 0)
df.excel_job.value_counts()

df_out = df.drop(['Unnamed: 0'], axis = 1)

df_out.to_csv('job_data_cleaned.csv', index = False)
