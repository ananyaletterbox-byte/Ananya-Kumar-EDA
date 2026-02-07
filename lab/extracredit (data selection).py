#ChatGPT was used as a guide in this assignment
#worked with Jaitha Jasti

import os
import pandas as pd
import numpy as np
import pyarrow

var_list = ['year', 'marital', 'reliten', 'happy', 'age']
output_dir = '/Users/ananyakumar/Downloads'
os.makedirs(output_dir, exist_ok=True)

output_filename = os.path.join(output_dir, 'selected_gss_data.csv')


phase = 0

for k in range(3):
    url = (
        'https://github.com/DS3001/project_gss/raw/main/'
        f'gss_chunk_{k+1}.parquet'
    )
    print(f"Loading chunk {k+1}...")
    
    df = pd.read_parquet(url)
    
    # Replace GSS missing codes
    df.replace([-9, -8, -7, -6, -5], np.nan, inplace=True)
    
    # Restrict to adults
    df = df[(df['age'] >= 18) & (df['age'] <= 89)]
    
    if phase == 0:
        df[var_list].to_csv(
            output_filename,
            mode='w',
            header=True,
            index=False
        )
        phase = 1
    else:
        df[var_list].to_csv(
            output_filename,
            mode='a',
            header=False,
            index=False
        )

print("Done! File saved.")


'''
1. Data Selection and Description
- For this analysis, we selected five variables from the General Social Survey (GSS) dataset:
 a. Year (year): The survey year lets us consider potential changes over time, but for this analysis we did aggregate trends instead han year-specific effects.
b. Marital Status (marital): This categorizes respondents as married, never married, divorced, separated, or widowed; used to explore the relationship between marital status and general happiness.
c. Religious Intensity (reliten): This measures the strength of religious identification from “no religion,” “not very strong,” “somewhat strong,” and “strong.” We used this to see how religiosity correlates with happiness.
d. Happiness (happy): Here, respondents rate their general happiness as “not too happy,” “pretty happy,” or “very happy.” This is the most important dependent variable in the analysis.
e. Age (age): Respondent’s age; we used this as a control for life-cycle effects and then explore trends in happiness from different stages of life.
These variables were chosen because we can thus form understandings on personal and social factors—marital status, religious involvement, and age—relate to general happiness, which is a very interesting conversation to be had!
'''