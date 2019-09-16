"""
Module containing utility functions used in HOMS plot generation script
"""

import matplotlib.pyplot as plt
import numpy as np

# TODO:
# - Overlay velocity and gantry difference - watch out for time array sizes
# - Function to generate PDF
# - Investigate slave axis data


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
    act_velo_slave = []
    pos_diff_slave = []

    with open(fname, 'r') as f:
        line = f.readline()
        cnt = 1
        while line:
            line = f.readline()
            cnt += 1
            if cnt >= start_line:
                line_array = line.split()
                try:
                    act_pos.append(float(line_array[1]))
                    set_pos.append(float(line_array[3]))
                    act_velo.append(float(line_array[5]))
                    set_velo.append(float(line_array[7]))
                    pos_diff.append(float(line_array[9]))
                    x_gantry.append(float(line_array[11]))
                    y_gantry.append(float(line_array[13]))
                    act_pos_slave.append(float(line_array[15]))
                    act_velo_slave.append(float(line_array[17]))
                    pos_diff_slave.append(float(line_array[19]))
                except:
                    pass

    # Going to numpy arrays!
    act_pos = np.asarray(act_pos)
    set_pos = np.asarray(set_pos)
    act_velo = np.asarray(act_velo)
    set_velo = np.asarray(set_velo)
    pos_diff = np.asarray(pos_diff)
    x_gantry = np.asarray(x_gantry)
    y_gantry = np.asarray(y_gantry)
    act_pos_slave = np.asarray(act_pos_slave)
    act_velo_slave = np.asarray(act_velo_slave)
    pos_diff_slave = np.asarray(pos_diff_slave)

    tvals = np.linspace(0, delta_t, len(act_pos))

    if gantry_cutoff:
        gantry_stop_idx = len(act_pos) // 5 # can round
        x_gantry = x_gantry[: gantry_stop_idx]
        y_gantry = y_gantry[: gantry_stop_idx]

    tvals_gantry = np.linspace(0, delta_t, len(x_gantry))

    nc_data = np.asarray([tvals, act_pos, set_pos, act_velo, set_velo,
                          pos_diff, act_pos_slave, act_velo_slave,
                          pos_diff_slave])
    gantry_data = np.asarray([tvals_gantry, x_gantry, y_gantry])

    if debug:
        print('Measurement time: %s s' % delta_t)

        print('Number of Pos Points:', len(act_pos))
        print('Number of Velo Points:', len(act_velo))
        print('Number of POSDIFF Points:', len(pos_diff))
        print('Number of X gantry Points:', len(x_gantry))
        print('Number of Y gantry Points:', len(y_gantry))
        print('NC var to PLC var Ratio:', len(act_velo)/len(x_gantry))

    return (nc_data, gantry_data)


def plot_data(filename, nc_unit, gantry_unit='nm', gantry_cutoff=False,
              by_index=False, debug=False):
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

    ganrty_cutoff : bool
        cut off gantry data as it was overfilled

    by_index : bool
        plot y vs index instead of time

    debug : bool
        print some debug information such as array sizes
    """
    # data in format ([TIME, ACTPOS, SETPOS, ACTVELO, SETVELO, POSDIFF],
    #                 [TIME_GANTRY, X_GANTRY, Y_GANTRY])
    all_data = get_data(filename, 22, gantry_cutoff=gantry_cutoff, debug=debug)
    nc_data = all_data[0]
    gantry_data = all_data[1]

    # First make double plots: actual and set vs time
    # ACTPOS, SETPOS vs TIME
    make_double_plot(nc_data[0], nc_data[1], nc_data[2], 'Actual Position',
                     'Set Position', 'Position (%s)' % nc_unit,
                     'Actual Position and Set Position', by_index=by_index)
    # ACTVELO, SETVELO vs TIME
    make_double_plot(nc_data[0], nc_data[3], nc_data[4], 'Actual Velocity',
                     'Set Velocity', 'Velocity (%s/s)' % nc_unit,
                     'Actual Velocity and Set Velocity', by_index=by_index)
    # Now make doubel plots: POSDIFF vs TIME
    make_single_plot(nc_data[0], nc_data[5], 'Position Difference',
                     'Position Difference (%s)' % nc_unit,
                     'Position Difference', by_index=by_index)

    # Make Ganrty plots:
    # X Gantry
    make_single_plot(gantry_data[0], gantry_data[1], 'X Gantry Difference',
                     'X Gantry Difference (%s)' % gantry_unit,
                     'X Gantry Difference', by_index=by_index)

    # Y Gantry
    make_single_plot(gantry_data[0], gantry_data[2], 'Y Gantry Difference',
                     'Y Gantry Difference (%s)' % gantry_unit,
                     'Y Gantry Difference', by_index=by_index)
    # ACTPOS, POSDIFF vs TIME
    make_overlay_plot(nc_data[0], nc_data[1], nc_data[5],
                      'Actual Position (%s)' % nc_unit,
                      'Position Difference (%s)' % nc_unit, 'tab:red',
                      'tab:blue', 'Actual Position and Position Difference',
                      by_index=by_index)


def make_overlay_plot(time, y1, y2, y1_axis_label, y2_axis_label, y1_color,
                      y2_color, plot_label, by_index=False):
    f, ax1 = plt.subplots()
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
    f.show()


def make_double_plot(time, y1, y2, y1_label, y2_label, y_axis_label, plot_label,
                     by_index=False):
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
    """
    f, ax = plt.subplots()
    if by_index:
        ax.plot(y1, label=y1_label)
        ax.plot(y2, label=y2_label)
        ax.set_xlabel('Index, (Integer)')
    else:
        ax.plot(time, y1, label=y1_label)
        ax.plot(time, y2, label=y2_label)
        ax.set_xlabel('Time (s)')
    ax.set_ylabel(y_axis_label)
    ax.legend(loc='best')
    ax.set_title(plot_label)
    f.show()


def make_single_plot(time, y, y_label, y_axis_label, plot_label, by_index=False):
    """
    Function to make a basic plot of y vs t

    Parameters:
    ----------
    time : numpy array
        time in seconds

    y : numpy array
        y axis data, i.e act_position, act_velocity. etc.

    y_axis_label : str
        y vs t curve label

    plot_label : str
        plot title

    by_index : bool, opt :
        plot vs index instead of time
    """
    f, ax = plt.subplots()
    if by_index:
        ax.plot(y, label=y_label)
        ax.set_xlabel('Index, (Integer)')
    else:
        ax.plot(time, y, label=y_label)
        ax.set_xlabel('Time (s)')
    ax.set_ylabel(y_axis_label)
    ax.legend(loc='best')
    ax.set_title(plot_label)
    f.show()
