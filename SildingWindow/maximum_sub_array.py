def max_sum_arr(arr,k):
    i = 0
    sum = 0
    j = 0
    maxi = 0
    while j < len(arr):
        sum += arr[j]
        if (j - i) + 1 < k:
            j += 1
        elif (j - i) + 1 == k:
            maxi = max(sum, maxi)
            sum = sum - arr[i]
            i += 1
            j += 1

    return maxi

input = [3, 5, 2, 1, 7]
k = 2
print(max_sum_arr(input, k))
