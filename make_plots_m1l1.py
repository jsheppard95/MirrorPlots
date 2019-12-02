"""
Script to call plot_functions to make plots for a particular file
"""

import MirrorPlots.plot_functions as pf

# Y Motion
# Y PL: x_range = (2027.5, 2841.9), y_range = (123524, 123537)
# Y NL: x_range = (254.28, 886.88), y_range = (8779.7, 8787.55)
#pf.plot_data(\
#'/reg/neh/home/sheppard/FlatMirrors/M1L1/M1L1_ScopeFiles/Y_LimSwitchRpt.csv',
#'um', gantry_cutoff=True, by_index=True,
#move_start_indecesY=[350, 37450, 40490, 52000, 54184, 63887, 65790, 73819, 75681, 88500],
#peak_gantry_indecesY=[16242, 38812, 41489, 52684, 55034, 64380, 66652, 74316, 76546, 139980],
#move_end_indecesY=[26576, 40000, 43205, 53756, 56210, 65515, 67814, 75396, 77604, 191412])
#pdf_title='M1L1YupPre-InstallCheckoutPlots.pdf')

# Plot Y 1 um Adjustment
#pf.plot_and_zoom(\
#'/reg/neh/home/sheppard/FlatMirrors/M1L1/M1L1_ScopeFiles/Y_1umAdj.csv',
#'um', pdf_title='M1L1-Y-1umAdjust-PreInstallCheckoutPlots.pdf')

# Plot Y Repeatability:
#pf.plot_and_zoom(\
#'/reg/neh/home/sheppard/FlatMirrors/M1L1/M1L1_ScopeFiles/Y_1umAdj.csv',
#'um', pdf_title='M1L1-Y-1umAdjustRptAbility-PreInstallCheckoutPlots.pdf')

# X Motion
# X PL: x_range = (17.471, 931.71), y_range = (24686.6, 24690.3)
# X NL: x_range = (119.4, 1150.3), y_range = (16514.8, 16515)
#pf.plot_data(\
#'/reg/neh/home/sheppard/FlatMirrors/M1L1/M1L1_ScopeFiles/X_LimSwitchRpt.csv',
#'um', gantry_cutoff=True, by_index=True,
#move_start_indecesX=[1019, 9200, 21807, 30587, 41028, 51096, 60075, 71721, 81189, 92306],
#peak_gantry_indecesX=[1062, 10486, 21860, 31659, 42854, 51125, 60284, 72830, 81400, 92575],
#move_end_indecesX=[3964, 14004, 27478, 36464, 45028, 54558, 63828, 74974, 84900, 105930])
#ll_roi=[(119.4, 1150.3), (16514.8, 16515)],
#hl_roi=[(17.471, 931.71), (24686.6, 24690.3)])

# Plot X 1 um Adjustment
#pf.plot_and_zoom(\
#'/reg/neh/home/sheppard/FlatMirrors/M1L1/M1L1_ScopeFiles/X_1umAdj.csv',
#'um', pdf_title='M1L1-X-1umAdjust-PreInstallCheckoutPlots.pdf')

# Plot X Repeatability
#pf.plot_and_zoom(\
#'/reg/neh/home/sheppard/FlatMirrors/M1L1/M1L1_ScopeFiles/X_1umAdj.csv',
#'um', pdf_title='M1L1-X-1umAdjustRptAbility-PreInstallCheckoutPlots.pdf')

# Pitch Motion
# Pitch PL: x_range = (49.47, 762.249), y_range = (50185.6, 50200.7)
# Pitch NL: x_range = (142.875, 849.323), y_range = (47907.1, 47933.5)
#plot_functions.plot_data(\
#'/reg/neh/home/sheppard/FlatMirrors/M1L1/M1L1_ScopeFiles/Pitch_LimSwitchRpt.csv',
#'urad', gantry_cutoff=True, pdf_title='M1L1PitchPre-InstallCheckoutPlots.pdf')

# Plot Pitch 1 um Adjustment
#pf.plot_and_zoom(\
#'/reg/neh/home/sheppard/FlatMirrors/M1L1/M1L1_ScopeFiles/Pitch_1umAdj.csv',
#'urad', pdf_title='M1L1/M1L1-Pitch-1umAdjust-PreInstallCheckoutPlots.pdf')

pf.plot_and_zoom(\
'/reg/neh/home/sheppard/FlatMirrors/M1L1/M1L1_ScopeFiles/Pitch_1umAdj.csv',
'urad', pdf_title='M1L1/M1L1-Pitch-1umAdjustRptAbility-PreInstallCheckoutPlots.pdf')

input('Press <Return> to close')
