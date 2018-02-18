# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 17:17:46 2018

@author: mwood
"""

import matplotlib.pyplot as plt
plt.ion()

from astropy import time
from astropy import units as u

from poliastro.bodies import Sun, Earth, Jupiter
from poliastro.twobody import Orbit 
from poliastro.plotting import plot, OrbitPlotter3D
from poliastro import iod
from poliastro.util import norm
import matplotlib.pyplot as plt
from poliastro.twobody.orbit import propagate

# Perigee = 149 km
# Apogee = 248 km
# Inclination = 32.5 degrees
# Period = 88.47 Minutes

date_Launch = time.Time("1962-02-20 14:47", scale = 'utc')
date_land = time.Time("1962-02-20 19:43", scale = 'utc')
tof = date_land - date_Launch

print("Time of Flight was: " + str(tof.to(u.h)))

r_per = Earth.R + 149 * u.km
r_apo = Earth.R + 248 * u.km
inc = 32.5 *u.deg

a_parking = (r_per + r_apo) / 2
ecc_parking = 1 - r_per / a_parking

parking = Orbit.from_classical(Earth, a_parking, ecc_parking,
                               inc, 0 * u.deg, 0 * u.deg, 0 * u.deg, date_Launch)

plot(parking,label="Friendship-7 Initial Orbit")



