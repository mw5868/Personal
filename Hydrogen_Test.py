# %%
import matplotlib.pyplot as plt
import batman
from orbital import KeplerianElements,earth,plot,Maneuver
from scipy.constants import kilo
from astropy.io import ascii


orb1 = KeplerianElements.with_altitude(5000*kilo, body=earth)
man1 = Maneuver.hohmann_transfer_to_altitude(15000*kilo)
plot(orb1,maneuver=man1)
man2 = Maneuver.hohmann_transfer_to_radius(20000)
plot(orb1,maneuver=man2)


#Reading real data, and plotting on a graph.
data = ascii.read("c:\\users\mwood\TransitData\ConfirmedPlanets.csv")
plt.xlabel("$Orbital Period$",fontsize=10)
plt.ylabel("$orbital Inclination$",fontsize=10)
plt.scatter(data["pl_orbper"],data['pl_orbincl'])
