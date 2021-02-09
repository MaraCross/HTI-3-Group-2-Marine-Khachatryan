def r_to_i(hrom):
    dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M':1000    
    }
    s = 0
    for i in range(len(hrom) - 1, -1, -2):
        if i == 0:
            s += dict[hrom[i]]
            break
        if dict[hrom[i]] > dict[hrom[i - 1]]:
            s += dict[hrom[i]] - dict[hrom[i - 1]]
        else:
            s += dict[hrom[i]] + dict[hrom[i - 1]]
    return s
lett = list(input())
result = r_to_i(lett)
print(result)
