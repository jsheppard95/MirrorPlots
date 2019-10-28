"""
Module containing utility functions used in HOMS plot generation script

Author: J. Sheppard
"""

import matplotlib.pyplot as plt
import numpy as np
import datetime
from matplotlib.backends.backend_pdf import PdfPages
import ntpath


def get_data(fname, start_line, gantry_cutoff=False, debug=False):
    """
    Function to read data file and store data
    Since NC variable arrays are 5x longer that PLC variable arrays, will
    return tuple (NCDataMatrix, GantryDataMatrix)

    Parameters
    ----------
    fname : string
        file name to parse
        file format at start_line is:
        #, ACTPOS, #, SETPOS, # ACTVELO, #, SETVELO, #, POSDIFF, #, XGANTRY,
        #, YGANTRY, #, ACTPOS-SLAVE, #, ACTVELO-SLAVE, #, POSDIFF-SLAVE

    start_line : int
        line number where actual data begins

    include_slave : bool, opt
        slave axis data inlcuded

    gantry_cutoff : bool, opt
        gantry data cut off

    debug : bool, opt
        display debug info such as measurement time, length of arrays
    """
    # Read file and get measurement time
    f = open(fname, 'r')
    f.readline() # line 1
    f.readline() # line 2

    start_time_line = f.readline() # line 3
    start_time_array = start_time_line.split()
    end_time_line = f.readline() # line 4
    end_time_array = end_time_line.split()

    f.close()

    start_time_split = start_time_array[6].split(':')
    end_time_split = end_time_array[6].split(':')

    start_hr = float(start_time_split[0])
    start_min = float(start_time_split[1])
    start_sec = float(start_time_split[2])
    end_hr = float(end_time_split[0])
    end_min = float(end_time_split[1])
    end_sec = float(end_time_split[2])
    start = (start_hr*3600) + (start_min*60.0) + start_sec
    end = (end_hr*3600) + (end_min*60.0) + end_sec

    delta_t = end - start

    # Now read file for data
    act_pos = []
    set_pos = []
    act_velo = []
    set_velo = []
    pos_diff = []
    x_gantry = []
    y_gantry = []
    act_pos_slave = []
    set_pos_slave = []
    act_velo_slave = []
    set_velo_slave = []
    pos_diff_slave = []

    with open(fname, 'r') as f:
        line = f.readline()
        cnt = 1
        while line:
            line = f.readline()
            cnt += 1
            if cnt >= start_line:
                line_array = line.split('\t')
                try:
                    act_pos.append(float(line_array[1]))
                    set_pos.append(float(line_array[3]))
                    act_velo.append(float(line_array[5]))
                    set_velo.append(float(line_array[7]))
                    pos_diff.append(float(line_array[9]))
                    act_pos_slave.append(float(line_array[11]))
                    set_pos_slave.append(float(line_array[13]))
                    act_velo_slave.append(float(line_array[15]))
                    set_velo_slave.append(float(line_array[17]))
                    pos_diff_slave.append(float(line_array[19]))
                    x_gantry.append(float(line_array[21]))
                    y_gantry.append(float(line_array[23]))
                except:
                    pass

    # Going to numpy arrays!
    act_pos = np.asarray(act_pos)
    set_pos = np.asarray(set_pos)
    act_velo = np.asarray(act_velo)
    set_velo = np.asarray(set_velo)
    pos_diff = np.asarray(pos_diff)
    act_pos_slave = np.asarray(act_pos_slave)
    set_pos_slave = np.asarray(set_pos_slave)
    act_velo_slave = np.asarray(act_velo_slave)
    set_velo_slave = np.asarray(set_velo_slave)
    pos_diff_slave = np.asarray(pos_diff_slave)
    x_gantry = np.asarray(x_gantry)
    y_gantry = np.asarray(y_gantry)

    tvals = np.linspace(0, delta_t, len(act_pos))

    if gantry_cutoff:
        gantry_stop_idx = len(act_pos) // 5 # can round
        x_gantry = x_gantry[: gantry_stop_idx]
        y_gantry = y_gantry[: gantry_stop_idx]

    tvals_gantry = np.linspace(0, delta_t, len(x_gantry))

    nc_data = np.asarray([tvals, act_pos, set_pos, act_velo, set_velo,
                          pos_diff, act_pos_slave, set_pos_slave,
                          act_velo_slave, set_velo_slave, pos_diff_slave])
    gantry_data = np.asarray([tvals_gantry, x_gantry, y_gantry])

    if debug:
        print('Measurement time: %s s' % delta_t)

        print('Number of tvals Points:', len(tvals))
        print('Number of tvals_gantry Points:', len(tvals_gantry))
        print('Number of Pos Points:', len(act_pos))
        print('Number of Velo Points:', len(act_velo))
        print('Number of POSDIFF Points:', len(pos_diff))
        print('Number of X gantry Points:', len(x_gantry))
        print('Number of Y gantry Points:', len(y_gantry))
        print('Number of Slave Pos Points:', len(act_pos_slave))
        print('Number of Slave Velo Points:', len(act_velo_slave))
        print('Number of Slave POSDIFF Points:', len(pos_diff_slave))

        print('NC var to PLC var Ratio:', len(act_velo)/len(x_gantry))

    return (nc_data, gantry_data)


def plot_data(filename, nc_unit, gantry_unit='nm', include_slave=False,
              gantry_cutoff=False, by_index=False, debug=False,
              pdf_title=None, ll_roi=None, hl_roi=None,
              move_start_indecesX=None, peak_gantry_indecesX=None,
              move_end_indecesX=None,
              move_start_indecesY=None, peak_gantry_indecesY=None,
              move_end_indecesY=None):
    """
    Function to plot NC Data: ACTPOS, SETPOS, ACTVELO, SETVELO, POSDIFF vs TIME

    Parameters
    ----------
    filename : str
        path to TwinCAT generated csv file

    nc_unit : str
        engineering unit in TwinCAT NC paramaters

    gantry_unit : str
        unit for gantry data

    ganrty_cutoff : bool, opt
        cut off gantry data as it was overfilled

    by_index : bool, opt
        plot y vs index instead of time

    debug : bool, opt
        print some debug information such as array sizes

    pdf_title : str, opt
        Add figures generated to a PDF with this title

    ll_roi : list, opt
        list with two tuples [(xmin, xmax), (ymin, ymax)]
    """
    # data in format ([TIME, ACTPOS, SETPOS, ACTVELO, SETVELO, POSDIFF,
    #                  ACTPOS-Slave, SETPOS-Slave, ACTVELO-Slave,
    #                  SETVELO-Slave, POSDIFF-Slave],
    #                 [TIME_GANTRY, X_GANTRY, Y_GANTRY])
    all_data = get_data(filename, 22, gantry_cutoff=gantry_cutoff, debug=debug)
    nc_data = all_data[0]
    gantry_data = all_data[1]

    PLOTS = ['Actual Position', 'Set Position', 'Actual Velocity',
             'Set Velocity', 'Position Difference', 'X Gantry Difference',
             'Y Gantry Difference']

    # First make double plots: actual and set vs time
    # ACTPOS, SETPOS vs TIME
    make_plot(nc_data[0], nc_data[1], 'Actual Position',
              'Position (%s)' % nc_unit, 'Actual Position and Set Position',
              y2=nc_data[2], y2_label='Set Position', by_index=by_index)
    # ACTVELO, SETVELO vs TIME
    make_plot(nc_data[0], nc_data[3], 'Actual Velocity',
              'Velocity (%s/s)' % nc_unit, 'Actual Velocity and Set Velocity',
              y2=nc_data[4], y2_label='Set Velocity', by_index=by_index)
    # Now make single plot: POSDIFF vs TIME
    make_plot(nc_data[0], nc_data[5], 'Position Difference',
              'Position Difference (%s)' % nc_unit, 'Position Difference',
              by_index=by_index)

    # Make Ganrty plots:
    # X Gantry
    make_plot(gantry_data[0], gantry_data[1], 'X Gantry Difference',
              'X Gantry Difference (%s)' % gantry_unit, 'X Gantry Difference',
              by_index=by_index)

    # Y Gantry
    make_plot(gantry_data[0], gantry_data[2], 'Y Gantry Difference',
              'Y Gantry Difference (%s)' % gantry_unit, 'Y Gantry Difference',
              by_index=by_index)
    # ACTPOS, POSDIFF vs TIME
    make_overlay_plot(nc_data[0], nc_data[1], nc_data[5],
                      'Actual Position (%s)' % nc_unit,
                      'Position Difference (%s)' % nc_unit, 'tab:red',
                      'tab:blue', 'Actual Position and Position Difference',
                      by_index=by_index)
    if hl_roi:
        make_plot(nc_data[0], nc_data[1], 'Actual Position',
                  'Position (%s)' % nc_unit,
                  'Actual Position and Set Position - Positive Limits',
                  y2=nc_data[2], y2_label='Set Position', x_range=hl_roi[0],
                  y_range=hl_roi[1], by_index=by_index)
    if ll_roi:
        make_plot(nc_data[0], nc_data[1], 'Actual Position',
                  'Position (%s)' % nc_unit,
                  'Actual Position and Set Position - Negative Limits',
                  y2=nc_data[2], y2_label='Set Position', x_range=ll_roi[0],
                  y_range=ll_roi[1], by_index=by_index)
    # Make Slave plots
    if include_slave:
        # Slave ACTPOS, SETPOS vs TIME
        make_plot(nc_data[0], nc_data[6], 'Slave Actual Position',
                  'Position (%s)' % nc_unit,
                  'Slave Actual Position and Set Position', y2=nc_data[7],
                  y2_label='Slave Set Position', by_index=by_index)
        # Slave ACTVELO, SETVELO vs TIME
        make_plot(nc_data[0], nc_data[8], 'Slave Actual Velocity',
                  'Velocity (%s/s)' % nc_unit,
                  'Slave Actual Velocity and Set Velocity', y2=nc_data[9],
                  y2_label='Slave Set Velocity', by_index=by_index)
        # Slave POSDIFF vs TIME
        make_plot(nc_data[0], nc_data[10], 'Slave Position Difference',
                  'Position Difference (%s)' % nc_unit,
                  'Slave Position Difference', by_index=by_index)

    # Make PDF:
    FIGSIZE=(11.69, 8.27)
    if pdf_title:
        with PdfPages(pdf_title) as pdf:
            # First make title page:
            date = datetime.datetime.now()
            firstPage = plt.figure(figsize=FIGSIZE)
            firstPage.clf()
            firstPage.text(0.5, 0.5, ntpath.basename(filename) + '\n',
                           transform=firstPage.transFigure, size=24,
                           ha="center")
            firstPage.text(0.5, 0.5, date, transform=firstPage.transFigure,
                           size=20, ha="center")
            pdf.savefig()
            plt.close()
            # Now save figures - one per page
            # ACTPOS, SETPOS vs TIME
            make_plot(nc_data[0], nc_data[1], 'Actual Position',
                      'Position (%s)' % nc_unit,
                      'Actual Position and Set Position', y2=nc_data[2],
                      y2_label='Set Position', show=False, figsize=FIGSIZE)

            pdf.savefig()
            # ACTVELO, SETVELO vs TIME
            make_plot(nc_data[0], nc_data[3], 'Actual Velocity',
                             'Velocity (%s/s)' % nc_unit,
                             'Actual Velocity and Set Velocity', y2=nc_data[4],
                             y2_label='Set Velocity', show=False, figsize=FIGSIZE)
            pdf.savefig()
            # POSDIFF vs TIME
            make_plot(nc_data[0], nc_data[5], 'Position Difference',
                      'Position Difference (%s)' % nc_unit,
                      'Position Difference', show=False, figsize=FIGSIZE)
            pdf.savefig()
            make_overlay_plot(nc_data[0], nc_data[1], nc_data[5],
                              'Actual Position (%s)' % nc_unit,
                              'Position Difference (%s)' % nc_unit, 'tab:red',
                              'tab:blue',
                              'Actual Position and Position Difference',
                              show=False, figsize=FIGSIZE)
            pdf.savefig()
            # X Gantry
            make_plot(gantry_data[0], gantry_data[1], 'X Gantry Difference',
                      'X Gantry Difference (%s)' % gantry_unit,
                      'X Gantry Difference', show=False, figsize=FIGSIZE)
            pdf.savefig()
            # Y Gantry
            make_plot(gantry_data[0], gantry_data[2], 'Y Gantry Difference',
                      'Y Gantry Difference (%s)' % gantry_unit,
                      'Y Gantry Difference', show=False, figsize=FIGSIZE)
            pdf.savefig()
            if hl_roi:
                make_plot(nc_data[0], nc_data[1], 'Actual Position',
                          'Position (%s)' % nc_unit,
                          'Actual Position and Set Position - Positive Limits',
                          y2=nc_data[2], y2_label='Set Position',
                          x_range=hl_roi[0], y_range=hl_roi[1], show=False,
                          figsize=FIGSIZE)
                pdf.savefig()
            if ll_roi:
                make_plot(nc_data[0], nc_data[1], 'Actual Position',
                          'Position (%s)' % nc_unit,
                          'Actual Position and Set Position - Negative Limits',
                          y2=nc_data[2], y2_label='Set Position',
                          x_range=ll_roi[0], y_range=ll_roi[1], show=False,
                          figsize=FIGSIZE)
                pdf.savefig()
            if include_slave:
                # Slave ACTPOS, SETPOS vs TIME
                make_plot(nc_data[0], nc_data[6], 'Slave Actual Position',
                          'Position (%s)' % nc_unit,
                          'Slave Actual Position and Set Position',
                          y2=nc_data[7], y2_label='Slave Set Position',
                          show=False, figsize=FIGSIZE)
                pdf.savefig()
                # Slave ACTVELO, SETVELO vs TIME
                make_plot(nc_data[0], nc_data[8], 'Slave Actual Velocity',
                          'Velocity (%s)' % nc_unit,
                          'Slave Actual Velocity and Set Velocity',
                          y2=nc_data[9], y2_label='Slave Set Velocity',
                          show=False, figsize=FIGSIZE)
                pdf.savefig()
                # Slave POSDIFF vs TIME
                make_plot(nc_data[0], nc_data[10], 'Slave Position Difference',
                          'Position Difference (%s)' % nc_unit,
                          'Slave Position Difference', show=False, figsize=FIGSIZE)
                pdf.savefig()
    if peak_gantry_indecesX:
        # Calculate X gantry
        calculate_gantry_err(gantry_data[1], move_start_indecesX,
                             peak_gantry_indecesX, move_end_indecesX)
    if peak_gantry_indecesY:
        # Calculate Y gantry
        calculate_gantry_err(gantry_data[2], move_start_indecesY,
                             peak_gantry_indecesY, move_end_indecesY)


def make_overlay_plot(time, y1, y2, y1_axis_label, y2_axis_label, y1_color,
        y2_color, plot_label, by_index=False, show=True, figsize=None):
    f, ax1 = plt.subplots(figsize=figsize)
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel(y1_axis_label, color=y1_color)
    if by_index:
        ax1.plot(y1, color=y1_color)
    else:
        ax1.plot(time, y1, color=y1_color)
    ax1.tick_params(axis='y', labelcolor=y1_color)
    ax2 = ax1.twinx()
    ax2.set_ylabel(y2_axis_label, color=y2_color)
    if by_index:
        ax2.plot(y2, color=y2_color)
    else:
        ax2.plot(time, y2, color=y2_color)
    ax2.tick_params(axis='y', labelcolor=y2_color)
    f.tight_layout()
    ax1.set_title(plot_label)
    if show:
        f.show()


def make_plot(time, y1, y1_label, y_axis_label, plot_label, y2=None,
              y2_label=None, x_range=None, y_range=None, by_index=False,
              show=True, figsize=None):
    """
    Function to make a basic plot

    Parameters:
    ----------
    time : numpy array
        time in seconds

    y1 : numpy array
        first y axis data, i.e act_position, act_velocity. etc.

    y2 : numpy array
        second y axis data, i.e set_pos, etc.

    y1_label : str
        first y vs t label

    y2_label : str
        second y_vs t label

    plot_label : str
        plot title

    by_index : bool, opt :
        plot vs index instead of time

    show : bool, opt
        display the figure (pass False for pdf writing)

    figsize : touple, opt
        `matplotib.pyplot.subplots.figsize` optional parameter
    """
    f, ax = plt.subplots(figsize=figsize)
    if by_index:
        ax.plot(y1, label=y1_label)
        if y2 is not None:
            ax.plot(y2, label=y2_label)
        ax.set_xlabel('Index, (Integer)')
    else:
        ax.plot(time, y1, label=y1_label)
        if y2 is not None:
            ax.plot(time, y2, label=y2_label)
        ax.set_xlabel('Time (s)')
    if x_range:
        ax.set_xlim(x_range)
    if y_range:
        ax.set_ylim(y_range)
    ax.set_ylabel(y_axis_label)
    ax.legend(loc='best')
    ax.grid(True)
    ax.set_title(plot_label)
    if show:
        f.show()


def calculate_gantry_err(gantry_data, move_start_indeces, peak_gantry_indeces,
                         move_end_indeces):
    """
    Function to calculate static and dynamic gantry error for given moves

    Parameters:
    -----------
    gantry_data: numpy array
        Gantry data used to calculate errors, either X or Y gantry

    move_start_indeces : list
        List of indeces corresponding to the start of each move in the gantry
        data

    peak_gantry_indeces : list
        List of indeces corresponding to peak gantry values in the gantry data

    move_end_indeces : list
        List of indeces corresponding to the end of each move - i.e when
        encoder noise has settled
    """
    gantry_before1 = gantry_data[:move_start_indeces[0]]
    gantry_after = [] # will be 2D list, inner lists -> gantry after each peak
    # No start after last move_end_indeces value
    for i in range(len(move_start_indeces) - 1):
        gantry_after_data = gantry_data[move_end_indeces[i]: move_start_indeces[i + 1]]
        gantry_after.append(gantry_after_data)

    gantry_after.append(gantry_data[move_end_indeces[len(move_end_indeces) - 1]:])
    # Now have gantry data before and after each peak
    gantry_before1_avg = np.mean(gantry_before1)
    gantry_after_avgs = []
    for data in gantry_after:
        gantry_after_avgs.append(np.mean(data))
    static_errs = []
    static_err1 = gantry_after_avgs[0] - gantry_before1_avg
    static_errs.append(abs(static_err1))
    for i in range(len(gantry_after_avgs) - 1):
        static_err = gantry_after_avgs[i + 1] - gantry_after_avgs[i]
        static_errs.append(abs(static_err))

    dynamic_errs = []
    dynamic_err1 = gantry_data[peak_gantry_indeces[0]] - gantry_before1_avg
    dynamic_errs.append(abs(dynamic_err1))
    for i in range(1, len(peak_gantry_indeces)):
        dynamic_err = gantry_data[peak_gantry_indeces[i]] - gantry_after_avgs[i - 1]
        dynamic_errs.append(abs(dynamic_err))

    # Print results
    print('Static Errors:', static_errs)
    print('Dynamic Errors:', dynamic_errs)


def plot_and_zoom(filename, nc_unit, debug=False, by_index=False,
                  pdf_title=None):
    """
    Function will take in a file with motion repeatability data, make a
    basic position vs time plot, then ask the user to input a ROI and make
    this zoomed plot, then add both to a pdf file

    Parameters
    ----------
    filename : str
        path to TwinCAT generated csv file

    nc_unit : str
        engineering unit in TwinCAT NC parameters

    debug : bool, opt
        print some debug information such as array sizes

    by_index : bool, opt
        plot y vs index instead of time

    pdf_title : str, opt
        Add figures generated to a PDF with this title
    """
    all_data = get_data(filename, 22, gantry_cutoff=True, debug=debug)
    nc_data = all_data[0]
    make_plot(nc_data[0], nc_data[1], 'Actual Position',
              'Position (%s)' % nc_unit, 'Actual Position and Set Position',
              y2=nc_data[2], y2_label='Set Position', by_index=by_index)
    x_low = float(input('Enter X low: '))
    x_high = float(input('Enter X high: '))
    y_low = float(input('Enter Y low: '))
    y_high = float(input('Enter Y high: '))
    roi = [(x_low, x_high), (y_low, y_high)]
    make_plot(nc_data[0], nc_data[1], 'Actual Position',
              'Position (%s)' % nc_unit, 'Actual Position and Set Position',
              y2=nc_data[2], y2_label='Set Position', x_range=roi[0],
              y_range=roi[1], by_index=by_index)
    FIGSIZE=(11.69, 8.27)
    if pdf_title:
        with PdfPages(pdf_title) as pdf:
            # First make title page:
            date = datetime.datetime.now()
            firstPage = plt.figure(figsize=FIGSIZE)
            firstPage.clf()
            firstPage.text(0.5, 0.5, ntpath.basename(filename) + '\n',
                           transform=firstPage.transFigure, size=24,
                           ha="center")
            firstPage.text(0.5, 0.5, date, transform=firstPage.transFigure,
                           size=20, ha="center")
            pdf.savefig()
            plt.close()
            # Now save figures - one per page
            # ACTPOS, SETPOS vs TIME
            make_plot(nc_data[0], nc_data[1], 'Actual Position',
                      'Position (%s)' % nc_unit, 'Actual Position and Set Position',
                      y2=nc_data[2], y2_label='Set Position', show=False,
                      figsize=FIGSIZE)
            pdf.savefig()
            make_plot(nc_data[0], nc_data[1], 'Actual Position',
                      'Position (%s)' % nc_unit, 'Actual Position and Set Position',
                      y2=nc_data[2], y2_label='Set Position', x_range=roi[0],
                      y_range=roi[1], show=False, figsize=FIGSIZE)
            pdf.savefig()

def plot_enc_noise(filename, nc_unit, debug=False, by_index=False):
    all_data = get_data(filename, 22, gantry_cutoff=True, debug=debug)
    nc_data = all_data[0]
    make_plot(nc_data[0], nc_data[1], 'Actual Position',
              'Position (%s)' % nc_unit, 'Actual Position and Set Position',
              y2=nc_data[2], y2_label='Set Position', by_index=by_index)
    fftplot(nc_data[0], nc_data[1])


def fftplot(x_axis, y_axis,
            xlabel=None, left_label='FFT Amplitude',
            remove_dc=True, scale=1.0, alpha=0.7):
    step_x = x_axis[1] - x_axis[0]
    freqs = np.fft.rfftfreq(len(x_axis), step_x)
    fft = np.fft.rfft(x_axis)
    spectra = np.abs(fft) / len(fft)

    # Remove DC component
    if remove_dc:
        data = spectra[1:]
        x_axis = freqs[1:]
    else:
        data = spectra
        x_axis = freqs

    if xlabel is None:
        xlabel = 'Frequency [Hz]'

    f, ax = plt.subplots()
    ax.plot(x_axis, data, alpha=alpha)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(left_label)
    ax.set_xlim(min(x_axis), max(x_axis))
    f.show()
