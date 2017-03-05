import random
import time
#import sys
#import os
def find_1D_peak_n_complexity(numbers):
    peak_found = False
    for number in range(len(numbers)):
        if number == 0:
            if numbers[number] >= numbers[number+1]:
                peak_found = True
                break
        elif number == len(numbers)-1:
            if numbers[number] >= numbers[number-1]:
                peak_found = True
                break
        else:
            if numbers[number] >= numbers[number-1] and numbers[number] >= numbers[number+1]:
                peak_found = True
                break
    return peak_found

def find_1D_peak_logn_complexity(numbers):
    peak_found = False
    while not(peak_found):
        array_middle = int(len(numbers) / 2)
        if array_middle != len(numbers) - 1 and numbers[array_middle] < numbers[array_middle + 1]:
            numbers = numbers[:array_middle]
            continue
        elif array_middle != len(numbers) and numbers[array_middle] < numbers[array_middle - 1]:
            numbers = numbers[array_middle :]
            continue
        else:
            peak_found = True
            break
    return peak_found

#start_time = time.time()
#array = [][]
#for a in range(10):
#    for b in range(10):
#    array.append(b)
#find_1D_peak_n_complexity(array)
#print("\nPeak found in: \n--- %s seconds ---" % (time.time() - start_time))
#print()