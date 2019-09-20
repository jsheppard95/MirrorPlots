"""
Script to call plot_functions to make plots for a particular file
"""

import MirrorPlots.plot_functions as pf
import matplotlib.pyplot as plt

# Plot Y Data
#pf.plot_data(\
#'/reg/neh/home/sheppard/HOMSRefurbish/M1L0-PreInstall-Checkout/Y_limit_rpt_test3-5_9_4_19.csv',
#'mm', gantry_cutoff=True, include_slave=True,
#hl_roi=[(532.992, 983.704), (27.6632, 27.6643)],
#ll_roi=[(322.974, 1139.98), (3.52054, 3.52117)],
#pdf_title='M1L0-Y-PreInstallCheckoutPlots.pdf')

# Plot X Data
#pf.plot_data(\
#'/reg/neh/home/sheppard/HOMSRefurbish/M1L0-PreInstall-Checkout/X_limit_rpt_9_4_19.csv',
#'mm', gantry_cutoff=True, include_slave=True,
#hl_roi=[(6.63368, 755.889), (25.5119, 25.5128)],
#ll_roi=[(86.2136, 816.423), (22.847, 23.0028)],
#pdf_title='M1L0-X-PreInstallCheckoutPlots.pdf')

# Plot Pitch Data
pf.plot_data(\
'/reg/neh/home/sheppard/HOMSRefurbish/M1L0-PreInstall-Checkout/PitchCoarse_limit_rpt_9_4_19.csv',
'urad', gantry_cutoff=True, hl_roi=[(20.8262, 703.554), (21941.6, 22010.7)],
ll_roi=[(90.7599, 806.176), (14662.2, 14740.7)],
pdf_title='M1L0-Pitch-PreInstallCheckoutPlots.pdf')

input('Press <Return> to close')
plt.close('all')
