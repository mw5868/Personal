# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 15:04:33 2018

@author: Mark Woodland
"""

from astroplan import Observer, FixedTarget
from astropy.coordinates import SkyCoord
from astropy.time import Time
import astropy.units as u
import numpy as np

site = Observer.at_site("siding spring observatory")



obj_input = input("Enter your object: ")

obj = FixedTarget.from_name(obj_input)
time = Time.now()

sunset_tonight = site.sun_set_time(time, which='nearest')
sunrise_tonight = site.sun_rise_time(time, which='nearest')

obj_rise = site.target_rise_time(time, obj) + 5*u.minute
obj_set = site.target_set_time(time, obj) - 5*u.minute

all_up_start = np.max([obj_rise])
all_up_end = np.min([obj_set])

start = np.max([sunset_tonight, all_up_start])
end = np.min([sunrise_tonight, all_up_end])


is_up = site.target_is_up(time,obj)
print("Is your object visible? " + str(is_up))
#print(is_up)

if is_up == True:
    import numpy as np
    import astropy.units as u
    object_rise = site.target_rise_time(time, obj) + 5*u.minute
    object_set = site.target_set_time(time, obj) - 5*u.minute
    from astroplan import download_IERS_A
    download_IERS_A()
    sunset_tonight = site.sun_set_time(time, which='nearest')
    print("sunset at your selected site will be " + sunset_tonight.iso + " UTC")
    from astroplan.plots import plot_airmass 
    import matplotlib.pyplot as plt 
    plot_airmass(obj, site, time) 
    plt.title("Visibility Chart")
    plt.legend(loc=1, bbox_to_anchor=(1, 1)) 
    plt.show()
    
    site.altaz(time, obj).secz
    from astroplan.plots import plot_parallactic
    plot_parallactic(obj, site, time)
    plt.legend(loc=2)
    plt.show()
    
    
    moon_rise = site.moon_rise_time(time)
    moon_set = site.moon_set_time(time)
    
    print("Moon rise will be at: " + str(moon_rise))
    print("Moon set will be at : " + str(moon_set))
    
    visible_time = start + (end - start)*np.linspace(0, 1, 20)
    
    print("Altitude of Moon during observation: " + str(visible_time))
    
    from astroplan.plots import plot_sky
    obj_style = {'color': 'r'}
    plot_sky(obj, site, start, style_kwargs=obj_style)
    plt.title("Object position at start of observing window")
    plt.legend(loc='center left', bbox_to_anchor=(1.25, 0.5))
    plt.show()
    
    plot_sky(obj, site, end, style_kwargs=obj_style)
    plt.legend(loc='center left', bbox_to_anchor=(1.25, 0.5))
    plt.title("Object position at end of observing window")
    plt.show()
    
    time_window = start + (end - start) * np.linspace(0, 1, 10)
    plot_sky(obj, site, time_window, style_kwargs=obj_style)
    plt.title("Object movement over observing window duration")
    plt.legend(loc='center left', bbox_to_anchor=(1.25, 0.5))
    plt.show()
    

else: 
    print ("Your object isn't visible from the site selected and therefore planning cannot take place.")
    

