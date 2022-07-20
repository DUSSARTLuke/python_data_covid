import pandas as pd



col_list = ['dep','date','reg','lib_dep','lib_reg','tx_pos','tx_incid','TO','R','hosp','rea','rad','dchosp','reg_rea','incid_hosp','incid_rea','incid_rad','incid_dchosp','reg_incid_rea','pos','pos_7j','cv_dose1']

df = pd.read_csv('table-indicateurs-open-data-dep-2022-07-19-19h00.csv', sep=',', usecols=col_list, encoding='latin-1')



print('Nombre d éléves :', (df['dep']))
