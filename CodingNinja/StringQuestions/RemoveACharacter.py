def remove_a_character(string, x):
    res = ""
    for i in range(len(string)):
        if string[i] == x:
            continue
        else:
            res = res + string[i]

    return res

if __name__ == '__main__':
    # input = "aabccbaa"
    # ch = 'a'
    input = "xxyyzxx"
    ch = 'y'
    print(remove_a_character(input, ch))




