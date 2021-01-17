a=[int(i) for i in input().split()]
max=a[0]*a[1]
for i in range(len(a)-1):
    if a[i] * a[i + 1] >= max:
        max=a[i] * a[i + 1] 
print(max)
