def pal_(text1):
    if len(text1) < 2:
        return 'Yes'
    if text1[0] == text1[len(text1) - 1]:
        del text1[0]
        text1.pop()
        return pal_(text1)
    else:    
        return 'No'
lett = list(input())
result = pal_(lett)
print(result)
