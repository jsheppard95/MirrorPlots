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
#pf.plot_data(\
#'/reg/neh/home/sheppard/FlatMirrors/M2K3/M2K3_ScopeFiles/x_closedLoop_slipAT23600um_largeMove.csv',
#'um', include_slave=True, gantry_cutoff=True)

# Plot Large Move Xup Slips with PLM Error Data
#pf.plot_data(\
#'/reg/neh/home/sheppard/FlatMirrors/M2K3/M2K3_ScopeFiles/x_closedLoop_slip_PLMerror.csv',
#'um', include_slave=True, gantry_cutoff=True)

# Plot Y move after gantry re-alignment where heard loud noise
#pf.plot_data(\
#'/reg/neh/home/sheppard/FlatMirrors/M2K3/M2K3_ScopeFiles/y_motion_gantry_realign_strange_ding_2019_10_29.csv',
#'um', include_slave=True, gantry_cutoff=True)

##############################################################################
# Plotting Data from after we got things working
# X Motion:
#pf.plot_data(\
#'/reg/neh/home/sheppard/FlatMirrors/M2K3/M2K3_ScopeFiles/Jackson-Project/X_LimToLim_JacksonProj_2019_12_10.csv',
#'um', include_slave=True, gantry_cutoff=True, pdf_title='M2K3-X-PreInstallCheckoutPlots.pdf')

# Y Motion
#pf.plot_data(\
#'/reg/neh/home/sheppard/FlatMirrors-PreInstall-Checkouts/M2K3/Jackson-Project/Y_LLToHL_2019_12_10.csv',
#'um', include_slave=True, gantry_cutoff=True, pdf_title='M2K3/M2K3-Y-PreInstallCheckoutPlots.pdf')

# Pitch Motion
pf.plot_data(\
'/reg/neh/home/sheppard/FlatMirrors-PreInstall-Checkouts/M2K3/Jackson-Project/Pitch_LimSwitchRpt_2019_12_11.csv',
'urad', include_slave=False, gantry_cutoff=True, pdf_title='M2K3/M2K3-Pitch-PreInstallCheckoutPlots.pdf')

input('Press <Return> to close')
plt.close('all')
