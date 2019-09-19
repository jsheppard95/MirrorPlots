"""
Script to call plot_functions to make plots for a particular file
"""

import MirrorPlots.plot_functions as pf
import matplotlib.pyplot as plt

# Plot Y HL Data
#pf.plot_data(\
#'/reg/neh/home/sheppard/FlatMirrors/M1K3/M1K3_ScopeFiles/Y_HighLimSwitchRpt_2019_9_18.csv',
#'um', include_slave=True, gantry_cutoff=True,
#pdf_title='M1K3-Y-HLPreInstallCheckoutPlots.pdf',
#hl_roi=[(136.77, 936.155), (122494, 122501)])

# Plot Y LL Data
#pf.plot_data(\
#'/reg/neh/home/sheppard/FlatMirrors/M1K3/M1K3_ScopeFiles/Y_LowLimSwitchRpt_2019_9_18.csv',
#'um', include_slave=True, gantry_cutoff=True,
#ll_roi=[(140.75, 683.165), (8699.25, 8705.95)],
#pdf_title='M1K3-Y-LLPreInstallCheckoutPlots.pdf')

# Plot X Data
#pf.plot_data(\
#'/reg/neh/home/sheppard/FlatMirrors/M1K3/M1K3_ScopeFiles/X_LimSwitchRpt_2019_9_18.csv',
#'um', include_slave=True, gantry_cutoff=True,
#hl_roi=[(14.908, 924.665), (23629.5, 23633.1)],
#ll_roi=[(133.632, 1021.8), (15973.6, 15980)],
#pdf_title='M1K3-X-PreInstallCheckoutPlots.pdf')

# Plot Pitch Data
pf.plot_data(\
'/reg/neh/home/sheppard/FlatMirrors/M1K3/M1K3_ScopeFiles/Pitch_LimSwitchRpt_2019_9_18.csv',
'urad', gantry_cutoff=True, hl_roi=[(22.6282, 673.76), (56329.8, 56339.5)],
ll_roi=[(123.2, 763.308), (54032.7, 54079.4)],
pdf_title='M1K3-Pitch-PreInstallCheckoutPlots.pdf')

input('Press <Return> to close')
plt.close('all')
