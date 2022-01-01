
def freq_worf_k(input, k):
    ### Another Logic
    # if word in result:
    #     result[word] +=1
    # else:
    #     result[word] = 1

    result = {}

    words = input.split()
    for word in words:

        result[word] = result.get(word, 0) + 1


    for i in result:
        if k == result[i]:
            print(i)


test = "Test My Bat it it it sound sound so good good"
k = 2
freq_worf_k(test, k)