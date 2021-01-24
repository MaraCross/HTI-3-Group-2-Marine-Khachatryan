def armat(n):
    while True:
        sum_num = 0
        for i in range(len(n)):
            sum_num += n[i]
        if sum_num > 9:
            n = [int(i) for i in str(sum_num)]
        else:
            break
    return sum_num

n = [int(i) for i in input()]
print(armat(n))
