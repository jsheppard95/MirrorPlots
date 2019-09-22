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
'um', include_slave=True, gantry_cutoff=True,
hl_roi=[(14.908, 924.665), (23629.5, 23633.1)],
ll_roi=[(133.632, 1021.8), (15973.6, 15980)],
pdf_title='TestData.pdf')

input('Press <Return> to close')
plt.close('all')
