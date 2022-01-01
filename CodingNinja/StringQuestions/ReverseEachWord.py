def reverse_each_word(input):
    final_result = ""
    input1 = input.split(" ")
    for i in input1:
        res = ""
        for j in range(len(i)):
            res = i[j] + res
        final_result = final_result + res + " "
    return final_result

string = "Always indent your code"
#string = "kunal berry"
print(reverse_each_word(string))