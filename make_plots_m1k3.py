"""
Script to call plot_functions to make plots for a particular file
"""

import MirrorPlots.plot_functions as pf
import matplotlib.pyplot as plt

# Plot Y HL Data
#pf.plot_data(\
#'/reg/neh/home/sheppard/FlatMirrors/M1K3/M1K3_ScopeFiles/Y_HighLimSwitchRpt_2019_9_18.csv',
#'um', include_slave=True, gantry_cutoff=True, by_index=True)
#pdf_title='M1K3-Y-HLPreInstallCheckoutPlots.pdf',
#hl_roi=[(136.77, 936.155), (122494, 122501)])

# Plot Y LL Data
#pf.plot_data(\
#'/reg/neh/home/sheppard/FlatMirrors/M1K3/M1K3_ScopeFiles/Y_LowLimSwitchRpt_2019_9_18.csv',
#'um', include_slave=True, gantry_cutoff=True, by_index=True,
#move_start_indecesY=[1007, 3810, 28454, 30859, 38104, 39747, 47399, 49759, 58401, 60170],
#peak_gantry_indecesY=[1658, 8895, 28499, 30936, 38153, 39835, 47455, 49845, 58451, 60258],
#move_end_indecesY=[2857, 15204, 30272, 33004, 39686, 41550, 49285, 51770, 60036, 62131])
#ll_roi=[(140.75, 683.165), (8699.25, 8705.95)],
#pdf_title='M1K3-Y-LLPreInstallCheckoutPlots.pdf')

# Plot Y 1 um adjustment

# Plot X Data
#pf.plot_data(\
#'/reg/neh/home/sheppard/FlatMirrors/M1K3/M1K3_ScopeFiles/X_LimSwitchRpt_2019_9_18.csv',
#'um', include_slave=True, gantry_cutoff=True, by_index=True,
#move_start_indecesX=[636, 11706, 21748, 30316, 39502, 49899, 60491, 70907, 80680, 90690, 101072],
#peak_gantry_indecesX=[661, 11832, 21786, 30359, 39595, 50987, 60523, 70973, 80712, 91255, 101439],
#move_end_indecesX=[4180, 16000, 26606, 34532, 44272, 53025, 64010, 74018, 84000, 93982, 102520])
#hl_roi=[(14.908, 924.665), (23629.5, 23633.1)],
#ll_roi=[(133.632, 1021.8), (15973.6, 15980)],
#pdf_title='M1K3-X-PreInstallCheckoutPlots.pdf')

# Plot Pitch Data
#pf.plot_data(\
#'/reg/neh/home/sheppard/FlatMirrors/M1K3/M1K3_ScopeFiles/Pitch_LimSwitchRpt_2019_9_18.csv',
#'urad', gantry_cutoff=True, hl_roi=[(22.6282, 673.76), (56329.8, 56339.5)],
#ll_roi=[(123.2, 763.308), (54032.7, 54079.4)],
#pdf_title='M1K3-Pitch-PreInstallCheckoutPlots.pdf')

input('Press <Return> to close')
plt.close('all')
