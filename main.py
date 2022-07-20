import pandas as pd

col_list = ['date','lib_dep','tx_pos','tx_incid','TO','R','hosp','rea','rad','reg_rea','incid_hosp','incid_rea','incid_rad','incid_dchosp','reg_incid_rea','pos']

df = pd.read_csv('table-indicateurs-open-data-dep-2022-07-19-19h00.csv', sep=',', usecols=col_list, encoding='utf-8')
tab_herault = df.loc[(df["date"]>"2021-12-31") & (df["lib_dep"] == "Hérault"),:]
print('Hérault :', tab_herault)

tab_finistere = df.loc[(df["date"]>"2021-12-31") & (df["lib_dep"]=="Finistère"),:]
print('Finistère :', tab_finistere)