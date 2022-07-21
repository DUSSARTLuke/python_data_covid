import pandas as pd
import matplotlib.pyplot as plt

col_list = ['date','lib_dep','tx_pos','tx_incid','TO','R','hosp','rea','rad','reg_rea','incid_hosp','incid_rea','incid_rad','incid_dchosp','reg_incid_rea','pos']

df = pd.read_csv('table-indicateurs-open-data-dep-2022-07-19-19h00.csv', sep=',', usecols=col_list, encoding='utf-8')
tab_herault = df.loc[(df["date"]>"2021-12-31") & (df["date"]<"2022-07-17") & (df["lib_dep"] == "Hérault"),:]
tab_finistere = df.loc[(df["date"]>"2021-12-31") & (df["date"]<"2022-07-17") & (df["lib_dep"]=="Finistère"),:]

xHerault = pd.to_datetime(pd.Series(tab_herault.date))
xFinistere = pd.to_datetime(pd.Series(tab_finistere.date))

col_list_temp = ["ID OMM station","Date","Pression au niveau mer","Variation de pression en 3 heures","Type de tendance barométrique","Direction du vent moyen 10 mn","Vitesse du vent moyen 10 mn","Température","Point de rosée","Humidité","Visibilité horizontale","Temps présent","Temps passé 1","Temps passé 2","Nebulosité totale","Nébulosité  des nuages de l' étage inférieur","Hauteur de la base des nuages de l'étage inférieur","Type des nuages de l'étage inférieur","Type des nuages de l'étage moyen","Type des nuages de l'étage supérieur","Pression station","Niveau barométrique","Géopotentiel","Variation de pression en 24 heures","Température minimale sur 12 heures","Température minimale sur 24 heures","Température maximale sur 12 heures","Température maximale sur 24 heures","Température minimale du sol sur 12 heures","Méthode de mesure Température du thermomètre mouillé","Température du thermomètre mouillé","Rafale sur les 10 dernières minutes","Rafales sur une période","Periode de mesure de la rafale","Etat du sol","Hauteur totale de la couche de neige, glace, autre au sol","Hauteur de la neige fraîche","Periode de mesure de la neige fraiche","Précipitations dans la dernière heure","Précipitations dans les 3 dernières heures","Précipitations dans les 6 dernières heures","Précipitations dans les 12 dernières heures","Précipitations dans les 24 dernières heures","Phénomène spécial 1","Phénomène spécial 2","Phénomène spécial 3","Phénomène spécial 4","Nébulosité couche nuageuse 1","Type nuage 1","Hauteur de base 1","Nébulosité couche nuageuse 2","Type nuage 2","Hauteur de base 2","Nébulosité couche nuageuse 3","Type nuage 3","Hauteur de base 3","Nébulosité couche nuageuse 4","Type nuage 4","Hauteur de base 4","Coordonnees","Nom","Type de tendance barométrique","Temps passé 1","Temps présent","Température (°C)","Température minimale sur 12 heures (°C)","Température minimale sur 24 heures (°C)","Température maximale sur 12 heures (°C)","Température maximale sur 24 heures (°C)","Température minimale du sol sur 12 heures (en °C)","Latitude","Longitude","Altitude","communes (name)","communes (code)","EPCI (name)","EPCI (code)","department (name)","department (code)","region (name)","region (code)","mois_de_l_annee"]

df_herault = pd.read_csv('herault.csv', sep=';', usecols=col_list_temp, encoding='utf-8')
df_finistere = pd.read_csv('finistere.csv', sep=';', usecols=col_list_temp, encoding='utf-8')


tab_temp_herault = df_herault.loc[(df_herault["Date"]>"2021-12-31") & (df_herault["Date"]<"2022-07-17"),:]
tab_temp_finistere = df_finistere.loc[(df_finistere["Date"]>"2021-12-31") & (df_finistere["Date"]<"2022-07-17"),:]

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
ax1.bar(xHerault, y2H, width= 0.8, color= "#EDFF91", label="Intensive care unit admission")
ax1.bar(xHerault, y1H, width = 0.8, color = "#3ED8C9", label="Hospitalized covid patients")
ax1.legend()

ax2.bar(xFinistere, y2F, width= 0.8, color= "#EDFF91", label="Intensive care unit admission")
ax2.bar(xFinistere, y1F, width = 0.8, color = "#3ED8C9", label="Hospitalized covid patients")
ax2.legend()

ax1.set_xlabel('Date')
ax2.set_xlabel('Date')

ax1.set_ylabel("Intensive care and hospitalized units admission rates")
ax2.set_ylabel("Intensive care and hospitalized units admission rates")

ax1.set_title("Hérault")
ax2.set_title("Finistère")

plt.show()
