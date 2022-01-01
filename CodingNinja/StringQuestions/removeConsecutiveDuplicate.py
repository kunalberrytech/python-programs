def remove_consscutive_dupli(string1):
    res = ""
    for i in range(len(string1)):
        if  i != len(string1)-1 and string1[i] == string1[i+1]:
            continue
        else:
            res += string1[i]
    return  res



#string1 = "aabccbaa"
string1 = "xxyyzxx"
print(remove_consscutive_dupli(string1))
