"""
Script to call plot_functions to make plots for a particular file
"""

import MirrorPlots.plot_functions as pf
import matplotlib.pyplot as plt

###########################################################################
# Y Motion:

# Plot Y HL Data
#pf.plot_data(\
#'/reg/neh/home/sheppard/FlatMirrors/M1K1/M1K1_ScopeFiles/Y_HL_rpt_2019_10_23.csv',
#'um', include_slave=True, gantry_cutoff=True, by_index=True,
#move_start_indecesY=[2112, 4200, 6432, 13083, 15147, 21900, 25036, 28995, 31208, 36259, 38313, 46846],
#peak_gantry_indecesY=[2254, 4925, 6628, 13832, 15332, 24028, 26646, 30219, 31399, 37488, 39559, 47198],
#move_end_indecesY=[3338, 6223, 10842, 15000, 17567, 24792, 27366, 30991, 34007, 38181, 42834, 47848])
#hl_roi=[(-7.596, 482.932), (31595.3, 31601)],
#pdf_title='M1K1-Y-HLPreInstallCheckoutPlots.pdf')

# Plot Y LL Data
#pf.plot_data(\
#'/reg/neh/home/sheppard/FlatMirrors/M1K1/M1K1_ScopeFiles/Y_LL_rpt_2019_10_23.csv',
#'um', include_slave=True, gantry_cutoff=True,
#ll_roi=[(-9.376, 412.916), (13517.3, 13519.5)],
#pdf_title='M1K1-Y-LLPreInstallCheckoutPlots.pdf')

# Plot Y Repeatability Data
#pf.plot_and_zoom(\
#'/reg/neh/home/sheppard/FlatMirrors/M1K1/M1K1_ScopeFiles/Y_repeatability_2019_10_23.csv',
#'um', pdf_title='M1K1-Y-Repeatability-PreInstallCheckoutPlots.pdf')

# Plot Y 1 um Adjustment Data
#pf.plot_and_zoom(\
#'/reg/neh/home/sheppard/FlatMirrors/M1K1/M1K1_ScopeFiles/Y_1um_adjust_2019_10_23.csv',
#'um', pdf_title='M1K1-Y-1umAdjust-PreInstallCheckoutPlots.pdf')

# Plot Encoder Noise Data
pf.plot_data(\
'/reg/neh/home/sheppard/FlatMirrors-PreInstall-Checkouts/M1K1/Y_EncNoise_2019_10_23.csv',
'um', gantry_cutoff=True)
###########################################################################

###########################################################################
# X Motion:

# Plot X HL Data
#pf.plot_data(\
#'/reg/neh/home/sheppard/FlatMirrors/M1K1/M1K1_ScopeFiles/X_HL_rpt_2019_10_23.csv',
#'um', include_slave=True, gantry_cutoff=True, by_index=True,
#move_start_indecesX=[1059, 2479, 8165, 9844, 18761, 24600, 29330, 31020, 35690, 37495],
#peak_gantry_indecesX=[1218, 2675, 8326, 9964, 18913, 24669, 29482, 31097, 35842, 37572],
#move_end_indecesX=[2213, 3994, 9505, 11340, 20254, 26125, 30640, 32410, 37000, 38900])
#hl_roi=[(-2.92, 464.72), (31758.4, 31769.4)],
#pdf_title='M1K1-X-HLPreInstallCheckoutPlots.pdf')

# Plot X LL Data
#pf.plot_data(\
#'/reg/neh/home/sheppard/FlatMirrors/M1K1/M1K1_ScopeFiles/X_LL_rpt_2019_10_23.csv',
#'um', include_slave=True, gantry_cutoff=True,
#ll_roi=[(-21.4677, 516.465), (7526.81, 7539.06)],
#pdf_title='M1K1-X-LLPreInstallCheckoutPlots.pdf')

# Plot X Repeatability
#pf.plot_and_zoom(\
#'/reg/neh/home/sheppard/FlatMirrors/M1K1/M1K1_ScopeFiles/X_repeatability_2019_10_23.csv',
#'um', pdf_title='M1K1-X-Repeatability-PreInstallCheckoutPlots.pdf')

# Plot X 1 um Adjustment Data
#pf.plot_and_zoom(\
#'/reg/neh/home/sheppard/FlatMirrors/M1K1/M1K1_ScopeFiles/X_1um_adjust_2019_10_23.csv',
#'um', pdf_title='M1K1-X-1umAdjust-PreInstallCheckoutPlots.pdf')
###########################################################################

###########################################################################
# Pitch Motion
# Plot Pitch Data
#pf.plot_data(\
#'/reg/neh/home/sheppard/FlatMirrors/M1K1/M1K1_ScopeFiles/Pitch_LimSwitchRpt_2019_11_27.csv',
#'urad', gantry_cutoff=True,
#pdf_title='M1K1/M1K1-Pitch-PreInstallCheckoutPlots.pdf')

#pf.plot_and_zoom(\
#'/reg/neh/home/sheppard/FlatMirrors/M1K1/M1K1_ScopeFiles/Pitch_repeatability_2019_11_27.csv',
#'urad', pdf_title='M1K1/M1K1-Pitch-Repeatability-PreInstallCheckoutPlots.pdf')

#pf.plot_and_zoom(\
#'/reg/neh/home/sheppard/FlatMirrors/M1K1/M1K1_ScopeFiles/Pitch_1um_adjust_2019_11_27.csv',
#'urad', pdf_title='M1K1/M1K1-Pitch-1umAdjust-PreInstallCheckoutPlots.pdf')
###########################################################################

input('Press <Return> to close')
plt.close('all')
