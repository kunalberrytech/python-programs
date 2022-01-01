def highest_occuring_character(input):
    dict = {}
    for i in input:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    max = 0
    tes = ""
    for key,value in dict.items():

        if value > max:
            # print(key,value)
            max = value
            tes = key
    return tes

    # res = max(dict, key = dict.get)

input = "acccbbaba"
print(highest_occuring_character(input))