"""
Script to call plot_functions to make plots for a particular file
"""

import MirrorPlots.plot_functions as pf
import matplotlib.pyplot as plt

pf.plot_data('test_data.csv', 'mm', debug=True, include_slave=True,
             gantry_cutoff=True)
#plot_functions.plot_data('M1L1_X_LimSwitchRpt.csv', 'um', gantry_cutoff=True,
#                         by_index=True, debug=True)
input('Press <Return> to close')
plt.close('all')
