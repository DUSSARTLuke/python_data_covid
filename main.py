import pandas as pd
import matplotlib.pyplot as plt

col_list = ['date','lib_dep','tx_pos','tx_incid','TO','R','hosp','rea','rad','reg_rea','incid_hosp','incid_rea','incid_rad','incid_dchosp','reg_incid_rea','pos']

df = pd.read_csv('table-indicateurs-open-data-dep-2022-07-19-19h00.csv', sep=',', usecols=col_list, encoding='utf-8')
tab_herault = df.loc[(df["date"]>"2021-12-31") & (df["date"]<"2022-07-17") & (df["lib_dep"] == "Hérault"),:]
tab_finistere = df.loc[(df["date"]>"2021-12-31") & (df["date"]<"2022-07-17") & (df["lib_dep"]=="Finistère"),:]

plt.scatter(tab_herault.date,tab_herault.tx_incid, c="red", s=2, label="Hérault")
plt.scatter(tab_finistere.date,tab_finistere.tx_incid, c="black", s=2, label="Finistère")
plt.title("Taux d'incidence en ‰ dans l'Hérault et le Finistère par jour")
plt.xlabel('Date du jour')
plt.ylabel("Taux d'incidence en ‰")
plt.legend()
plt.show()


x = tab_herault.date
y1 = tab_herault.rea
y2 = tab_herault.hosp

plt.bar(x, y2, width= 0.8, color= "#EDFF91")
plt.bar(x, y1, width = 0.8, color = "#3ED8C9")
plt.title('HERAULT')
plt.xlabel('Date du jour')
plt.ylabel("Nb Réanimation et Nb Hospitalisation")
plt.show()

y1 = tab_finistere.rea
y2 = tab_finistere.hosp

plt.bar(x, y2, width= 0.8, color= "#EDFF91")
plt.bar(x, y1, width = 0.8, color = "#3ED8C9")
plt.title('FINISTERE')
plt.ylabel("Nb Réanimation et Nb Hospitalisation")
plt.xlabel('Date du jour')
plt.show()