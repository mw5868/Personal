# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 19:15:19 2018

@author: mwood
"""

import batman
import numpy as np
import matplotlib.pyplot as plt

params = batman.TransitParams()
params.t0 = 0
params.per = 1
params.rp = 0.1
params.a = 7
params.inc = 90
params.ecc = 0.6
params.w = 90
params.limb_dark = 'quadratic'
params.u = [0.1,0.3]

t = np.linspace(-0.025,0.025,1000)

m = batman.TransitModel(params, t)

flux = m.light_curve(params)

radii = np.linspace(0.09,0.11,20)


    
plt.plot(flux)