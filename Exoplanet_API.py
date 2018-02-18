from astropy.table import Table, Column
import matplotlib.pyplot as plt
url = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&select=pl_hostname,ra,dec&order=dec&format=csv"
# This API returns Hostname, RA and Dec

t = Table.read(url, format="csv")

# Generate a plot of RA against Dec for the data.
plt.scatter(t["ra"],t["dec"])
plt.xlabel("RA")
plt.ylabel("DEC")
plt.show()