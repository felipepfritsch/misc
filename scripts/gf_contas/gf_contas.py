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
name_map = {'L': 'laura',
            'I': 'itunes',
            'F': 'felipe',
            'M': 'fafa',
            'UB': 'uber',
            'U': 'unknown'}
init_df['person'] = init_df['person'].map(name_map)
init_df['expense_type'] = init_df['expense_type'].apply(lambda x: x.lower())

df = init_df


# Analise
include_uber = False
df = df if include_uber else df.loc[df['gasto'] != 'Uber']
total_pp = df.groupby('pessoa').apply(lambda x: x['valor'].sum())

felipe_df = df.loc[df['pessoa'] == 'Felipe']
felipe_df.groupby('gasto')['valor'].sum()
