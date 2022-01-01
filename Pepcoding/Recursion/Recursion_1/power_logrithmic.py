def power_logrithmic(x, n):
    if n == 0:
        return 1
    xpnb2 = power_logrithmic(x, n // 2)
    xn = xpnb2 * xpnb2

    if n % 2 == 1:
        xn = xn * x

    return xn


n = int(input())
x = int(input())
print(power_logrithmic(n,x))
