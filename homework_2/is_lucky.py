a = [int(i) for i in input()]
sum1 = 0
sum2 = 0
for i in range(int(len(a) / 2)):
    sum1 += a[i]
    sum2 += a[-(i + 1)]
if sum1 == sum2:
    print('Yes')
else:
    print('No')
    