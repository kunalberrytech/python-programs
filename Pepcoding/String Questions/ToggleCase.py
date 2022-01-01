def togglecase(st):
    res = ""
    for i in range(0, len(st)):
        ch = st[i]
        if ch >= 'a' and ch <= 'z':
            res += chr(ord('A') + ord(ch) - ord('a'))
        else:
            res += chr(ord('a') + ord(ch) - ord('A'))

    print(res)

if __name__ == '__main__':
    st = input()
    togglecase(st)