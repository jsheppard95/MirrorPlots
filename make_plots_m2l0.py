"""
make_plots_m2l0.py
Script to call plot_functions to make plots for a particular file
"""

import MirrorPlots.plot_functions as pf
import matplotlib.pyplot as plt

# Post-Install:
##############################################################################
# Y Motion

pf.plot_data('/reg/neh/home/sheppard/FlatMirrors/Post-Install-Scope-Files/M2L0/Y_repeatability_2020_1_13.csv',
             'um', gantry_cutoff=True, include_slave=True, pdf_title='M2L0/M2L0-Y-Repeatability.pdf')

##############################################################################
# X Motion

#pf.plot_data('/reg/neh/home/sheppard/FlatMirrors/Post-Install-Scope-Files/M2L0/X_repeatability_2020_1_13.csv',
#             'um', gantry_cutoff=True, include_slave=True, pdf_title='M2L0/M2L0-X-Repeatability.pdf')

##############################################################################
# Pitch Motion

#pf.plot_data('/reg/neh/home/sheppard/FlatMirrors/Post-Install-Scope-Files/M2L0/Pitch-repeatability-2019_12_18.csv',
#             'urad', gantry_cutoff=True, include_slave=True, pdf_title='M2L0/M2L0-Pitch-Repeatability.pdf')
#pitch_data = pf.get_data('/reg/neh/home/sheppard/FlatMirrors/Post-Install-Scope-Files/M2L0/Pitch-repeatability-2019_12_18.csv',
#                         22, gantry_cutoff=True)
#pitch_tvals = pitch_data[0][0][38297: 40846]
#pitch_actpos = pitch_data[0][1][38297: 40846]
#pitch_setpos = pitch_data[0][2][38297: 40846]
#rms_error = pf.calculate_rms_error(pitch_tvals, pitch_actpos, pitch_setpos)
#print(rms_error)

input('Press <Return> to close')
plt.close('all')
