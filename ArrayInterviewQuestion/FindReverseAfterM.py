def revese_after_m(arr, m):
    res = []
    first_half = arr[:m+1]
    second_half = arr[m+1:]
    second_half.reverse()
    res[:] = first_half + second_half
    return res

input = [1, 2, 3, 4, 5, 6]
m = 3
input1 = [10 ,9 ,8 ,7 ,6]
n = 2
print(revese_after_m(input1, n))
