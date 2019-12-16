import matplotlib
import numpy as np

def convolve(data, win=5, mode='same'):
    conv = np.convolve(data, np.ones(win)/float(win) , mode).tolist()
    for n in range(win):
        if n%2 == 0:
            conv[n//2*(-1)] = conv[win*(-1)]  
        else:
            conv[n//2] = conv[win] 
    return conv

def get_nearest_value_index(lst, val):
  #return the smallest value of (list - num)
  return np.abs(np.array(lst) - val).argmin()

def dict_merge(*dicts):
    merged = {}
    for d in dicts:
        for k, v in d.items():
            merged[k] = v
    return merged

def merge_dicts_by_key(keys, dicts):
    merged = {}
    for d in dicts:
        for k in d.keys():
            if k in merged:
                merged[k].append(d[k])
            else:
                merged[k] = [d[k]]
    return merged

def fitting_square_method(x, y, dim=1):
    coef = np.polyfit(x, y, dim)
    return np.poly1d(coef)(x)

def set_plot_params(size='small'):
    if size == 'small':
        ls = 20
        ft = 20
    elif size == 'middle':
        ls = 25
        ft = 25
    matplotlib.rc('axes', labelsize=ls)     
    matplotlib.rc('axes', grid=True)     
    matplotlib.rc('axes.grid', axis='y')     
    matplotlib.rc('axes.grid', which='major')     
    matplotlib.rc('grid', linestyle='dashed')     
    matplotlib.rc('grid', linewidth=1)     
    matplotlib.rc('xtick', labelsize=ls)     
    matplotlib.rc('ytick', labelsize=ls)
    matplotlib.rc('legend', fontsize=ft-5)
    matplotlib.rc('legend', edgecolor='k')
    matplotlib.rc('legend', framealpha=1)