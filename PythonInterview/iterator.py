nums = [1, 2, 3]
# print(dir(nums))

value = nums.__iter__()
print(value.__next__())
print(value.__next__())
print(value.__next__())