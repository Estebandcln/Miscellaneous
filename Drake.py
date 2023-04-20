# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 00:19:16 2023

@author: DECLINE
"""

# Drake equation

R_star = 7 # Rate of star formation in the Milky Way (per year)
fp = 0.5 # Fraction of those stars that have planets
ne = 0.4 # Average number of planets in the habitable zone (per star)
fl = 0.2 # Fraction of these planets on which life emerges
fi = 0.8 # Fraction of planets on which life develops to a technological civilization
ft = 0.1 # Fraction of civilizations that emit detectable signals
L = 2000 # Length of time for which such civilizations release detectable signals (years)
#En utilisant les valeurs supposées ci-dessus, nous avons :

N = R_star*fp*ne*fl*fi*ft*L
print("Number of active, communicative extraterrestrial civilizations in the Milky Way:",round(N,2))