def sum_min_and_max(arr):
    max = 0
    min = 100000

    for i in arr:
        if i > max:
            max = i
        if i < min:
            min = i
    return min + max

input = [1 ,2 ,4 ,5 ,6 ,6,6 ]
print(sum_min_and_max(input))