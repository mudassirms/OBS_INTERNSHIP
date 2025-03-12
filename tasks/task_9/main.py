import pandas as pd
import numpy as np

# Sample data with string numbers, missing values, and duplicates
data = {
    'Player': ['Danial', 'Saam', 'Karthik', 'Danial', 'hawa', 'Saam', 'krish'],
    'Score': ['85', '90', np.nan, '85', '88', '90', '92']
}

df = pd.DataFrame(data)

df['Score'] = pd.to_numeric(df['Score'], errors='coerce')
df['Score'] = df['Score'].fillna(df['Score'].mean())

df = df.drop_duplicates(subset=['Player'], keep='first')

df = df.sort_values(by='Score', ascending=False)

df = df.reset_index(drop=True)

print(df)
