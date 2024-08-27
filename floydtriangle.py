x = int(input('enter number of rows: '))
number = 1

for i in range (x):
    for h in range(i + 1):
        print (number, end=' ')
        number += 1
    print ()
