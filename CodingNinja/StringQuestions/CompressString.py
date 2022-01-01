def compress_string(input):
    res = ""
    count = 1
    for i in range(len(input) - 1):
        if input[i] == input[i+1]:
            count += 1
        else:
            if count == 1:
                res = res + input[i]
            else:
                res += input[i] + str(count)
                count = 1
    return res

input = "aaabbcddeeeee"
# output = "a3b2cd2e5"
print(compress_string(input))