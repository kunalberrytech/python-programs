def normal_list():
    list1 = []
    for i in range(0, 6):
       list1.append(i)
    return list1

def generator_list():
    for i in range(0, 6):
        yield i

print(normal_list())
a = generator_list()
print(next(a))
print(next(a))
print(next(a))
print(next(a))




