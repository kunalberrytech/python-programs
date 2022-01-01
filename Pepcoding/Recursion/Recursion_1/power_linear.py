def power_linear(x, n):
    if n == 0:
        return 1
    return x * power_linear(x,n-1)

n = int(input())
x = int(input())
print(power_linear(n,x))