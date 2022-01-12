import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_dir = r"C:\users\felip\python\input"
file_name = 'gf_contas.xlsx'
file_path = file_dir + '\\' + file_name
init_df = pd.read_excel(file_path)

# Reformatting data
name_map = {'L': 'Laura', 'I': 'Itunes', 'F': 'Felipe',
            'M': 'Fafa', 'G': 'Gabriel', 'UB': 'Uber',
            'UN': 'Unknown'}
init_df['person'] = init_df['person'].map(name_map)
df = init_df

# Analise
include_uber = True
df = df if include_uber else df.loc[df['person'] != 'Uber']
total_pp = df.groupby('person').apply(lambda x: x['value'].sum())

felipe_df = df.loc[df['person'] == 'Felipe']
felipe_df.groupby('expense_type')['value'].sum()
