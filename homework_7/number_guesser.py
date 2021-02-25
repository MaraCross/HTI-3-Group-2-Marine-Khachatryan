def game_1():
    max1 = 1000
    min1 = 0
    a = 500
    print('1:',a)
    for i in range(2, 12):
        q = int(input())
    
        if q == 0:
            print('your number is {}'.format(a))
            break
        if i == 11 and q != 0 :
            print('I couldn’t guess in 10 steps! This means you cheated!')
        
        elif q == 1:
            min1 = a
            a = (min1 + max1) // 2
            print('{}:'.format(i),a)
    
        elif q == -1:
            max1 = a
            a = (max1+min1) // 2
            print('{}:'.format(i),a)
game_1()

        