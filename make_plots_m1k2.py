"""
Script to call plot_functions to make plots for a particular file
"""

import MirrorPlots.plot_functions as pf
import matplotlib.pyplot as plt

# Plot Y HL Data
pf.plot_data(\
'/reg/neh/home/sheppard/FlatMirrors/M1K2/M1K2_ScopeFiles/Y_HL_LimSwitchRpt_2019_10_1.csv',
'um', include_slave=True, gantry_cutoff=True, by_index=True,
move_start_indecesY=[445, 17972, 30600, 45779, 58523],
peak_gantry_indecesY=[3680, 18066, 30910, 45893, 58913],
move_end_indecesY=[14000, 25000, 38000, 54000, 66000])
#hl_roi=[(-4.451, 743.181), (113550, 113560.2,)],
#pdf_title='M1K2-Y-HLPreInstallCheckoutPlots.pdf')

# Plot Y LL Data
#pf.plot_data(\
#'/reg/neh/home/sheppard/FlatMirrors/M1K2/M1K2_ScopeFiles/Y_LL_LimSwitchRpt_2019_10_1.csv',
#'um', include_slave=True, gantry_cutoff=True,
#ll_roi=[(-21.2297, 872.42), (17933, 17942.5)],
#pdf_title='M1K2-Y-LLPreInstallCheckoutPlots.pdf')

# Plot X Data
#pf.plot_data(\
#'/reg/neh/home/sheppard/FlatMirrors/M1K2/M1K2_ScopeFiles/X_LimSwitchRpt_2019_10_1.csv',
#'um', include_slave=True, gantry_cutoff=True,
#hl_roi=[(-14.447, 1234.18), (22588, 22591.5)],
#ll_roi=[(82.6332, 1290.52), (18280.8, 18295.9)],
#pdf_title='M1K2-X-PreInstallCheckoutPlots.pdf')

# Plot Pitch Data
#pf.plot_data(\
#'/reg/neh/home/sheppard/FlatMirrors/M1K2/M1K2_ScopeFiles/Pitch_LimSwitchRpt_2019_10_1.csv',
#'urad', gantry_cutoff=True, hl_roi=[(-17.3134, 406.21), (25898.4, 25898.9)],
#ll_roi=[(13.0417, 497.862), (25653.1, 25654.8)],
#pdf_title='M1K2-Pitch-PreInstallCheckoutPlots.pdf')

input('Press <Return> to close')
plt.close('all')
