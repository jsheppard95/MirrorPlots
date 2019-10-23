"""
Script to call plot_functions to make plots for a particular file
"""

import MirrorPlots.plot_functions as pf
import matplotlib.pyplot as plt

# Plot Small Moves Xup Slips Data
#pf.plot_data(\
#'/reg/neh/home/sheppard/FlatMirrors/M2K3/M2K3_ScopeFiles/x_closedLoop_slipAt23600um.csv',
#'um', include_slave=True, gantry_cutoff=True)

# Plot Large Move Xup Slips Data
pf.plot_data(\
'/reg/neh/home/sheppard/FlatMirrors/M2K3/M2K3_ScopeFiles/x_closedLoop_slipAT23600um_largeMove.csv',
'um', include_slave=True, gantry_cutoff=True)

# Plot Large Move Xup Slips with PLM Error Data
#pf.plot_data(\
#'/reg/neh/home/sheppard/FlatMirrors/M2K3/M2K3_ScopeFiles/x_closedLoop_slip_PLMerror.csv',
#'um', include_slave=True, gantry_cutoff=True)

input('Press <Return> to close')
plt.close('all')
