a = input()
k=0
for i in range(int(len(a) // 2)+1):
    if a[i] == a[-(i + 1)]:
        k=1
    else:
        k=0
        break
if k == 1:
    print('Yes')
else:
    print('No')
    