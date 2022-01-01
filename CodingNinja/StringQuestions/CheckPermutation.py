def check_permutation(string1, string2):
    if len(string1) != len(string2):
        return False

    freq = [0] * 256
    for i in range(len(string1)):
        ch = ord(string1[i])
        freq[ch] += 1

    for i in range(len(string2)):
        ch = ord(string2[i])
        freq[ch] -= 1

    for i in range(256):
        if freq[i] != 0:
            return False

    return True

# string1 = "abcde"
# string2 = "baedc"

string1 = "abc"
string2 = "cbd"
print(check_permutation(string1, string2))

