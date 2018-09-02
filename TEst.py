from astropy.table import Table, Column
import matplotlib.pyplot as plt
#url = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&select=pl_hostname,ra,dec&order=dec&format=csv"
url = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets"
# This API returns Hostname, RA and Dec

t = Table.read(url, format="csv")

t_b = t[t["pl_letter"] == "b"]
t_c = t[t["pl_letter"] == "c"]
t_d = t[t["pl_letter"] == "d"]
t_e = t[t["pl_letter"] == "e"]
t_f = t[t["pl_letter"] == "f"]
t_g = t[t["pl_letter"] == "g"]
t_h = t[t["pl_letter"] == "h"]
t_i = t[t["pl_letter"] == "i"]

fig = plt.figure()
ax = fig.add_subplot(1,1,1,aspect="equal")
ax.scatter(t_b["ra"],t_b["dec"],color="Black",label = "2 Planets")
ax.scatter(t_c["ra"],t_c["dec"],color="red", label = "3 Planets")
ax.scatter(t_d["ra"],t_d["dec"],color="blue", label = "4 Planets")
ax.scatter(t_e["ra"],t_e["dec"],color="green", label = "5 Planets")
ax.scatter(t_f["ra"],t_f["dec"],color="yellow", label = "6 Planets")
ax.scatter(t_g["ra"],t_g["dec"],color="purple", label = "7 Planets")
ax.scatter(t_h["ra"],t_h["dec"],color="orange", label = "8 Planets")
ax.scatter(t_i["ra"],t_i["dec"],color="cyan", label = "9 Planets")

ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
ax.set_xlim(360,0)
ax.set_ylim(-90,90)
ax.set_ylabel("DEC")
ax.set_xlabel("RA")
ax.set_title("Positions of Explanets by number of planets in system")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()