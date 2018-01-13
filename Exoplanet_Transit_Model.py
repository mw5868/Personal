# Testing the BATMAN exoplanet code
# Example code taken from BATMAN tutoral.
import batman
import numpy as np
import matplotlib.pyplot as plt

params = batman.TransitParams()
params.t0 = 0.                       #time of inferior conjunction
params.per = 1.                      #orbital period
params.rp = 0.1                      #planet radius (in units of stellar radii)
params.a = 15.                       #semi-major axis (in units of stellar radii)
params.inc = 87.                     #orbital inclination (in degrees)
params.ecc = 0.                      #eccentricity
params.w = 90.                       #longitude of periastron (in degrees)
params.u = [0.1, 0.3]                #limb darkening coefficients [u1, u2]
params.limb_dark = "quadratic"       #limb darkening model

t = np.linspace(-0.05,0.05,100)

m = batman.TransitModel(params, t)    #initializes model

flux = m.light_curve(params)          #calculates light curve

radii = np.linspace(0.09,0.11,20)
for r in radii:
    params.np = r
    new_flux = m.light_curve(params)

plt.plot(t,flux)
plt.xlabel("Time from central transit")
plt.ylabel("Relative flux")
plt.show()

ld_options = ["uniform","linear","quadratic","nonlinear"]
ld_coefficients = [[], [0.3], [0.1, 0.3], [0.5, 0.1, 0.1, -0.1]]

plt.figure()
for i in range(4):
        params.limb_dark = ld_options[i]          #specifies the LD profile
        params.u = ld_coefficients[i]             #updates LD coefficients
        m = batman.TransitModel(params, t)        #initializes the model
        flux = m.light_curve(params)              #calculates light curve
        plt.plot(t, flux, label = ld_options[i])
plt.show()
