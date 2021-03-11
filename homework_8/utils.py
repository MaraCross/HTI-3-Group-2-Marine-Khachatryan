import sys
start = sys.argv[1]
stop = sys.argv[2]
def gen(start, stop):
    for i in range(int(start),int(stop)):
        k = 0
        for j in range(len(str(i))):
            
            if int((str(i))[j]) % 2 != 0:
                k += 1
                continue
            else:
                break
        if k == len(str(i)):
            yield i
            
for i in gen(start, stop):
    print(i, end=' ')
    