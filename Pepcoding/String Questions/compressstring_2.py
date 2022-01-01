def String_compression01(st):
    # write your code here
    res = ""
    res += st[0]

    for i in range(1, len(st)):
        curr = st[i]
        prev = st[i - 1]
        if curr != prev:
            res += curr
    #    if res[len(res) - 1] != st[i]:
    #        res += st[i]

    print(res)


def String_compression02(st):
    # write your code here
    res = ""
    res += st[0]
    count = 1

    for i in range(1, len(st)):
        prev = st[i - 1]
        curr = st[i]

        if curr == prev:
            count += 1
        else:
            if count > 1:
                res += str(count)
                count = 1
            res += curr

    if count > 1:
        res += str(count)

    print(res)


st = input()
String_compression01(st)
String_compression02(st)