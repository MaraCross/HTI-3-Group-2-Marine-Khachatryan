def recur(start, a, b, liss,):
    count = 0
    if b == 0:
        print(' '.join(map(str, liss)))
        return 1
    for i in range(start, a + 1):
        liss.append(i)
        count+=recur(i, a, b - 1, liss)
        liss.pop()
    return count
n = int(input())
k = int(input())
res = recur(1, n, k, [])
print('Total: {}'.format(res))