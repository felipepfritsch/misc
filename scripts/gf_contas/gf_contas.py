import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import gf_contas.aux_gf_contas as agc

file_dir = r"C:\users\felip\python\input"
file_name = 'gf_contas.xlsx'
file_path = file_dir + '\\' + file_name
init_df = pd.read_excel(file_path)

# Reformatting data
name_map = {'L': 'Laura', 'I': 'Itunes', 'F': 'Felipe',
            'M': 'Fafa', 'G': 'Gabriel', 'UB': 'Uber',
            'UN': 'Unknown'}
init_df['person'] = init_df['person'].map(name_map)
final_df = init_df

agc.export_all_to_excel(final_df)
print('Done')