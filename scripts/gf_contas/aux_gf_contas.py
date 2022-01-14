import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_dir = r"C:\users\felip\python\input"
file_name = 'gf_contas.xlsx'
file_path = file_dir + '\\' + file_name
output_path = file_dir.replace('input', 'output')


def get_all_transactions_pp(df):
    out = {}
    for p in df['person'].unique():
        out[p] = df.loc[df['person'] == p].drop('person', axis=1).set_index('date')
    return out


def get_total_pp(df):
    out = df.groupby('person').apply(lambda x: x['value'].sum())
    return out


def get_total_pp_breakdown(df):
    tmp = df.groupby('person').apply(lambda x: x.groupby('expense_type')['value'].sum())
    out = tmp.reset_index().pivot_table(values='value', index='expense_type', columns='person')
    return out.fillna(0.0)


def get_timeseries_pp(df):
    tmp = df.groupby(['person', 'date']).apply(lambda x: x['value'].sum())
    out = tmp.reset_index().pivot_table(values=0, index='date', columns='person').fillna(0.0)
    return out


def get_timeseries_pp_split(df):
    tmp = get_all_transactions_pp(df)
    out = {}
    for p, data in tmp.items():
        out[p] = data.groupby(['date', 'expense_type'])['value'].sum()
    return pd.DataFrame(out).fillna(0.0)


def export_all_to_excel(df, f_name='analise_contas.xlsx', path=output_path):
    f_name = f_name if '.xlsx' in f_name else f_name + '.xlsx'
    with pd.ExcelWriter(path + '\\' + f_name, engine='xlsxwriter') as writer:
        # Summary sheet
        sheet_1 = 'Summary'
        total_pp = get_total_pp(df)
        total_pp_breakdown = get_total_pp_breakdown(df)
        total_pp.to_excel(writer,
                          sheet_name=sheet_1,
                          startcol=1,
                          startrow=1)
        total_pp_breakdown.to_excel(writer,
                                    sheet_name=sheet_1,
                                    startcol=total_pp.to_frame().shape[1] + 3,
                                    startrow=1)

        # Time-series sheet
        sheet_2 = 'TimeSeries Analysis'
        ts_basic = get_timeseries_pp(df)
        ts_basic_breakdown = get_timeseries_pp_split(df)
        ts_basic.to_excel(writer,
                          sheet_name=sheet_2,
                          startcol=1,
                          startrow=1)
        ts_basic_breakdown.to_excel(writer,
                                    sheet_name=sheet_2,
                                    startcol=ts_basic.shape[1] + 3,
                                    startrow=1)

        # All transactions by person
        sheet_3 = 'All_'
        all_data_pp = get_all_transactions_pp(df)
        for p, data in all_data_pp.items():
            data.to_excel(writer,
                          sheet_name=sheet_3 + p,
                          startcol=1,
                          startrow=1)

    return None
