import random
import time
#import sys
#import os
def find_1D_peak_n_complexity(array):
    peak = []
    for i in range(len(array)):
        if i == 0:
            if array[i] >= array[i + 1]:
                break
        elif i == len(array) - 1:
            if array[i] >= array[i - 1]:
                break
        else:
            if array[i] >= array[i - 1] and array[i] >= array[i + 1]:             
                break
    else:
        return []
    peak.append(array[i])
    return peak

def find_1D_peak_logn_complexity(array):
    peak = []
    while len(array) != 0:
        array_middle = int(len(array) / 2)
        if array_middle != len(array) - 1 and array[array_middle] <= array[array_middle + 1]:
            array = array[array_middle:]
            continue
        elif array_middle != 0 and array[array_middle] <= array[array_middle - 1]:
            array = array[:array_middle]
            continue
        else:
            peak.append(array[array_middle])
            break
    return peak

