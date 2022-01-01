def max_freq(arr):
    dict = {}
    for i in arr:
        dict[i] = dict.get(i, 0) + 1

    max = arr[0]
    for i in arr:
        if dict[i] > dict[max]:
            max = i

    return  max

input = [2, 12, 2, 11, 12, 2, 1, 2, 2, 11, 12, 2, 6]
input2 = [1, 4 ,5]
print(max_freq(input2))

