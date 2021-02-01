def stools(n):
    max_1 = max(n)
    s = 0
    for i in range(len(n)):
        if max_1 - n[i] != 0:
            s += max_1 - n[i]
    return(s)
a = [int(i) for i in input().split()]
print(stools(a))