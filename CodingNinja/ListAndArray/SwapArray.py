def swap_alternate(arr, n):
    if n % 2 == 0:
        for i in range(0, len(arr)- 1,2):
            c = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = c
    else:
        for i in range(0, len(arr) -2,1):
            c = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = c
    return arr


arr = [9, 3, 6, 12, 4, 32]
n = 6
print(swap_alternate(arr, n))

