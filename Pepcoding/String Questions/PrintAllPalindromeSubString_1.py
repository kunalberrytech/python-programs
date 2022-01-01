def is_Palindrome(str):
    i = 0
    j = len(str) - 1
    while i <= j:
        if str[i] != str[j]:
            return False
        i += 1
        j -= 1
    return True

def print_palidrome(input):
    for i in range(0,len(input)):
        for j in range(1, len(input) + 1):
            if i + j <= len(input):
                sub = input[i:i+j]
                if is_Palindrome(sub):
                    print(sub)



input = 'abcc'
print_palidrome(input)
