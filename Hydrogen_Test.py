# %%
import matplotlib.pyplot as plt
import batman
from orbital import KeplerianElements,earth,plot,Maneuver
from scipy.constants import kilo


orb1 = KeplerianElements.with_altitude(5000*kilo, body=earth)
man1 = Maneuver.hohmann_transfer_to_altitude(15000*kilo)
plot(orb1,maneuver=man1)
