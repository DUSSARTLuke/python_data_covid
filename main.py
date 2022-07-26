import pandas as pd
import matplotlib.pyplot as plt

col_list = ['date','lib_dep','tx_pos','tx_incid','TO','R','hosp','rea','rad','reg_rea','incid_hosp','incid_rea','incid_rad','incid_dchosp','reg_incid_rea','pos']

df = pd.read_csv('table-indicateurs-open-data-dep-2022-07-19-19h00.csv', sep=',', usecols=col_list, encoding='utf-8')
tab_herault = df.loc[(df["date"]>"2021-12-31") & (df["date"]<"2022-07-17") & (df["lib_dep"] == "Hérault"),:]
tab_finistere = df.loc[(df["date"]>"2021-12-31") & (df["date"]<"2022-07-17") & (df["lib_dep"]=="Finistère"),:]

xHerault = pd.to_datetime(pd.Series(tab_herault.date))
xFinistere = pd.to_datetime(pd.Series(tab_finistere.date))

plt.scatter(xHerault,tab_herault.tx_incid, c="red", s=2, label="Hérault")
plt.scatter(xFinistere,tab_finistere.tx_incid, c="black", s=2, label="Finistère")
plt.title("Daily incidence rate in ‰ in Hérault and Finistère")
plt.xlabel("Date")
plt.ylabel("Incidence rate in ‰")
plt.legend()
plt.show()

y1H = tab_herault.rea
y2H = tab_herault.hosp

y1F = tab_finistere.rea
y2F = tab_finistere.hosp

fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True)
fig.suptitle("Daily intensive care and hospitalized units admission rates in Hérault and in Finistère")
#fig.suptitle('Horizontally stacked subplots')
ax1.bar(xHerault, y2H, width= 0.8, color= "#EDFF91", label="Hospitalized covid patients")
ax1.bar(xHerault, y1H, width = 0.8, color = "#3ED8C9", label="Intensive care unit admission")
ax1.legend()

ax2.bar(xFinistere, y2F, width= 0.8, color= "#EDFF91", label="Hospitalized covid patients")
ax2.bar(xFinistere, y1F, width = 0.8, color = "#3ED8C9", label="Hospitalized covid patients")
ax2.legend()

ax1.set_xlabel('Date')
ax2.set_xlabel('Date')

ax1.set_ylabel("Intensive care and hospitalized units admission rates")
ax2.set_ylabel("Intensive care and hospitalized units admission rates")

ax1.set_title("Hérault")
ax2.set_title("Finistère")

plt.show()


col_list_temp = ["Date","Température (°C)","communes (name)","department (name)","region (name)","mois_de_l_annee"]

df_herault = pd.read_csv('herault.csv', sep=';', usecols=col_list_temp, encoding='utf-8')
df_finistere = pd.read_csv('finistere.csv', sep=';', usecols=col_list_temp, encoding='utf-8')
print('test', df_herault)

tab_temp_herault = df_herault.loc[(df_herault["Date"]>"2021-12-31") & (df_herault["Date"]<"2022-07-17"),:]
tab_temp_finistere = df_finistere.loc[(df_finistere["Date"]>"2021-12-31") & (df_finistere["Date"]<"2022-07-17"),:]

xTempHerault = pd.to_datetime(pd.Series(tab_temp_herault.Date))
xTempFinistere = pd.to_datetime(pd.Series(tab_temp_finistere.Date))

print("tab", df_herault)