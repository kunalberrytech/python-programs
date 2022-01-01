def bubble_sort(list1):
    for i in range(0, len(list1) - 1):
        for j in range(0, len(list1) - i - 1):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]

    return list1

arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))
