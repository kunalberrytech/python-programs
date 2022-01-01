# List Comprehension  Example
list1 = [1,2,3,4,5,6,7,8,9]

list1 = [1,2,3]
check1 = [i * 10 for i in list1]
print(check1)

my_list = [i*i for i in list1 if i % 2 ==0]
# print(my_list)

name1 = ['a','b','c']
int1 = [1,2,3]

dict_compr = {k: v**2 for k, v in zip(name1, int1)}
# print(dict_compr)


