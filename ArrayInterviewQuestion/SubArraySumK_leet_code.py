def sub_Sum_k(arr, k):
    count = 0
    max_sum = 0
    sum = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            sum += arr[j]
            if sum == k:    
                count = count + 1
        sum = 0
    return count

list1 = [9,4,20,3,10,5]
k = 33

tt = sub_Sum_k(list1, k)
print(tt)