"""
Script to call plot_functions to make plots for a particular file
"""

import plot_functions

plot_functions.plot_data('TestData_for_PlotScript.csv', 'um',
                         include_slave=True, gantry_cutoff=True,
                         pdf_title='TestData.pdf')
#plot_functions.plot_data('M1L1_X_LimSwitchRpt.csv', 'um', gantry_cutoff=True,
#                         by_index=True, debug=True)
input('Press <Return> to close')
