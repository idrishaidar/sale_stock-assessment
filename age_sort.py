import math
import time

start_time = time.time()

input_file = open('age.txt', 'r')
output_file = open('sorted_age.txt', 'w')

age_lines = input_file.readlines()

def my_sort(list_input):
    if len(list_input) > 1:
        mid = math.floor(len(list_input)/2)
        left = list_input[:mid]
        right = list_input[mid:]

        my_sort(left)
        my_sort(right)

        ii = 0
        jj = 0
        kk = 0

        while ii < int(len(left)) and jj < int(len(right)):
            if int(left[ii]) < int(right[jj]):
                list_input[kk] = left[ii]
                ii += 1
            else:
                list_input[kk] = right[jj]
                jj += 1
            kk += 1

        while ii < int(len(left)):
            list_input[kk] = left[ii]
            kk += 1
            ii += 1

        while jj < int(len(right)):
            list_input[kk] = right[jj]
            kk += 1
            jj += 1
    return(list_input)

sorted = my_sort(age_lines)
for ag in sorted:
    output_file.write(ag)

input_file.close()
output_file.close()