def print_decresing(n):
    if n == 0:
        return
    print(n)
    print_decresing(n-1)

n = int(input())
print_decresing(n)