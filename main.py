import pandas as pd
import matplotlib.pyplot as plt

col_list = ['date','lib_dep','tx_pos','tx_incid','TO','R','hosp','rea','rad','reg_rea','incid_hosp','incid_rea','incid_rad','incid_dchosp','reg_incid_rea','pos']

df = pd.read_csv('table-indicateurs-open-data-dep-2022-07-19-19h00.csv', sep=',', usecols=col_list, encoding='utf-8')
tab_herault = df.loc[(df["date"]>"2021-12-31") & (df["date"]<"2022-07-17") & (df["lib_dep"] == "Hérault"),:]
print('Hérault :', tab_herault)

tab_finistere = df.loc[(df["date"]>"2021-12-31") & (df["date"]<"2022-07-17") & (df["lib_dep"]=="Finistère"),:]
print('Finistère :', tab_finistere)

plt.scatter(tab_herault.date,tab_herault.tx_incid, c="red", s=2)
plt.title("Taux d'incidence en % dans l'HERAULT par jour")
plt.xlabel('Date du jour')
plt.ylabel("Taux d'incidence en %")
plt.show()

plt.scatter(tab_finistere.date,tab_finistere.tx_incid, c="green", s=2)
plt.title("Taux d'incidence en % dans le FINISTERE par jour")
plt.xlabel('Date du jour')
plt.ylabel("Taux d'incidence en %")
plt.show()