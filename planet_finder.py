# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 19:30:46 2018

@author: mwood
"""

import numpy as np
import scipy.signal
import matplotlib.pyplot as plt

# Configure the plotting aesthetics (boring)

from matplotlib import rcParams
rcParams["figure.figsize"] = (14, 5)
rcParams["font.size"] = 20

#url = "https://archive.stsci.edu/missions/kepler/target_pixel_files/0119/011904151/kplr011904151-2010009091648_lpd-targ.fits.gz"
#url2 = "https://archive.stsci.edu/missions/kepler/target_pixel_files/0019/001995038/kplr001995038-2009131105131_lpd-targ.fits.gz"
print("You find the URL via STSCI.edu website")
url = str(input("Enter URL for FITS: "))

# Read in Kepler data for star number 011904151
import astropy.io.fits
data = astropy.io.fits.open(url)[1].data
time = data["TIME"][data['QUALITY'] == 0]
images = data["FLUX"][data['QUALITY'] == 0]

time[0:5]  # The units are in days

images[0:5]  # The images give us photons per pixel per second

# Let's plot the image at the first timestamp
#plt.imshow(images[0], cmap='gray', interpolation='nearest');

# Let's create a lightcurve by summing the flux in all the time cadences
lightcurve = np.sum(images, axis=(1, 2))
'''
plt.plot(time, lightcurve, '.')
plt.ylabel("Brightness")
plt.xlabel("Time");
'''
trend = scipy.signal.savgol_filter(lightcurve, 101, polyorder=3) 
percent_change = 100 * ((lightcurve / trend) - 1)

'''plt.plot(time, percent_change, '.')
plt.ylabel("Brightness change (%)")
plt.xlabel("Time");
'''
# We will use the Lomb-Scargle Periodogram.
# For background, see Jake VanderPlas' blog at https://jakevdp.github.io/blog/2015/06/13/lomb-scargle-in-python/
from astropy.stats import LombScargle
frequency, power = LombScargle(time, percent_change, nterms=2).autopower(minimum_frequency=1/1.5, maximum_frequency=1/0.6, samples_per_peak=10)
period = 1 / frequency[np.argmax(power)]

plt.plot(1 / frequency, power)
plt.xlabel("Period (days)")
plt.ylabel("Power");


n_plots = 10
'''
plt.figure(figsize=(10, 30))
for i in range(n_plots):
    mask = (time >= time[0] + i*period) & (time < time[0] + (i+1)*period)
    plt.subplot(n_plots, 1, i+1)
    plt.scatter(time[mask], percent_change[mask], c='C{}'.format(i))
'''
plt.figure(figsize=(10, 5))
for i in range(n_plots):
    mask = (time >= time[0] + i*period) & (time < time[0] + (i+1)*period)
    plt.scatter(time[mask] - time[0] - i*period, percent_change[mask])
plt.show()
