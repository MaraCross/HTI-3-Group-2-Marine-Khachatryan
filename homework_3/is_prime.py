def parz_num(n):
    if n == 1:
        ans = 'No'
    elif n == 2:
        ans = 'Yes'
    else:
        for i in range(3, n + 1):
            for j in range(2, i):
                if i % j == 0:
                    ans = 'No'
                    break
                else:
                    ans = 'Yes'
    return ans
n = int(input())
print(parz_num(n))
