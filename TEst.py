# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 17:54:38 2018

@author: mwood
"""

from astropy.table import Table
import matplotlib.pyplot as plt

url = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets"

t = Table.read(url,format="csv")

t_trans = t[["pl_discmethod"]=="Transit"]

fig, axes = plt.subplots(1,1,figsize=(8,10),subplot_kw={"projection":"aitoff"})

axes.set_title("Transit")
plt.scatter(t_trans["ra"],t_trans["dec"],color="red")
