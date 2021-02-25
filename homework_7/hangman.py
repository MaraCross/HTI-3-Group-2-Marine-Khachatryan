def game_2():
    import random
    f = open('fruits.txt').read().splitlines()
    line = random.choice(f)
    # print(line)
    s=list('_'*len(line))
    i = 4
    print('Guess the word.5 mistakes left')
    print(' '.join(s))
    while i >=0:
        l = input('Guess a letter: ')
        k = 0

        for j in range(len(line)):
            if line[j] == l:
                s[j] = l
                k += 1
        if k!=0:
            print(' '.join(s))
            if not '_' in s:
                print('You won the game')
                break
        else:
            if i == 0:
                print('You lost the game')
                break
            else:
                print(' '.join(s))
                print('Guess the word.{} mistakes left'.format(i))
                i -= 1        
game_2()
