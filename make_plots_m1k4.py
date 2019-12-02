"""
Script to call plot_functions to make plots for a particular file
"""

import MirrorPlots.plot_functions as pf
import matplotlib.pyplot as plt

# Plot Y 1 um Adjustment:
#pf.plot_and_zoom(\
#'/reg/neh/home/sheppard/HOMSRefurbish/M1K4-PreInstall-Checkout/Yup_1um_adj.csv',
#'mm', pdf_title='M1K4-Y-1umAdjust-PreInstallCheckoutPlots.pdf')

#pf.plot_and_zoom(\
#'/reg/neh/home/sheppard/HOMSRefurbish/M1K4-PreInstall-Checkout/Yup_1um_adj.csv',
#'mm', pdf_title='M1K4/M1K4-Y-1umAdjustRptAbility-PreInstallCheckoutPlots.pdf')

# Plot X 1 um Adjustment:
#pf.plot_and_zoom(\
#'/reg/neh/home/sheppard/HOMSRefurbish/M1K4-PreInstall-Checkout/Xup_1um_adj.csv',
#'mm', pdf_title='M1K4-X-1umAdjust-PreInstallCheckoutPlots.pdf')

#pf.plot_and_zoom(\
#'/reg/neh/home/sheppard/HOMSRefurbish/M1K4-PreInstall-Checkout/Xup_1um_adj.csv',
#'mm', pdf_title='M1K4/M1K4-X-1umAdjustRptAbility-PreInstallCheckoutPlots.pdf')

# Plot Pitch 1 um Adjustment:
#pf.plot_and_zoom(\
#'/reg/neh/home/sheppard/HOMSRefurbish/M1K4-PreInstall-Checkout/PitchCoarse_1um_adj.csv',
#'urad', pdf_title='M1K4-Pitch-1umAdjust-PreInstallCheckoutPlots.pdf')

pf.plot_and_zoom(\
'/reg/neh/home/sheppard/HOMSRefurbish/M1K4-PreInstall-Checkout/PitchCoarse_1um_adj.csv',
'urad', pdf_title='M1K4/M1K4-Pitch-1umAdjustRptAbility-PreInstallCheckoutPlots.pdf')

input('Press <Return> to close')
plt.close('all')
