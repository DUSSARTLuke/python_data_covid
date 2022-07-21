import pandas as pd
import matplotlib.pyplot as plt

col_list = ['date','lib_dep','tx_pos','tx_incid','TO','R','hosp','rea','rad','reg_rea','incid_hosp','incid_rea','incid_rad','incid_dchosp','reg_incid_rea','pos']

df = pd.read_csv('table-indicateurs-open-data-dep-2022-07-19-19h00.csv', sep=',', usecols=col_list, encoding='utf-8')
tab_herault = df.loc[(df["date"]>"2021-12-31") & (df["date"]<"2022-07-17") & (df["lib_dep"] == "Hérault"),:]
tab_finistere = df.loc[(df["date"]>"2021-12-31") & (df["date"]<"2022-07-17") & (df["lib_dep"]=="Finistère"),:]

xHerault = pd.to_datetime(pd.Series(tab_herault.date))
xFinistere = pd.to_datetime(pd.Series(tab_finistere.date))
print(xHerault)

plt.scatter(xHerault,tab_herault.tx_incid, c="red", s=2, label="Hérault")
plt.scatter(xFinistere,tab_finistere.tx_incid, c="black", s=2, label="Finistère")
plt.title("Taux d'incidence en ‰ dans l'Hérault et le Finistère par jour")
plt.xlabel('Date du jour')
plt.ylabel("Taux d'incidence en ‰")
plt.legend()
plt.show()

y1H = tab_herault.rea
y2H = tab_herault.hosp

y1F = tab_finistere.rea
y2F = tab_finistere.hosp


fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True)
fig.suptitle("Nombre de patients en réanimation et hospitalisés dans le Finistère")
#fig.suptitle('Horizontally stacked subplots')
ax1.bar(xHerault, y2H, width= 0.8, color= "#EDFF91", label="Nombre de patients en réanimation ou en soins intensifs")
ax1.bar(xHerault, y1H, width = 0.8, color = "#3ED8C9", label="Nombre de patients hospitalisés pour COVID-19")
plt.ylabel("Nb Réanimation et Nb Hospitalisation")
plt.xlabel('Date du jour')
ax2.bar(xFinistere, y2F, width= 0.8, color= "#EDFF91", label="Nombre de patients en réanimation ou en soins intensifs")
ax2.bar(xFinistere, y1F, width = 0.8, color = "#3ED8C9", label="Nombre de patients hospitalisés pour COVID-19")
plt.ylabel("Nb Réanimation et Nb Hospitalisation")
plt.xlabel('Date du jour')


plt.legend()
plt.show()
