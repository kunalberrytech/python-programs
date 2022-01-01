# def arr_test(list1):
#     max_sum = 0
#     for i in range(0,len(list1)-1):
#         curr_sum = 0
#         for j in range(i, len(list1) -1):
#             curr_sum = curr_sum + list1[j]
#             if curr_sum > max_sum:
#                 max_sum = curr_sum
#     return max_sum
#

                    ################## Using Kadne Algorithm ##########################
import sys
def kadne_alg(list1):

    curr_sum = 0
    max_sum = -sys.maxsize-1
    for i in range(0, len(list1)-1):
        curr_sum = curr_sum + list1[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0

    return max_sum

# Input: [-3, -4, 5, -1, 2, -4, 6, -1]
# Output: 8

list = [-3, -4, 5, -1, 2, -4, 6, -1]
print(kadne_alg(list))