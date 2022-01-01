def check_dupli(nums):
    res = 0
    dict1 = {}
    for i in nums:
        if i in dict1:
            res += dict1[i]
            dict1[i] += 1
        else:
            dict1[i] = 1

    return res


nums = [1,2,3,1,1,3]
nums1 = [1,1,1,1]
print(check_dupli(nums1))