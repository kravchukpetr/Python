a=int(input())
b=int(input())
h=int(input())
if h>=a and h<b:
    print('Это нормально')
elif h>b:
        print('Пересып')
else:
        print('Недосып')
