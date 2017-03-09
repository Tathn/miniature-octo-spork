'''
 [a,b,c,d,e,f,g,h,i]
  1 2 3 4 5 6 7 8 9
 a-i are numbers
 Position 2 is a peak if and only if b >= a and b >= c.
 Position 9 is a peak if i >= h.
 Position 1 is a peak if a >=b.
 Problem: Find a peak.
'''

def find_1D_peak_n_complexity(values):
    '''Straightforward algorithm implementation. Worst case complexity - O(n) - goes through entire list
    
    Args:
        values(list of str): List of values in which we want to find a peak

    Returns:
        int: Value of peak that was found
    '''

    for i in range(len(values)):
        if i == 0:
            if values[i] >= values[i + 1]:
                break
        elif i == len(values) - 1:
            if values[i] >= values[i - 1]:
                break
        else:
            if values[i] >= values[i - 1] and values[i] >= values[i + 1]:             
                break
    return values[i]

def find_1D_peak_logn_complexity(values):
    '''Divide & Conquer implementation. Worst case complexity - O(log2 n)
    
    Args:
        values(list of str): List of values in which we want to find a peak

    Returns:
        int: Value of peak that was found
    '''
    
    while len(values) != 0:
        values_middle = int(len(values) / 2)
        if values_middle != len(values) - 1 and values[values_middle] < values[values_middle + 1]:
            values = values[values_middle:]
            continue
        elif values_middle != 0 and values[values_middle] < values[values_middle - 1]:
            values = values[:values_middle]
            continue
        else:
            break
    return values[values_middle]

'''
        2D version

        ^  x,c,x,x,
        |  b,a,d,x,
 n rows |  x,e,x,x,
        |  x,x,x,x
        +---------->
         m columns

 'a' is a 2D-peak if and only if a >= b, a >= d, a >= c, a >= e
'''

def find_2D_peak_mn_complexity(values, start_row = None, start_column = None):
    '''Greedy Ascent Algorithm (Hill Climbing). Worst case complexity - O(nm)
    
    Args:
        values(list of str): List of values in which we want to find a peak
        start_row(int, optional): Row from which function will start search for a peak. Will become lists middle if left empty.
        start_column(int, optional): Column from which function will start search for a peak. Will become lists middle if left empty.

    Returns:
        int: Value of peak that was found
    '''

    current_position_row = len(values)//2 if start_row == None else start_row
    current_position_column = len(values[0])//2 if start_column == None else start_column
    for _ in range(len(values) * len(values[0])):
        possible_peak = values[current_position_row][current_position_column]
        if current_position_row != 0 and possible_peak < values[current_position_row - 1][current_position_column]:
            current_position_row -= 1
            continue
        elif current_position_row != len(values[current_position_row]) - 1 and possible_peak < values[current_position_row + 1][current_position_column]:
            current_position_row += 1
            continue
        elif current_position_column != 0 and possible_peak < values[current_position_row][current_position_column - 1]:
            current_position_column -= 1
            continue
        elif current_position_column != len(values[current_position_column]) - 1 and possible_peak < values[current_position_row][current_position_column + 1]:
            current_position_column += 1
            continue
        else:
            break
    return values[current_position_row][current_position_column]

def find_2D_peak_mlogn_complexity(values):
    '''Divide & Conquer implementation. Worst case complexity - O(m log2 n)
    
    Selects middle column of list and gets maximum value from it.
    Then depending on values to the left/right of that max chooses to slice left/right side of array or return current maximum value.

    Args:
        values(list of str): List of values in which we want to find a peak

    Returns:
        int: Value of peak that was found
    '''

    peak_found = False
    global_max = None # maximum value of currently selected column
    if len(values) == 0: return None
    while not(peak_found):
        middle_column = len(values[0])//2 
        global_max_column = middle_column
        for itr in range(len(values)): # gets maximum value from middle column of array and saves it for later use
            if global_max == None or values[itr][global_max_column] > global_max:
                global_max = values[itr][middle_column]
                global_max_row = itr
        if middle_column == 0: # if lists lenght is == 1 we already have our peak in our maximum so we break
            break
        if global_max_column != 0 and global_max < values[global_max_row][global_max_column - 1]:
            values = [a[:middle_column] for a in values] # cut off columns to the right of middle column
            continue
        elif global_max_column != len(values[0]) - 1 and global_max < values[global_max_row][global_max_column + 1]:
            values = [a[middle_column:] for a in values] # cut off columns to the left of middle column
            continue
        else: # if our max value(global_max) from current middle_column is not less than values to its left and right then we have our peak
            break 
    return global_max

''' TESTS
from random import randint
from os import system
system('cls')
array1d = [randint(100,999) for x in range(10)]
print("\n1D Array")
print("--------------------------------------------------")
for a in array1d:
    print(a,end=" ")
print("\n--------------------------------------------------")
print("1D Peak(n complexity) =",find_1D_peak_n_complexity(array1d))
print("1D Peak(logn complexity) =",find_1D_peak_logn_complexity(array1d))
print("--------------------------------------------------")

array2d = [[randint(100,999) for x in range(10)] for y in range(10)]
print("\n2D Array")
print("--------------------------------------------------")
for a in array2d:
    print(a)
print("--------------------------------------------------")
print("2D Peak(mn complexity) =",find_2D_peak_mn_complexity(array2d))
print("2D Peak(mlogn complexity) =",find_2D_peak_mlogn_complexity(array2d))
print("--------------------------------------------------\n")