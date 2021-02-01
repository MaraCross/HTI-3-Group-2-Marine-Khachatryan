def hetero(n):
    a1=''.join(n).lower()
    s = set()
    s.update(a1)
    if len(a1)==len(s):
        return 'Yes'
    else:
        return 'No'
a = [i for i in input().split()]
print(hetero(a))
