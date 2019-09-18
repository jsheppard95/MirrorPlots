"""
Script to call plot_functions to make plots for a particular file
"""

import plot_functions

# Y Motion
# Y PL: x_range = (2027.5, 2841.9), y_range = (123524, 123537)
# Y NL: x_range = (254.28, 886.88), y_range = (8779.7, 8787.55)
#plot_functions.plot_data(\
#'/reg/neh/home/sheppard/FlatMirrors/M1L1/M1L1_ScopeFiles/Y_LimSwitchRpt.csv',
#'um', gantry_cutoff=True, pdf_title='M1L1YupPre-InstallCheckoutPlots.pdf')

# X Motion
# X PL: x_range = (17.471, 931.71), y_range = (24686.6, 24690.3)
# X NL: x_range = (119.4, 1150.3), y_range = (16514.8, 16515)
#plot_functions.plot_data(\
#'/reg/neh/home/sheppard/FlatMirrors/M1L1/M1L1_ScopeFiles/X_LimSwitchRpt.csv',
#'um', gantry_cutoff=True, pdf_title='M1L1XupPre-InstallCheckoutPlots.pdf')

# Pitch Motion
# Pitch PL: x_range = (49.47, 762.249), y_range = (50185.6, 50200.7)
# Pitch NL: x_range = (142.875, 849.323), y_range = (47907.1, 47933.5)
plot_functions.plot_data(\
'/reg/neh/home/sheppard/FlatMirrors/M1L1/M1L1_ScopeFiles/Pitch_LimSwitchRpt.csv',
'urad', gantry_cutoff=True, pdf_title='M1L1PitchPre-InstallCheckoutPlots.pdf')

input('Press <Return> to close')
