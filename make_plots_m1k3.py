"""
Script to call plot_functions to make plots for a particular file
"""

import MirrorPlots.plot_functions_test as pf
import matplotlib.pyplot as plt

# Plot Y HL Data
pf.plot_data(\
'/reg/neh/home/sheppard/FlatMirrors/M1K3/M1K3_ScopeFiles/test.csv',
'um', include_slave=True, gantry_cutoff=True, by_index=True)

input('Press <Return> to close')
plt.close('all')
