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
#'um', include_slave=True, gantry_cutoff=True,
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
pf.plot_enc_noise(\
'/reg/neh/home/sheppard/FlatMirrors/M1K1/M1K1_ScopeFiles/Y_EncNoise_2019_10_23.csv',
'um')
###########################################################################

###########################################################################
# X Motion:

# Plot X HL Data
#pf.plot_data(\
#'/reg/neh/home/sheppard/FlatMirrors/M1K1/M1K1_ScopeFiles/X_HL_rpt_2019_10_23.csv',
#'um', include_slave=True, gantry_cutoff=True,
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
#'/reg/neh/home/sheppard/FlatMirrors/M1K2/M1K2_ScopeFiles/Pitch_LimSwitchRpt_2019_10_1.csv',
#'urad', gantry_cutoff=True, hl_roi=[(-17.3134, 406.21), (25898.4, 25898.9)],
#ll_roi=[(13.0417, 497.862), (25653.1, 25654.8)],
#pdf_title='M1K2-Pitch-PreInstallCheckoutPlots.pdf')
###########################################################################

input('Press <Return> to close')
plt.close('all')
