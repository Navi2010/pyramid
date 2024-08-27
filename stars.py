print ('half pyramid of stars: ')

rows = int(input('enter how many rows: '))

for x in range(rows + 1):
    for star in range(x):
        print('*', end=' ')
    print ()    