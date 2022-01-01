def find_uniq(arr):

    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if i != j and arr[i] == arr[j]:
                count += 1

        if count == 0:
            return arr[i]
    return -1

# arr = [2,3,1,6,3,6,2]
arr = [2 ,4, 7, 2, 7]
print(find_uniq(arr))

