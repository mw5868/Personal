# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 17:54:38 2018

@author: mwood
"""

from orbital import earth, KeplerianElements,Maneuver, plot, plot3d
from numpy import radians
from scipy.constants import kilo, minute

from orbital import earth_sidereal_day

orbit = KeplerianElements.with_period(88.47*minute,body=earth,i=radians(32.5),ref_epoch="J1962")
#plot(orbit,title="orbit")

plot3d(orbit, title="First Orbit of Friendship-7",animate=True)


