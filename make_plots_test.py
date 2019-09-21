"""
Script to call plot_functions to make plots for a particular file
"""

import MirrorPlots.plot_functions as pf
import matplotlib.pyplot as plt

#pf.plot_data('test_data.csv', 'mm', debug=True, include_slave=True,
#             gantry_cutoff=True)
#plot_functions.plot_data('M1L1_X_LimSwitchRpt.csv', 'um', gantry_cutoff=True,
#                         by_index=True, debug=True)

# Plot M1K3 X Data - includes slave
pf.plot_data(\
'/reg/neh/home/sheppard/FlatMirrors/M1K3/M1K3_ScopeFiles/X_LimSwitchRpt_2019_9_18.csv',
'um', include_slave=True, gantry_cutoff=True, pdf_title='TestData.pdf')

input('Press <Return> to close')
plt.close('all')
