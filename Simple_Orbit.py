from orbital import KeplerianElements, earth, Maneuver, plot
from scipy.constants import kilo
import matplotlib.pyplot as plt

orb1 = KeplerianElements.with_altitude(1000*kilo, body = earth)
man = Maneuver.hohmann_transfer_to_altitude(150000*kilo)
plot(orb1, maneuver = man)
plt.show()
