# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 15:21:31 2018

@author: mwood
"""
import numpy as np
import scipy.signal
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams["figure.figsize"] = (14,5)
rcParams["font.size"] = 20
from astropy.stats import LombScargle
import astropy.io.fits

from matplotlib import rcParams
rcParams["figure.figsize"] = (14, 5)
rcParams["font.size"] = 20

import astropy.io.fits

target_file = ("https://archive.stsci.edu/missions/kepler/kepler/target_pixel_files/1000/100003954/kplr100003954-2012088054726_lpd-targ.fits.gz")

data = astropy.io.fits.open(target_file)[1].data
time = data["TIME"][data['QUALITY'] == 0]
images = data["FLUX"][data['QUALITY'] == 0]

lightcurve = np.sum(images, axis=(1, 2))

plt.plot(time, lightcurve, '.')
plt.ylabel("Brightness")
plt.xlabel("Time")

trend = scipy.signal.savgol_filter(lightcurve, 101, polyorder=3) 
percent_change = 100 * ((lightcurve / trend) - 1)

plt.plot(time, percent_change, '.')
plt.ylabel("Brightness change (%)")
plt.xlabel("Time")

from astropy.stats import LombScargle
frequency, power = LombScargle(time, percent_change, nterms=2).autopower(minimum_frequency=1/1.5, maximum_frequency=1/0.6, samples_per_peak=10)
period = 1 / frequency[np.argmax(power)]

plt.plot(1 / frequency, power)
plt.xlabel("Period (days)")
plt.ylabel("Power")

n_plots = 10
plt.figure(figsize=(10, 30))
for i in range(n_plots):
    mask = (time >= time[0] + i*period) & (time < time[0] + (i+1)*period)
    plt.subplot(n_plots, 1, i+1)
    plt.scatter(time[mask], percent_change[mask], c='C{}'.format(i))
    
    plt.figure(figsize=(10, 5))
for i in range(n_plots):
    mask = (time >= time[0] + i*period) & (time < time[0] + (i+1)*period)
    plt.scatter(time[mask] - time[0] - i*period, percent_change[mask])