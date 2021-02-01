def rem_fail(n):
    new_1=n.copy()
    for i in new_1.keys():
        if int(n[i]) < 60:
            del n[i]
    return n
s = {}
for i in range(int(input())):
    a = input().split(' ')
    s[a[0]] = a[1]
print(rem_fail(s))
