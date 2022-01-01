def find_duplicate(arr):
    dict1 = {}
    for i in arr:
        if i in dict1:
            dict1[i] = dict1[i] + 1
        else:
            dict1[i] = 1
    res = []
    for i in arr:
        if dict1[i] > 1:
            res.append(i)
    res.sort()
    test = set(res)
    res = list(test)
    return res

input = [0, 2, 1, 2, 3]
input1 = [3 ,2 ,1 ,3 ,2, 1, 5]
print(find_duplicate(input))



