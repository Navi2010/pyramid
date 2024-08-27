x = int(input('enter number of rows: '))

for i in range (1, x+1):
    print (' '*(x - i), end=' ')
    for h in range (1, i+1):
        print (h, end=' ')
    print ()    

for i in range (x-1, 0, -1):
    print (' '*(x - i), end=' ')
    for h in range (1, i+1):
        print (h, end=' ')
    print ()    