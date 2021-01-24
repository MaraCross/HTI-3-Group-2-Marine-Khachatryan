def factor_func(n):
    fact = 1
    if n == 0:
        fact = 1
    else:
        for i in range(1, n + 1):
            fact *= i
    return fact
n = int(input())
print(factor_func(n))
