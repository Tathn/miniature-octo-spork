import random
'''
 [a,b,c,d,e,f,g,h,i]
  1 2 3 4 5 6 7 8 9
 a-i are numbers
 Position 2 is a peak if and only if b >= a and b >= c.
 Position 9 is a peak if i >= h.
 Position 1 is a peak if a >=b.
 Problem: Find a peak.
'''

# Straightforward algorithm implementation. Worst case complexity - O(n) - goes through entire array
def find_1D_peak_n_complexity(array):
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
#    else:
#        return []
    return array[i]

# Divide & Conquer implementation. Worst case complexity - O(log2 n)
def find_1D_peak_logn_complexity(array):
    while len(array) != 0:
        array_middle = int(len(array) / 2)
        if array_middle != len(array) - 1 and array[array_middle] < array[array_middle + 1]:
            array = array[array_middle:]
            continue
        elif array_middle != 0 and array[array_middle] < array[array_middle - 1]:
            array = array[:array_middle]
            continue
        else:
            break
#    else:
#        return []
    return array[array_middle]

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

# Greedy Ascent Algorithm (Hill Climbing). Worst case complexity - O(nm)

def find_2D_peak_mn_complexity(array, starting_point = []):
    if starting_point == []:
        current_position = [len(array)//2, len(array[0])//2]
    else:
        current_position = starting_point
    peak_found = False
    for _ in range(len(array) * len(array[0])):
        possible_peak = array[current_position[0]][current_position[1]]
        if current_position[0] != 0 and possible_peak < array[current_position[0] - 1][current_position[1]]:
            current_position[0] -= 1
            continue
        elif current_position[0] != len(array[current_position[0]]) - 1 and possible_peak < array[current_position[0] + 1][current_position[1]]:
            current_position[0] += 1
            continue
        elif current_position[1] != 0 and possible_peak < array[current_position[0]][current_position[1] - 1]:
            current_position[1] -= 1
            continue
        elif current_position[1] != len(array[current_position[1]]) - 1 and possible_peak < array[current_position[0]][current_position[1] + 1]:
            current_position[1] += 1
            continue
        else:
            break
#    else:
#        return []
    return array[current_position[0]][current_position[1]]

array = []
for a in range(10):
    array.append([])
    for b in range(10):
        array[a].append(random.randint(10,99))
        print(array[a][b], end=' ')
    print("")
print(find_2D_peak_mn_complexity(array))