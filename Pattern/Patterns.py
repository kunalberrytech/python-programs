# 1
# 11
# 111
# 1111
def pattern1(n):
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            print("1", end='')
            j += 1
        print()
        i += 1

######################      2 .      ####################
# 		*
# 	*	*	*
# *	*	*	*	*
# 	*	*	*
# 		*

def diamondpattern(n):
    star = 1
    space = int(n / 2)
    i = 1
    while i <= n:
        k = 1
        while k <= space:
            print(" ",end="")
            k += 1
        j = 1
        while j <= star:
            print("* ", end="")
            j += 1

        if i < (n / 2):
            space = space - 1
            star = star + 2
        else:
            space = space + 1
            star = star - 2
        i += 1
        print()

n = int(input())
diamondpattern(n)