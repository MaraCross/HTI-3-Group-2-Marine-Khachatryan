year = int(input("enter year: "))
a = year // 100
b = year % 100
if a == 0 and b != 0:
    print(a + 1)
elif a != 0 and b == 0:
    print(a)
elif a != 0 and b != 0:
    print(a + 1)
    